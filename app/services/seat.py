from app.repositories.seat_repository import SeatRepository


class SeatService:
    repository = SeatRepository
    entity_name = "Место"

    @classmethod
    async def get_by_hall(cls, hall_id: int):
        return await cls.repository.get_by_hall(hall_id)
