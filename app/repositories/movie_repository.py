from sqlalchemy import select, update as sqlalchemy_update
from sqlalchemy.exc import SQLAlchemyError

from app.models import Movie
from app.repositories.base_repository import BaseRepository
from app.database import async_session_maker


class MovieRepository(BaseRepository):
     model = Movie

     @classmethod
     async def update_movie(cls, movie_id: int, **update_fields):
         if not update_fields:
             return 0  # Нечего обновлять

         async with async_session_maker() as session:
             async with session.begin():
                 query = (
                     sqlalchemy_update(cls.model)
                     .where(cls.model.id == movie_id)
                     .values(**update_fields)
                     .execution_options(synchronize_session="fetch")
                 )
                 result = await session.execute(query)

                 try:
                     await session.commit()
                 except SQLAlchemyError as e:
                     await session.rollback()
                     raise e

                 return result.rowcount

     @classmethod
     async def get_by_kp_id(cls, kp_id: int):
         async with async_session_maker() as session:
             stmt = select(Movie).where(Movie.kp_id == kp_id)
             result = await session.execute(stmt)
             return result.scalar_one_or_none()