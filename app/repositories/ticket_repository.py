from sqlalchemy import select
from app.models import Ticket
from app.repositories.base_repository import BaseRepository
from app.database import async_session_maker

class TicketRepository(BaseRepository):
    model = Ticket

    @classmethod
    async def get_by_booking(cls, booking_id: int):
        async with async_session_maker() as session:
            stmt = select(Ticket).where(Ticket.booking_id == booking_id)
            result = await session.scalars(stmt)
            return result.all()

    @classmethod
    async def get_by_showtime(cls, showtime_id: int):
        async with async_session_maker() as session:
            stmt = select(Ticket).where(Ticket.showtime_id == showtime_id)
            result = await session.scalars(stmt)
            return result.all()
