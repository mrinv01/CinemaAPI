from typing import Any

from passlib.context import CryptContext
from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import User
from app.repositories.base import BaseRepository
from app.schemas import UserCreate, UserUpdate

pwd_context = CryptContext(schemes=["pbkdf2_sha256"], deprecated="auto")


class UserRepository(BaseRepository[User, UserCreate, UserUpdate]):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(User, session)

    async def get_by_email(self, email: str) -> User | None:
        stmt = select(User).where(User.email == email)
        return await self.session.scalar(stmt)

    async def get_by_phone(self, phone: str) -> User | None:
        stmt = select(User).where(User.phone == phone)
        return await self.session.scalar(stmt)

    def _dump_create_data(self, data: UserCreate | dict[str, Any]) -> dict[str, Any]:
        create_data = data.model_dump() if isinstance(data, BaseModel) else dict(data)
        password = create_data.pop("password", None)
        if password is not None and "password_hash" not in create_data:
            create_data["password_hash"] = pwd_context.hash(password)
        return create_data
