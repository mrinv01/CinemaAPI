from app.repositories.booking import BookingRepository
from app.services.base import BaseService


class BookingService(BaseService[BookingRepository]):
    repository = BookingRepository
    entity_name = "Бронирование"
