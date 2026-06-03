from datetime import datetime
from enum import Enum
from sqlalchemy import DateTime, ForeignKey, Numeric, Enum as SqlEnum, Text
from app.database import Base, int_pk, created_at, updated_at
from sqlalchemy.orm import relationship, Mapped, mapped_column


class PaymentStatus(str, Enum):
    PENDING = "PENDING"
    SUCCESS = "SUCCESS"
    FAILED = "FAILED"
    REFUNDED = "REFUNDED"


class PaymentProvider(str, Enum):
    STRIPE = "STRIPE"
    PAYPAL = "PAYPAL"
    APPLE_PAY = "APPLE_PAY"
    GOOGLE_PAY = "GOOGLE_PAY"


class Payment(Base):
    id: Mapped[int_pk]

    booking_id: Mapped[int] = mapped_column(
        ForeignKey("bookings.id", ondelete="CASCADE"),
        nullable=False,
        index=True
    )
    provider: Mapped[str] = mapped_column(SqlEnum(PaymentProvider), nullable=False)

    status: Mapped[str] = mapped_column(
        SqlEnum(PaymentStatus),
        nullable=False,
        default=PaymentStatus.PENDING,
        index=True
    )
    amount = mapped_column(Numeric(10, 2),nullable=False)
    currency: Mapped[str] = mapped_column(nullable=False, default="RUB")
    transaction_id: Mapped[str] = mapped_column(unique=True, nullable=True)
    external_payment_id: Mapped[str] = mapped_column(unique=True, nullable=True)
    failure_reason: Mapped[str] = mapped_column(nullable=True)
    paid_at: Mapped[datetime] = mapped_column(nullable=True)
    refunded_at: Mapped[datetime] = mapped_column(nullable=True)
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]

    booking = relationship("Booking", back_populates="payments")