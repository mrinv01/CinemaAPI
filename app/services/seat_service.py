from app.repositories.seat_repository import SeatRepository
from app.services.base_service import BaseService


class SeatService(BaseService):
    repository = SeatRepository
    entity_name = "Место"
