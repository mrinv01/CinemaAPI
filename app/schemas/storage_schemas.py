from pydantic import Field

from app.schemas.common_schemas import ORMBaseModel


class StorageObjectRead(ORMBaseModel):
    bucket: str = Field(min_length=1)
    object_name: str = Field(min_length=1)
    url: str = Field(min_length=1)
