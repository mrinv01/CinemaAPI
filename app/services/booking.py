from app.repositories.booking_repository import BookingRepository
from app.services.base import BaseService


class BookingService(BaseService[BookingRepository]):
    repository = BookingRepository
    entity_name = "Бронирование"
