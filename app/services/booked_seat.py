from typing import Any

from pydantic import BaseModel

from app.repositories.booked_seat import BookedSeatRepository
from app.services.base import BaseService
from app.services.exceptions import EntityAlreadyExistsError, EntityNotFoundError


class BookedSeatService(BaseService[BookedSeatRepository]):
    repository = BookedSeatRepository
    entity_name = "Забронированное место"

    @classmethod
    async def get_by_showtime(cls, showtime_id: int):
        return await cls.repository.get_by_showtime(showtime_id)

    @classmethod
    async def get_by_seat(cls, seat_id: int):
        return await cls.repository.get_by_seat(seat_id)

    @classmethod
    async def get_by_showtime_and_seat(cls, showtime_id: int, seat_id: int):
        booked_seat = await cls.repository.get_by_showtime_and_seat(showtime_id, seat_id)
        if booked_seat is None:
            raise EntityNotFoundError("Забронированное место для указанного сеанса и места не найдено.")
        return booked_seat

    @classmethod
    async def create(cls, data: BaseModel | dict[str, Any]):
        values = cls._dump_schema(data)
        existing = await cls.repository.get_by_showtime_and_seat(
            values["showtime_id"],
            values["seat_id"],
        )
        if existing is not None:
            raise EntityAlreadyExistsError("Это место уже забронировано на выбранный сеанс.")
        return await cls.repository.create(**values)
