from typing import Optional

from app.schemas.common_schemas import Money, ORMBaseModel, PositiveID, Timestamp


class BookingBase(ORMBaseModel):
    user_id: PositiveID
    total_amount: Money


class BookingCreate(BookingBase):
    pass


class BookingUpdate(ORMBaseModel):
    user_id: Optional[PositiveID] = None
    total_amount: Optional[Money] = None


class BookingRead(BookingBase):
    id: PositiveID
    created_at: Timestamp
