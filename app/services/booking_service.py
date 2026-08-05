from app.repositories.booking_repository import BookingRepository
from app.exceptions.BookingExceptions import *
from app.services.base_service import BaseService


class BookingService(BaseService):
    repository = BookingRepository
    entity_name = "Бронирование"

    @classmethod
    async def get_all_bookings(cls):
        return await cls.repository.get_all()

    @classmethod
    async def get_bookings_by_user(cls, user_id: int):
        bookings = await cls.repository.get_all(user_id=user_id)
        if not bookings:
            raise BookingForUserNotFound(user_id)
        return bookings

    @classmethod
    async def get_booking_by_id(cls, booking_id: int):
        booking = await cls.repository.get_one_or_none_by_id(booking_id)
        if not booking:
            raise BookingNotFound(booking_id)
        return booking