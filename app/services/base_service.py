from typing import Any
from pydantic import BaseModel

from app.exceptions.GeneralException import EmptyUpdateError, EntityNotFoundError


class BaseService:
    repository = None
    entity_name = "Сущность"

    @classmethod
    def _dump_schema(cls, data: BaseModel | dict[str, Any], *, exclude_unset: bool = False) -> dict[str, Any]:
        if isinstance(data, BaseModel):
            return data.model_dump(exclude_unset=exclude_unset)
        return dict(data)

    @classmethod
    async def get_all(cls):
        return await cls.repository.get_all()

    @classmethod
    async def get(cls, entity_id: int):
        entity = await cls.repository.get_one_or_none_by_id(entity_id)
        if entity is None:
            raise EntityNotFoundError(f"{cls.entity_name} с id={entity_id} не найдена.")
        return entity

    @classmethod
    async def create(cls, data: BaseModel | dict[str, Any]):
        return await cls.repository.create(**cls._dump_schema(data))

    @classmethod
    async def update(cls, entity_id: int, data: BaseModel | dict[str, Any]):
        values = cls._dump_schema(data, exclude_unset=True)
        if not values:
            raise EmptyUpdateError("Необходимо передать хотя бы одно поле для обновления.")

        _, rowcount = await cls.repository.update({"id": entity_id}, **values)
        if rowcount == 0:
            raise EntityNotFoundError(f"{cls.entity_name} с id={entity_id} не найдена.")
        return await cls.get(entity_id)

    @classmethod
    async def delete(cls, entity_id: int):
        deleted = await cls.repository.delete(id=entity_id)
        if deleted == 0:
            raise EntityNotFoundError(f"{cls.entity_name} с id={entity_id} не найдена.")
        return None