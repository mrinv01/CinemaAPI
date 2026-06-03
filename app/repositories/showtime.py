from datetime import datetime
from sqlalchemy import select
from app.models import Showtime
from app.repositories.base import BaseRepository
from app.database import async_session_maker

class ShowtimeRepository(BaseRepository):
    model = Showtime

    @classmethod
    async def get_by_movie(cls, movie_id: int):
        async with async_session_maker() as session:
            stmt = select(Showtime).where(Showtime.movie_id == movie_id)
            result = await session.scalars(stmt)
            return result.all()

    @classmethod
    async def get_by_hall(cls, hall_id: int):
        async with async_session_maker() as session:
            stmt = select(Showtime).where(Showtime.hall_id == hall_id)
            result = await session.scalars(stmt)
            return result.all()

    @classmethod
    async def get_between(cls, start_time: datetime, end_time: datetime):
        async with async_session_maker() as session:
            stmt = select(Showtime).where(
                Showtime.start_time >= start_time,
                Showtime.end_time <= end_time,
            )
            result = await session.scalars(stmt)
            return result.all()
