from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from app.database import Base, int_pk, created_at

class Seat(Base):
    id: Mapped[int_pk]
    hall_id: Mapped[int] = mapped_column(ForeignKey("halls.id"), nullable=False,)
    row_number: Mapped[int] = mapped_column(nullable=False,)
    seat_number: Mapped[int] = mapped_column(nullable=False,)
    seat_type: Mapped[str] = mapped_column(default="STANDARD", nullable=False,)
    created_at: Mapped[created_at]

    hall: Mapped["Hall"] = relationship(
        back_populates="seats",
    )
    tickets: Mapped[list["Ticket"]] = relationship(
        back_populates="seat",
        cascade="all, delete-orphan",
    )
    booked_seats: Mapped[list["booked_seat"]] = relationship(
        back_populates="seat",
        cascade="all, delete-orphan",
    )
