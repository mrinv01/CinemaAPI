from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from app.database import Base, int_pk, created_at
from decimal import Decimal

class Booking(Base):
    id: Mapped[int_pk]
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    total_amount: Mapped[Decimal] = mapped_column(nullable=False)
    created_at: Mapped[created_at]

    user: Mapped["User"] = relationship(back_populates="bookings")
    tickets: Mapped[list["Ticket"]] = relationship(
        back_populates="booking",
        cascade="all, delete-orphan",
    )
    payments: Mapped[list["Payment"]] = relationship(
        back_populates="booking",
        cascade="all, delete-orphan",
    )
