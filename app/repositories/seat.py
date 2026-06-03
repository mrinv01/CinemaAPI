from collections.abc import Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Seat
from app.repositories.base import BaseRepository
from app.schemas import SeatCreate, SeatUpdate


class SeatRepository(BaseRepository[Seat, SeatCreate, SeatUpdate]):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(Seat, session)

    async def get_by_hall(self, hall_id: int) -> Sequence[Seat]:
        stmt = select(Seat).where(Seat.hall_id == hall_id)
        result = await self.session.scalars(stmt)
        return result.all()
