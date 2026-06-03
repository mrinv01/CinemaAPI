from datetime import datetime
from typing import Literal, Optional

from pydantic import Field, model_validator

from app.schemas.common import Money, ORMBaseModel, PositiveID, Timestamp

ShowtimeFormat = Literal["2D", "3D", "IMAX", "VIP"]
ShowtimeStatus = Literal["SCHEDULED", "CANCELLED", "COMPLETED"]


class ShowtimeBase(ORMBaseModel):
    movie_id: PositiveID
    hall_id: PositiveID
    start_time: datetime
    end_time: datetime
    format: ShowtimeFormat = "2D"
    base_price: Money
    status: ShowtimeStatus = "SCHEDULED"

    @model_validator(mode="after")
    def validate_time_interval(self) -> "ShowtimeBase":
        if self.end_time <= self.start_time:
            raise ValueError("end_time must be later than start_time")
        return self


class ShowtimeCreate(ShowtimeBase):
    pass


class ShowtimeUpdate(ORMBaseModel):
    movie_id: Optional[PositiveID] = None
    hall_id: Optional[PositiveID] = None
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None
    format: Optional[ShowtimeFormat] = None
    base_price: Optional[Money] = None
    status: Optional[ShowtimeStatus] = None

    @model_validator(mode="after")
    def validate_time_interval(self) -> "ShowtimeUpdate":
        if (
            self.start_time is not None
            and self.end_time is not None
            and self.end_time <= self.start_time
        ):
            raise ValueError("end_time must be later than start_time")
        return self


class ShowtimeRead(ShowtimeBase):
    id: PositiveID
    created_at: Timestamp
