from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Movie
from app.repositories.base import BaseRepository
from app.schemas import MovieCreate, MovieUpdate


class MovieRepository(BaseRepository[Movie, MovieCreate, MovieUpdate]):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(Movie, session)

    async def get_by_kp_id(self, kp_id: int) -> Movie | None:
        stmt = select(Movie).where(Movie.kp_id == kp_id)
        return await self.session.scalar(stmt)
