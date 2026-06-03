from sqlalchemy import ForeignKey, DateTime
from sqlalchemy.orm import relationship, Mapped, mapped_column
from app.database import Base, int_pk
from datetime import datetime
from decimal import Decimal

class Showtime(Base):
    id: Mapped[int_pk]
    movie_id: Mapped[int] = mapped_column(ForeignKey("movies.id"), nullable=False)
    hall_id: Mapped[int] = mapped_column(ForeignKey("halls.id"), nullable=False)
    start_time: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    end_time: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    format: Mapped[str] = mapped_column( default="2D", nullable=False)
    base_price: Mapped[Decimal] = mapped_column(nullable=False)
    status: Mapped[str] = mapped_column(nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)

    movie: Mapped["Movie"] = relationship(back_populates="showtimes")
    hall: Mapped["Hall"] = relationship(back_populates="showtimes")
    tickets: Mapped[list["Ticket"]] = relationship(
        back_populates="showtime",
        cascade="all, delete-orphan",
    )
    booked_seats: Mapped[list["booked_seat"]] = relationship(
        back_populates="showtime",
        cascade="all, delete-orphan",
    )
