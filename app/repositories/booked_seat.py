from sqlalchemy.ext.asyncio import AsyncSession

from app.models import booked_seat
from app.repositories.base import BaseRepository
from app.schemas import BookedSeatCreate, BookedSeatUpdate


class BookedSeatRepository(BaseRepository[booked_seat, BookedSeatCreate, BookedSeatUpdate]):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(booked_seat, session)
