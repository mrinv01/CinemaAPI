from typing import Any, Generic, TypeVar

from pydantic import BaseModel

from app.services.exceptions import EmptyUpdateError, EntityNotFoundError

RepositoryT = TypeVar("RepositoryT")


class BaseService(Generic[RepositoryT]):
    """Common asynchronous CRUD operations for application services."""

    repository: type[RepositoryT]
    entity_name = "entity"

    @classmethod
    def _dump_schema(
        cls,
        data: BaseModel | dict[str, Any],
        *,
        exclude_unset: bool = False,
    ) -> dict[str, Any]:
        if isinstance(data, BaseModel):
            return data.model_dump(exclude_unset=exclude_unset)
        return dict(data)

    @classmethod
    async def get(cls, entity_id: int):
        entity = await cls.repository.get(entity_id)
        if entity is None:
            raise EntityNotFoundError(f"{cls.entity_name} с id={entity_id} не найден(а).")
        return entity

    @classmethod
    async def get_all(cls, *, offset: int = 0, limit: int = 100):
        return await cls.repository.get_all(offset=offset, limit=limit)

    @classmethod
    async def create(cls, data: BaseModel | dict[str, Any]):
        values = cls._dump_schema(data)
        return await cls.repository.create(**values)

    @classmethod
    async def update(cls, entity_id: int, data: BaseModel | dict[str, Any]):
        values = cls._dump_schema(data, exclude_unset=True)
        if not values:
            raise EmptyUpdateError("Необходимо передать хотя бы одно поле для обновления.")

        _, rowcount = await cls.repository.update({"id": entity_id}, **values)
        if rowcount == 0:
            raise EntityNotFoundError(f"{cls.entity_name} с id={entity_id} не найден(а).")
        return await cls.get(entity_id)

    @classmethod
    async def delete(cls, entity_id: int) -> int:
        rowcount = await cls.repository.delete(id=entity_id)
        if rowcount == 0:
            raise EntityNotFoundError(f"{cls.entity_name} с id={entity_id} не найден(а).")
        return rowcount
