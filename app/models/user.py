from sqlalchemy.orm import relationship, Mapped, mapped_column
from app.database import Base, int_pk, created_at, updated_at
from datetime import date

class User(Base):
    id: Mapped[int_pk]
    email: Mapped[str | None] = mapped_column(unique=True,nullable=True,)
    phone: Mapped[str] = mapped_column(unique=True, nullable=False,)
    password_hash: Mapped[str] = mapped_column(nullable=False,)
    first_name: Mapped[str] = mapped_column(nullable=False,)
    last_name: Mapped[str | None] = mapped_column(nullable=True,)
    birth_date: Mapped[date | None] = mapped_column( nullable=True,)
    role: Mapped[str] = mapped_column(default=".USER", nullable=False,)
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]

    bookings: Mapped[list["Booking"]] = relationship(
        back_populates="user",
        cascade="all, delete-orphan",
    )