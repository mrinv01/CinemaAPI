from typing import Literal, Optional

from pydantic import Field

from app.schemas.common_schemas import ORMBaseModel, PositiveID, Timestamp

HallType = Literal["2D", "3D", "IMAX", "VIP"]


class HallBase(ORMBaseModel):
    name: str = Field(min_length=1, max_length=100)
    hall_type: HallType = "2D"


class HallCreate(HallBase):
    pass


class HallUpdate(ORMBaseModel):
    name: Optional[str] = Field(default=None, min_length=1, max_length=100)
    hall_type: Optional[HallType] = None


class HallRead(HallBase):
    id: PositiveID
    created_at: Timestamp
