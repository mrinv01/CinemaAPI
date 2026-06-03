from datetime import datetime
from typing import Literal, Optional

from pydantic import Field

from app.schemas.common_schemas import Money, ORMBaseModel, PositiveID, Timestamp

PaymentStatus = Literal["PENDING", "SUCCESS", "FAILED", "REFUNDED"]
PaymentProvider = Literal["STRIPE", "PAYPAL", "APPLE_PAY", "GOOGLE_PAY"]


class PaymentBase(ORMBaseModel):
    booking_id: PositiveID
    provider: PaymentProvider
    status: PaymentStatus = "PENDING"
    amount: Money
    currency: str = Field(default="RUB", min_length=3, max_length=3)
    transaction_id: Optional[str] = Field(default=None, max_length=255)
    external_payment_id: Optional[str] = Field(default=None, max_length=255)
    failure_reason: Optional[str] = None
    paid_at: Optional[datetime] = None
    refunded_at: Optional[datetime] = None


class PaymentCreate(PaymentBase):
    pass


class PaymentUpdate(ORMBaseModel):
    booking_id: Optional[PositiveID] = None
    provider: Optional[PaymentProvider] = None
    status: Optional[PaymentStatus] = None
    amount: Optional[Money] = None
    currency: Optional[str] = Field(default=None, min_length=3, max_length=3)
    transaction_id: Optional[str] = Field(default=None, max_length=255)
    external_payment_id: Optional[str] = Field(default=None, max_length=255)
    failure_reason: Optional[str] = None
    paid_at: Optional[datetime] = None
    refunded_at: Optional[datetime] = None


class PaymentRead(PaymentBase):
    id: PositiveID
    created_at: Timestamp
    updated_at: Timestamp
