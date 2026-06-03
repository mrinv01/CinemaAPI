from datetime import datetime
from decimal import Decimal

from app.repositories.payment_repository import PaymentRepository
from app.services.base import BaseService
from app.services.exceptions import EntityNotFoundError


class PaymentService(BaseService[PaymentRepository]):
    repository = PaymentRepository
    entity_name = "Платеж"

    @classmethod
    async def get_by_transaction_id(cls, transaction_id: str):
        payments = await cls.repository.get_by_transaction_id(transaction_id)
        if not payments:
            raise EntityNotFoundError(f"Платеж с transaction_id={transaction_id} не найден.")
        return payments[0]

    @classmethod
    async def get_by_external_payment_id(cls, external_payment_id: str):
        payments = await cls.repository.get_by_external_payment_id(external_payment_id)
        if not payments:
            raise EntityNotFoundError(f"Платеж с external_payment_id={external_payment_id} не найден.")
        return payments[0]

    @classmethod
    async def mark_success(cls, payment_id: int, *, transaction_id: str | None = None):
        values = {"status": "SUCCESS", "paid_at": datetime.utcnow()}
        if transaction_id is not None:
            values["transaction_id"] = transaction_id
        return await cls.update(payment_id, values)

    @classmethod
    async def mark_failed(cls, payment_id: int, *, failure_reason: str | None = None):
        return await cls.update(
            payment_id,
            {"status": "FAILED", "failure_reason": failure_reason},
        )

    @classmethod
    async def mark_refunded(cls, payment_id: int):
        return await cls.update(
            payment_id,
            {"status": "REFUNDED", "refunded_at": datetime.utcnow()},
        )

    @classmethod
    async def create_for_booking(
        cls,
        *,
        booking_id: int,
        provider: str,
        amount: Decimal,
        currency: str = "RUB",
        external_payment_id: str | None = None,
    ):
        return await cls.repository.create(
            booking_id=booking_id,
            provider=provider,
            amount=amount,
            currency=currency,
            external_payment_id=external_payment_id,
            status="PENDING",
        )
