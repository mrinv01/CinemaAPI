from datetime import timedelta
from typing import Any
from urllib.parse import urlparse

import boto3
from botocore.exceptions import BotoCoreError, ClientError
from starlette.concurrency import run_in_threadpool

from app.config import settings


class ObjectStorageError(Exception):
    """Base error for object storage operations."""


class ObjectStorageNotFoundError(ObjectStorageError):
    """Raised when an object is missing in object storage."""


class InvalidObjectPathError(ObjectStorageError):
    """Raised when an object path is not safe to use as an object key."""

def _build_endpoint_url() -> str:
    endpoint = settings.MINIO_URL
    parsed_endpoint = urlparse(endpoint)
    if parsed_endpoint.scheme:
        return endpoint

    scheme = "https" if settings.MINIO_SECURE else "http"
    return f"{scheme}://{endpoint}"


def _build_s3_client() -> Any:
    return boto3.client(
        "s3",
        endpoint_url=_build_endpoint_url(),
        aws_access_key_id=settings.MINIO_ACCESS_KEY,
        aws_secret_access_key=settings.MINIO_SECRET_KEY,
    )


def _is_not_found_error(exc: ClientError) -> bool:
    error_code = exc.response.get("Error", {}).get("Code")
    return error_code in {"404", "NoSuchBucket", "NoSuchKey", "NotFound"}


class ObjectStorageClient:
    """Async-friendly wrapper around the synchronous boto3 S3 client."""

    def __init__(self, client: Any | None = None, bucket: str | None = None) -> None:
        self.client = client or _build_s3_client()
        self.bucket = bucket or settings.MINIO_BUCKET

    async def ensure_bucket(self) -> None:
        try:
            await run_in_threadpool(self.client.head_bucket, Bucket=self.bucket)
        except ClientError as exc:
            if _is_not_found_error(exc):
                await self._create_bucket()
                return
            raise ObjectStorageError(str(exc)) from exc
        except BotoCoreError as exc:
            raise ObjectStorageError(str(exc)) from exc

    async def _create_bucket(self) -> None:
        try:
            await run_in_threadpool(self.client.create_bucket, Bucket=self.bucket)
        except (BotoCoreError, ClientError) as exc:
            raise ObjectStorageError(str(exc)) from exc

    async def upload_object(
        self,
        object_name: str,
        data,
        length: int,
        content_type: str | None = None,
    ) -> str:
        await self.ensure_bucket()
        try:
            await run_in_threadpool(
                self.client.put_object,
                Bucket=self.bucket,
                Key=object_name,
                Body=data,
                ContentLength=length,
                ContentType=content_type or "application/octet-stream",
            )
        except (BotoCoreError, ClientError) as exc:
            raise ObjectStorageError(str(exc)) from exc
        return object_name

    async def remove_object(self, object_name: str) -> None:
        await self._ensure_object_exists(object_name)
        try:
            await run_in_threadpool(
                self.client.delete_object,
                Bucket=self.bucket,
                Key=object_name,
            )
        except (BotoCoreError, ClientError) as exc:
            raise ObjectStorageError(str(exc)) from exc

    async def get_presigned_url(
        self,
        object_name: str,
        expires: timedelta | None = None,
    ) -> str:
        await self._ensure_object_exists(object_name)
        expires_in = int((expires or timedelta(hours=1)).total_seconds())
        try:
            return await run_in_threadpool(
                self.client.generate_presigned_url,
                "get_object",
                Params={"Bucket": self.bucket, "Key": object_name},
                ExpiresIn=expires_in,
            )
        except (BotoCoreError, ClientError) as exc:
            raise ObjectStorageError(str(exc)) from exc

    async def get_url(self, object_name: str) -> str:
        await self._ensure_object_exists(object_name)
        return f"{_build_endpoint_url()}/{self.bucket}/{object_name}"

    async def _ensure_object_exists(self, object_name: str) -> None:
        try:
            await run_in_threadpool(
                self.client.head_object,
                Bucket=self.bucket,
                Key=object_name,
            )
        except ClientError as exc:
            if _is_not_found_error(exc):
                raise ObjectStorageNotFoundError(
                    f"Объект {object_name} не найден в хранилище."
                ) from exc
            raise ObjectStorageError(str(exc)) from exc
        except BotoCoreError as exc:
            raise ObjectStorageError(str(exc)) from exc


object_storage = ObjectStorageClient()
