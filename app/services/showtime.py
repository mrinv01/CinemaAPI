from datetime import datetime

from app.repositories.showtime import ShowtimeRepository
from app.services.base import BaseService


class ShowtimeService(BaseService[ShowtimeRepository]):
    repository = ShowtimeRepository
    entity_name = "Сеанс"

    @classmethod
    async def get_by_movie(cls, movie_id: int):
        return await cls.repository.get_by_movie(movie_id)

    @classmethod
    async def get_by_hall(cls, hall_id: int):
        return await cls.repository.get_by_hall(hall_id)

    @classmethod
    async def get_between(cls, start_time: datetime, end_time: datetime):
        return await cls.repository.get_between(start_time, end_time)
