from sqlalchemy.orm import relationship, Mapped, mapped_column
from app.database import Base, int_pk, created_at

class Hall(Base):
    id: Mapped[int_pk]
    name: Mapped[str] = mapped_column(nullable=False)
    hall_type: Mapped[str] = mapped_column(default="2D", nullable=False)
    created_at: Mapped[created_at]

    showtimes: Mapped[list["Showtime"]] = relationship(
        back_populates="hall",
        cascade="all, delete-orphan",
    )

    seats: Mapped[list["Seat"]] = relationship(
        back_populates="hall",
        cascade="all, delete-orphan",
    )
