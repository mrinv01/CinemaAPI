from collections.abc import Sequence
from typing import Any, Generic, TypeVar

from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import Base

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class BaseRepository(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    """Base repository with common asynchronous CRUD operations."""

    def __init__(self, model: type[ModelType], session: AsyncSession) -> None:
        self.model = model
        self.session = session

    async def get(self, entity_id: int) -> ModelType | None:
        return await self.session.get(self.model, entity_id)

    async def get_all(self, *, offset: int = 0, limit: int = 100) -> Sequence[ModelType]:
        stmt = select(self.model).offset(offset).limit(limit)
        result = await self.session.scalars(stmt)
        return result.all()

    async def create(self, data: CreateSchemaType | dict[str, Any]) -> ModelType:
        entity = self.model(**self._dump_create_data(data))
        self.session.add(entity)
        await self.session.commit()
        await self.session.refresh(entity)
        return entity

    async def update(
        self,
        entity: ModelType,
        data: UpdateSchemaType | dict[str, Any],
    ) -> ModelType:
        update_data = self._dump_update_data(data)
        for field, value in update_data.items():
            setattr(entity, field, value)

        self.session.add(entity)
        await self.session.commit()
        await self.session.refresh(entity)
        return entity

    async def delete(self, entity: ModelType) -> None:
        await self.session.delete(entity)
        await self.session.commit()

    def _dump_create_data(self, data: CreateSchemaType | dict[str, Any]) -> dict[str, Any]:
        if isinstance(data, BaseModel):
            return data.model_dump()
        return data

    def _dump_update_data(self, data: UpdateSchemaType | dict[str, Any]) -> dict[str, Any]:
        if isinstance(data, BaseModel):
            return data.model_dump(exclude_unset=True)
        return {field: value for field, value in data.items() if value is not None}
