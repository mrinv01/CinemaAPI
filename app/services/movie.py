from typing import Any

from pydantic import BaseModel

from app.repositories.movie import MovieRepository
from app.services.base import BaseService
from app.services.exceptions import EntityAlreadyExistsError, EntityNotFoundError


class MovieService(BaseService[MovieRepository]):
    repository = MovieRepository
    entity_name = "Фильм"

    @classmethod
    async def get_by_kp_id(cls, kp_id: int):
        movies = await cls.repository.get_by_kp_id(kp_id)
        if not movies:
            raise EntityNotFoundError(f"Фильм с kp_id={kp_id} не найден.")
        return movies[0]

    @classmethod
    async def create(cls, data: BaseModel | dict[str, Any]):
        values = cls._dump_schema(data)
        if await cls.repository.get_by_kp_id(values["kp_id"]):
            raise EntityAlreadyExistsError("Фильм с таким kp_id уже существует.")
        return await cls.repository.create(**values)
