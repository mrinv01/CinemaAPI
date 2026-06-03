from app.repositories.hall_repository import HallRepository
from app.services.base import BaseService


class HallService(BaseService[HallRepository]):
    repository = HallRepository
    entity_name = "Зал"
