from fastapi import APIRouter, Query, status

from app.exceptions.GeneralException import handle_service_error
from app.schemas.payment_schemas import PaymentCreate, PaymentRead, PaymentUpdate
from app.services.payments_service import PaymentService

router = APIRouter(prefix="/payments", tags=["Платежи"])


@router.get("/", summary="Получить все платежи", response_model=list[PaymentRead])
async def get_payments():
    return await PaymentService.get_all()


@router.get("/by-transaction", summary="Получить платеж по transaction_id", response_model=PaymentRead)
async def get_payment_by_transaction(transaction_id: str = Query(...)):
    try:
        return await PaymentService.get_by_transaction_id(transaction_id)
    except Exception as exc:
        raise handle_service_error(exc) from exc


@router.get("/by-external", summary="Получить платеж по external_payment_id", response_model=PaymentRead)
async def get_payment_by_external(external_payment_id: str = Query(...)):
    try:
        return await PaymentService.get_by_external_payment_id(external_payment_id)
    except Exception as exc:
        raise handle_service_error(exc) from exc


@router.get("/{payment_id}", summary="Получить платеж", response_model=PaymentRead)
async def get_payment(payment_id: int):
    try:
        return await PaymentService.get(payment_id)
    except Exception as exc:
        raise handle_service_error(exc) from exc


@router.post("/", summary="Создать платеж", response_model=PaymentRead, status_code=status.HTTP_201_CREATED)
async def create_payment(payment: PaymentCreate):
    try:
        return await PaymentService.create(payment)
    except Exception as exc:
        raise handle_service_error(exc) from exc


@router.put("/{payment_id}", summary="Обновить платеж", response_model=PaymentRead)
async def update_payment(payment_id: int, payment: PaymentUpdate):
    try:
        return await PaymentService.update(payment_id, payment)
    except Exception as exc:
        raise handle_service_error(exc) from exc


@router.delete("/{payment_id}", summary="Удалить платеж", status_code=status.HTTP_204_NO_CONTENT)
async def delete_payment(payment_id: int):
    try:
        await PaymentService.delete(payment_id)
    except Exception as exc:
        raise handle_service_error(exc) from exc