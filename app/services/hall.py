from app.repositories.hall import HallRepository
from app.services.base import BaseService


class HallService(BaseService[HallRepository]):
    repository = HallRepository
    entity_name = "Зал"
