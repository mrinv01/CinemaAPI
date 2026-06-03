from app.models import booked_seat
from app.repositories.base import BaseRepository


class BookedSeatRepository(BaseRepository):
    model = booked_seat
