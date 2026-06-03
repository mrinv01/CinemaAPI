from typing import Literal, Optional

from app.schemas.common_schemas import Money, ORMBaseModel, PositiveID, Timestamp

TicketStatus = Literal["BOOKED", "PAID", "CANCELLED", "USED", "REFUNDED"]


class TicketBase(ORMBaseModel):
    booking_id: PositiveID
    showtime_id: PositiveID
    seat_id: PositiveID
    price: Money
    ticket_status: TicketStatus = "BOOKED"


class TicketCreate(TicketBase):
    pass


class TicketUpdate(ORMBaseModel):
    booking_id: Optional[PositiveID] = None
    showtime_id: Optional[PositiveID] = None
    seat_id: Optional[PositiveID] = None
    price: Optional[Money] = None
    ticket_status: Optional[TicketStatus] = None


class TicketRead(TicketBase):
    id: PositiveID
    created_at: Timestamp
