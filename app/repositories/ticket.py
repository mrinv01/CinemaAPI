from collections.abc import Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Ticket
from app.repositories.base import BaseRepository
from app.schemas import TicketCreate, TicketUpdate


class TicketRepository(BaseRepository[Ticket, TicketCreate, TicketUpdate]):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(Ticket, session)

    async def get_by_booking(self, booking_id: int) -> Sequence[Ticket]:
        stmt = select(Ticket).where(Ticket.booking_id == booking_id)
        result = await self.session.scalars(stmt)
        return result.all()

    async def get_by_showtime(self, showtime_id: int) -> Sequence[Ticket]:
        stmt = select(Ticket).where(Ticket.showtime_id == showtime_id)
        result = await self.session.scalars(stmt)
        return result.all()
