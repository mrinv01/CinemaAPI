from app.schemas.booking_schemas import *
from app.repositories.booking_repository import BookingRepository
from app.exceptions.BookingExceptions import *


class BookingService:
    @staticmethod
    async def get_all_bookings():
        return await BookingRepository.get_all()

    @staticmethod
    async def get_bookings_by_user(user_id: int):
        bookings = await BookingRepository.get_all(user_id=user_id)
        if not bookings:
            raise BookingForUserNotFound(user_id)
        return bookings

    @staticmethod
    async def get_booking_by_id(booking_id: int):
        booking = await BookingRepository.get_one_or_none_by_id(booking_id)
        if not booking:
            raise BookingNotFound(booking_id)
        return booking