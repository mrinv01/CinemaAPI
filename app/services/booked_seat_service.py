from app.schemas.booked_seat_schemas import *
from app.repositories.booked_seat_repository import BookedSeatRepository
from app.repositories.seat_repository import SeatRepository
from app.repositories.showtime_repository import ShowtimeRepository
from app.services.exceptions import EntityAlreadyExistsError, EntityNotFoundError
from app.exceptions.SeatExceptions import *
from app.exceptions.ShowtimeExceptions import ShowtimeNotFound
from app.exceptions.SeatExceptions import SeatNotFound


class BookedSeatService:

    @staticmethod
    async def get_by_showtime(showtime_id: int):
        return await BookedSeatRepository.get_by_showtime(showtime_id)

    @staticmethod
    async def get_by_seat(seat_id: int):
        return await BookedSeatRepository.get_by_seat(seat_id)

    @staticmethod
    async def get_by_showtime_and_seat(showtime_id: int, seat_id: int):
        booked_seat = await BookedSeatRepository.get_by_showtime_and_seat(showtime_id, seat_id)
        if booked_seat is None:
            raise EntityNotFoundError("Забронированное место для указанного сеанса и места не найдено.")
        return booked_seat

    @staticmethod
    async def create(data: BookedSeatCreate):
        showtime = await ShowtimeRepository.get_one_by_id(data.showtime_id)
        seat = await SeatRepository.get_one_by_id(data.seat_id)
        existing = await BookedSeatRepository.get_by_showtime_and_seat(
            data.showtime_id,
            data.seat_id,
        )

        if existing:
            raise EntityAlreadyExistsError("Это место уже забронировано на выбранный сеанс.")
        if not showtime:
            raise ShowtimeNotFound(data.showtime_id)
        if not seat:
            raise SeatNotFound(data.seat_id)

        return await BookedSeatRepository.create(**data.model_dump())


    @staticmethod
    async def delete(booked_seat_id: int):
        deleted = await BookedSeatRepository.delete(id=booked_seat_id)
        if deleted == 0:
            raise SeatNotFound(booked_seat_id)
        return {"message": f"Место с id {booked_seat_id} успешно удалёно."}

