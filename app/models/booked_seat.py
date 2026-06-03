from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from app.database import Base, int_pk


class booked_seat(Base):
    id: Mapped[int_pk]
    showtime_id: Mapped[int] = mapped_column(ForeignKey("showtimes.id"),nullable=False,)
    seat_id: Mapped[int] = mapped_column(ForeignKey("seats.id"), nullable=False,)

    showtime: Mapped["Showtime"] = relationship(
        back_populates="booked_seats",
    )
    seat: Mapped["Seat"] = relationship(
        back_populates="booked_seats",
    )