from sqlalchemy import select
from app.models import User
from app.repositories.base_repository import BaseRepository
from app.database import async_session_maker


class UserRepository(BaseRepository):
    model = User

    @classmethod
    async def get_by_email(cls, email: str):
        async with async_session_maker() as session:
            stmt = select(User).where(User.email == email)
            result = await session.scalar(stmt)
            return result

    @classmethod
    async def get_by_phone(cls, phone: str):
        async with async_session_maker() as session:
            stmt = select(User).where(User.phone == phone)
            result = await session.scalar(stmt)
            return result
