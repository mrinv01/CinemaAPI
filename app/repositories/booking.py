from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Booking
from app.repositories.base import BaseRepository
from app.schemas import BookingCreate, BookingUpdate


class BookingRepository(BaseRepository[Booking, BookingCreate, BookingUpdate]):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(Booking, session)
