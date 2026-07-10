from io import BytesIO
from pathlib import PurePosixPath
from typing import Any, Coroutine
from uuid import uuid4

from fastapi import UploadFile

from app.storage import InvalidObjectPathError, object_storage


class StorageService:
    @staticmethod
    def _build_object_name(file: UploadFile, directory: str | None = None) -> str:
        safe_name = PurePosixPath(file.filename or "file").name
        object_name = f"{uuid4().hex}-{safe_name}"
        if directory:
            directory_parts = PurePosixPath(directory.strip("/")).parts
            if any(part in {"", ".", ".."} for part in directory_parts):
                raise InvalidObjectPathError("Некорректный путь директории для объекта.")
            if directory_parts:
                object_name = f"{'/'.join(directory_parts)}/{object_name}"
        return object_name

    @classmethod
    async def upload_file(
        cls,
        file: UploadFile,
        directory: str | None = None,
    ) -> dict[str, str]:
        content = await file.read()
        object_name = cls._build_object_name(file, directory)
        await object_storage.upload_object(
            object_name=object_name,
            data=BytesIO(content),
            length=len(content),
            content_type=file.content_type,
        )
        url = await object_storage.get_url(object_name)
        return {
            "bucket": object_storage.bucket,
            "object_name": object_name,
            "url": url,
        }

    @staticmethod
    async def get_url(object_name: str) -> dict[str, str]:
        url = await object_storage.get_url(object_name)
        return {
            "bucket": object_storage.bucket,
            "object_name": object_name,
            "url": url,
        }

    @staticmethod
    async def delete_file(object_name: str):
        await object_storage.remove_object(object_name)