from fastapi import APIRouter, Depends, Path, Query, status

from app.schemas.booked_seat_schemas import *
from app.services.booked_seat_service import BookedSeatService


router = APIRouter(prefix="/booked", tags=["Забронированные места"])

@router.get(path="/showtime",
            summary="Получить забронированные места для сеанса",
            response_model=list[BookedSeatRead])
async def get_booked_by_showtime(showtime_id: int):
    return await BookedSeatService.get_by_showtime(showtime_id)

@router.post("/", summary="Забронировать место",
             response_model=BookedSeatRead,
             status_code=status.HTTP_201_CREATED)
async def create(seat: BookedSeatCreate):
    return await BookedSeatService.create(seat)


@router.delete("/", summary="Удалить место",)
async def delete(seat_id: int):
    return await BookedSeatService.delete(seat_id)