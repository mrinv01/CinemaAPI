from fastapi import APIRouter, File, HTTPException, Query, UploadFile, status

from app.schemas.storage_schemas import StorageObjectRead
from app.services.storage_service import StorageService
from app.storage import (
    InvalidObjectPathError,
    ObjectStorageError,
    ObjectStorageNotFoundError,
)

router = APIRouter(prefix="/storage", tags=["Object storage"])


@router.post(
    "/upload",
    response_model=StorageObjectRead,
    status_code=status.HTTP_201_CREATED,
)
async def upload_file(
    file: UploadFile = File(...),
    directory: str | None = Query(default=None, max_length=255),
):
    try:
        return await StorageService.upload_file(file, directory)
    except InvalidObjectPathError as exc:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(exc),
        ) from exc
    except ObjectStorageError as exc:
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail=str(exc),
        ) from exc


@router.get("/{object_name:path}", response_model=StorageObjectRead)
async def get_file_url(object_name: str):
    try:
        return await StorageService.get_url(object_name)
    except ObjectStorageNotFoundError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        ) from exc
    except ObjectStorageError as exc:
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail=str(exc),
        ) from exc


@router.delete("/{object_name:path}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_file(object_name: str):
    try:
        await StorageService.delete_file(object_name)
    except ObjectStorageNotFoundError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        ) from exc
    except ObjectStorageError as exc:
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail=str(exc),
        ) from exc
