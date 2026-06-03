from app.models import Hall
from app.repositories.base import BaseRepository

class HallRepository(BaseRepository):
    model = Hall
