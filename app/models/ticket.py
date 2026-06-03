from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from app.database import Base, int_pk, created_at
from decimal import Decimal

class Ticket(Base):
    id: Mapped[int_pk]
    booking_id: Mapped[int] = mapped_column(ForeignKey("bookings.id"),nullable=False,)
    showtime_id: Mapped[int] = mapped_column(ForeignKey("showtimes.id"), nullable=False,)
    seat_id: Mapped[int] = mapped_column(ForeignKey("seats.id"), nullable=False,)
    price: Mapped[Decimal] = mapped_column(nullable=False,)
    ticket_status: Mapped[str] = mapped_column(nullable=False,)
    created_at: Mapped[created_at]

    booking: Mapped["Booking"] = relationship(
        back_populates="tickets",
    )
    showtime: Mapped["Showtime"] = relationship(
        back_populates="tickets",
    )
    seat: Mapped["Seat"] = relationship(
        back_populates="tickets",
    )
