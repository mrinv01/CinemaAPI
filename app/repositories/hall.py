from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Hall
from app.repositories.base import BaseRepository
from app.schemas import HallCreate, HallUpdate


class HallRepository(BaseRepository[Hall, HallCreate, HallUpdate]):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(Hall, session)
