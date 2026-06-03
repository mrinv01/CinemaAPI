from app.models import booked_seat
from app.repositories.base_repository import BaseRepository


class BookedSeatRepository(BaseRepository):
    model = booked_seat
