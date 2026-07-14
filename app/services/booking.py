from app.repositories.booking_repository import BookingRepository


class BookingService:
    repository = BookingRepository
    entity_name = "Бронирование"
