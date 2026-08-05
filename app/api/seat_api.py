from fastapi import APIRouter, Query, status

from app.exceptions.GeneralException import handle_service_error
from app.schemas.seat_schemas import SeatCreate, SeatRead, SeatUpdate
from app.services.seat_service import SeatService

router = APIRouter(prefix="/seats", tags=["Места"])


@router.get("/", summary="Получить все места", response_model=list[SeatRead])
async def get_seats(hall_id: int | None = Query(default=None)):
    if hall_id is not None:
        return await SeatService.get(hall_id)
    return await SeatService.get_all()


@router.get("/{seat_id}", summary="Получить место", response_model=SeatRead)
async def get_seat(seat_id: int):
    try:
        return await SeatService.get(seat_id)
    except Exception as exc:
        raise handle_service_error(exc) from exc


@router.post("/", summary="Создать место", response_model=SeatRead, status_code=status.HTTP_201_CREATED)
async def create_seat(seat: SeatCreate):
    try:
        return await SeatService.create(seat)
    except Exception as exc:
        raise handle_service_error(exc) from exc


@router.put("/{seat_id}", summary="Обновить место", response_model=SeatRead)
async def update_seat(seat_id: int, seat: SeatUpdate):
    try:
        return await SeatService.update(seat_id, seat)
    except Exception as exc:
        raise handle_service_error(exc) from exc


@router.delete("/{seat_id}", summary="Удалить место", status_code=status.HTTP_204_NO_CONTENT)
async def delete_seat(seat_id: int):
    try:
        await SeatService.delete(seat_id)
    except Exception as exc:
        raise handle_service_error(exc) from exc