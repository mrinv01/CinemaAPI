from collections.abc import Sequence
from datetime import datetime

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Showtime
from app.repositories.base import BaseRepository
from app.schemas import ShowtimeCreate, ShowtimeUpdate


class ShowtimeRepository(BaseRepository[Showtime, ShowtimeCreate, ShowtimeUpdate]):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(Showtime, session)

    async def get_by_movie(self, movie_id: int) -> Sequence[Showtime]:
        stmt = select(Showtime).where(Showtime.movie_id == movie_id)
        result = await self.session.scalars(stmt)
        return result.all()

    async def get_by_hall(self, hall_id: int) -> Sequence[Showtime]:
        stmt = select(Showtime).where(Showtime.hall_id == hall_id)
        result = await self.session.scalars(stmt)
        return result.all()

    async def get_between(self, start_time: datetime, end_time: datetime) -> Sequence[Showtime]:
        stmt = select(Showtime).where(
            Showtime.start_time >= start_time,
            Showtime.end_time <= end_time,
        )
        result = await self.session.scalars(stmt)
        return result.all()
