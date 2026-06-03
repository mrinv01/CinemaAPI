from sqlalchemy import select
from app.models import Payment
from app.repositories.base import BaseRepository
from app.database import async_session_maker


class PaymentRepository(BaseRepository):
    model = Payment

    @classmethod
    async def get_by_transaction_id(cls, transaction_id: str):
        async with async_session_maker() as session:
            stmt = select(Payment).where(Payment.transaction_id == transaction_id)
            result = await session.execute(stmt)
            return result.scalars().all()

    @classmethod
    async def get_by_external_payment_id(cls, external_payment_id: str):
        async with async_session_maker() as session:
            stmt = select(Payment).where(Payment.external_payment_id == external_payment_id)
            result = await session.execute(stmt)
            return result.scalars().all()
