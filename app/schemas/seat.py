from typing import Literal, Optional

from pydantic import Field

from app.schemas.common import ORMBaseModel, PositiveID, Timestamp

SeatType = Literal["STANDARD", "VIP", "COUPLE", "ACCESSIBLE"]


class SeatBase(ORMBaseModel):
    hall_id: PositiveID
    row_number: int = Field(gt=0)
    seat_number: int = Field(gt=0)
    seat_type: SeatType = "STANDARD"


class SeatCreate(SeatBase):
    pass


class SeatUpdate(ORMBaseModel):
    hall_id: Optional[PositiveID] = None
    row_number: Optional[int] = Field(default=None, gt=0)
    seat_number: Optional[int] = Field(default=None, gt=0)
    seat_type: Optional[SeatType] = None


class SeatRead(SeatBase):
    id: PositiveID
    created_at: Timestamp
