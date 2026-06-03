from app.models import Booking
from app.repositories.base_repository import BaseRepository


class BookingRepository(BaseRepository):
    model=Booking
