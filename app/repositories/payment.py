from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Payment
from app.repositories.base import BaseRepository
from app.schemas import PaymentCreate, PaymentUpdate


class PaymentRepository(BaseRepository[Payment, PaymentCreate, PaymentUpdate]):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(Payment, session)

    async def get_by_transaction_id(self, transaction_id: str) -> Payment | None:
        stmt = select(Payment).where(Payment.transaction_id == transaction_id)
        return await self.session.scalar(stmt)

    async def get_by_external_payment_id(self, external_payment_id: str) -> Payment | None:
        stmt = select(Payment).where(Payment.external_payment_id == external_payment_id)
        return await self.session.scalar(stmt)
