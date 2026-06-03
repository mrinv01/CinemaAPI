from typing import Optional

from app.schemas.common_schemas import ORMBaseModel, PositiveID


class BookedSeatBase(ORMBaseModel):
    showtime_id: PositiveID
    seat_id: PositiveID


class BookedSeatCreate(BookedSeatBase):
    pass


class BookedSeatUpdate(ORMBaseModel):
    showtime_id: Optional[PositiveID] = None
    seat_id: Optional[PositiveID] = None


class BookedSeatRead(BookedSeatBase):
    id: PositiveID
