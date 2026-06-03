from sqlalchemy import select
from app.models import Movie
from app.repositories.base_repository import BaseRepository
from app.database import async_session_maker


class MovieRepository(BaseRepository):
     model = Movie

     @classmethod
     async def get_by_kp_id(cls, kp_id: int):
         async with async_session_maker() as session:
             stmt = select(Movie).where(Movie.kp_id == kp_id)
             result = await session.execute(stmt)
             return result.scalars.all()
