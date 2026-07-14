from typing import Any

from pydantic import BaseModel

from app.schemas.movie_schemas import *
from app.repositories.movie_repository import MovieRepository
from app.exceptions.MovieExceptions import MovieNotFound
from app.services.exceptions import EntityAlreadyExistsError, EntityNotFoundError


class MovieService:

    @staticmethod
    async def get_all_movies():
        return await MovieRepository.get_all()

    @staticmethod
    async def get_by_kp_id(kp_id: int):
        movies = await MovieRepository.get_by_kp_id(kp_id)
        if not movies:
            raise MovieNotFound(kp_id)
        return movies[0]

    @staticmethod
    async def create(data: MovieCreate):
        return await MovieRepository.create(**data.model_dump())

    @staticmethod
    async def delete(kp_id: int):
        deleted = await MovieRepository.delete(id=kp_id)
        if deleted == 0:
            raise MovieNotFound(kp_id)
        return {"message": f"Фильм с kp-id {kp_id} успешно удалён."}

