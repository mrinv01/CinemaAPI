from app.repositories.ticket_repository import TicketRepository
from app.services.base_service import BaseService

class TicketService(BaseService):
    repository = TicketRepository
    entity_name = "Билет"

    @classmethod
    async def get_by_booking(cls, booking_id: int):
        return await cls.repository.get_by_booking(booking_id)

    @classmethod
    async def get_by_showtime(cls, showtime_id: int):
        return await cls.repository.get_by_showtime(showtime_id)
