from fastapi import APIRouter, status

from app.schemas.booking_schemas import *
from app.services.booking_service import BookingService
from app.exceptions.GeneralException import handle_service_error


router = APIRouter(prefix="/bookings", tags=["Бронирования"])

@router.get(path="/", summary="Получить все бронирования", response_model=list[BookingRead])
async def get_booking_list():
    return await BookingService.get_all_bookings()

@router.get(path="/user", summary="Получить бронирования пользователя", response_model=list[BookingRead])
async def get_booking(user_id: int):
    return await BookingService.get_bookings_by_user(user_id)

@router.get(path="/booking", summary="Получить данные бронирования", response_model=BookingRead)
async def get_booking(booking_id: int):
    return await BookingService.get_booking_by_id(booking_id)

@router.post(path="/", summary="Создать бронирование", response_model=BookingRead, status_code=status.HTTP_201_CREATED)
async def create_booking(booking: BookingCreate):
    try:
        return await BookingService.create(booking)
    except Exception as exc:
        raise handle_service_error(exc) from exc


@router.put(path="/{booking_id}", summary="Обновить бронирование", response_model=BookingRead)
async def update_booking(booking_id: int, booking: BookingUpdate):
    try:
        return await BookingService.update(booking_id, booking)
    except Exception as exc:
        raise handle_service_error(exc) from exc


@router.delete(path="/{booking_id}", summary="Удалить бронирование", status_code=status.HTTP_204_NO_CONTENT)
async def delete_booking(booking_id: int):
    try:
        await BookingService.delete(booking_id)
    except Exception as exc:
        raise handle_service_error(exc) from exc

