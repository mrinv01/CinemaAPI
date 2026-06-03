from sqlalchemy import select
from app.models import Seat
from app.repositories.base import BaseRepository
from app.database import async_session_maker

class SeatRepository(BaseRepository):
    model = Seat

    @classmethod
    async def get_by_hall(cls, hall_id: int):
        async with async_session_maker() as session:
            stmt = select(Seat).where(Seat.hall_id == hall_id)
            result = await session.scalars(stmt)
            return result.all()
