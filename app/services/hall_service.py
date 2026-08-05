from app.repositories.hall_repository import HallRepository
from app.services.base_service import BaseService

class HallService(BaseService):
    repository = HallRepository
    entity_name = "Зал"
