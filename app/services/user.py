from typing import Any

from pydantic import BaseModel
from passlib.context import CryptContext

from app.repositories.user_repository import UserRepository
from app.services.exceptions import EntityAlreadyExistsError, EntityNotFoundError, EmptyUpdateError

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class UserService:
    repository = UserRepository
    entity_name = "Пользователь"

    @staticmethod
    def hash_password(password: str) -> str:
        return pwd_context.hash(password)

    @staticmethod
    def verify_password(password: str, password_hash: str) -> bool:
        return pwd_context.verify(password, password_hash)

    @classmethod
    async def get_by_email(cls, email: str):
        user = await cls.repository.get_by_email(email)
        if user is None:
            raise EntityNotFoundError(f"Пользователь с email={email} не найден.")
        return user

    @classmethod
    async def get_by_phone(cls, phone: str):
        user = await cls.repository.get_by_phone(phone)
        if user is None:
            raise EntityNotFoundError(f"Пользователь с phone={phone} не найден.")
        return user

    @classmethod
    async def create(cls, data: BaseModel | dict[str, Any]):
        values = cls._dump_schema(data)
        password = values.pop("password")

        if values.get("email") and await cls.repository.get_by_email(values["email"]):
            raise EntityAlreadyExistsError("Пользователь с таким email уже существует.")
        if await cls.repository.get_by_phone(values["phone"]):
            raise EntityAlreadyExistsError("Пользователь с таким телефоном уже существует.")

        values["password_hash"] = cls.hash_password(password)
        return await cls.repository.create(**values)

    @classmethod
    async def update(cls, entity_id: int, data: BaseModel | dict[str, Any]):
        values = cls._dump_schema(data, exclude_unset=True)
        if not values:
            raise EmptyUpdateError("Необходимо передать хотя бы одно поле для обновления.")

        if "password" in values:
            values["password_hash"] = cls.hash_password(values.pop("password"))

        if values.get("email"):
            existing = await cls.repository.get_by_email(values["email"])
            if existing is not None and existing.id != entity_id:
                raise EntityAlreadyExistsError("Пользователь с таким email уже существует.")

        if values.get("phone"):
            existing = await cls.repository.get_by_phone(values["phone"])
            if existing is not None and existing.id != entity_id:
                raise EntityAlreadyExistsError("Пользователь с таким телефоном уже существует.")

        _, rowcount = await cls.repository.update({"id": entity_id}, **values)
        if rowcount == 0:
            raise EntityNotFoundError(f"Пользователь с id={entity_id} не найден.")
        return await cls.get(entity_id)
