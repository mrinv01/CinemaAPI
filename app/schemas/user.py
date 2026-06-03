from datetime import date
from typing import Optional

from pydantic import EmailStr, Field

from app.schemas.common import ORMBaseModel, PositiveID, Timestamp


class UserBase(ORMBaseModel):
    email: Optional[EmailStr] = None
    phone: str = Field(min_length=5, max_length=32)
    first_name: str = Field(min_length=1, max_length=100)
    last_name: Optional[str] = Field(default=None, max_length=100)
    birth_date: Optional[date] = None
    role: str = "USER"


class UserCreate(UserBase):
    password: str = Field(min_length=8, max_length=128)


class UserUpdate(ORMBaseModel):
    email: Optional[EmailStr] = None
    phone: Optional[str] = Field(default=None, min_length=5, max_length=32)
    password: Optional[str] = Field(default=None, min_length=8, max_length=128)
    first_name: Optional[str] = Field(default=None, min_length=1, max_length=100)
    last_name: Optional[str] = Field(default=None, max_length=100)
    birth_date: Optional[date] = None
    role: Optional[str] = None


class UserRead(UserBase):
    id: PositiveID
    created_at: Timestamp
    updated_at: Timestamp


class UserInDB(UserRead):
    password_hash: str
