from fastapi import APIRouter, status

from app.schemas.booking_schemas import *
from app.services.booking_service import BookingService


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


