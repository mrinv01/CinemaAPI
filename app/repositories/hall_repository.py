from app.models import Hall
from app.repositories.base_repository import BaseRepository

class HallRepository(BaseRepository):
    model = Hall
