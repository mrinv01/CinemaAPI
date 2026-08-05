from datetime import datetime

from fastapi import APIRouter, Query, status

from app.exceptions.GeneralException import handle_service_error
from app.schemas.showtime_schemas import ShowtimeCreate, ShowtimeRead, ShowtimeUpdate
from app.services.showtime_service import ShowtimeService

router = APIRouter(prefix="/showtimes", tags=["Сеансы"])


@router.get("/", summary="Получить все сеансы", response_model=list[ShowtimeRead])
async def get_showtimes(
    movie_id: int | None = Query(default=None),
    hall_id: int | None = Query(default=None),
    start_time: datetime | None = Query(default=None),
    end_time: datetime | None = Query(default=None),
):
    if movie_id is not None:
        return await ShowtimeService.get_by_movie(movie_id)
    if hall_id is not None:
        return await ShowtimeService.get_by_hall(hall_id)
    if start_time is not None and end_time is not None:
        return await ShowtimeService.get_between(start_time, end_time)
    return await ShowtimeService.get_all()


@router.get("/{showtime_id}", summary="Получить сеанс", response_model=ShowtimeRead)
async def get_showtime(showtime_id: int):
    try:
        return await ShowtimeService.get(showtime_id)
    except Exception as exc:
        raise handle_service_error(exc) from exc


@router.post("/", summary="Создать сеанс", response_model=ShowtimeRead, status_code=status.HTTP_201_CREATED)
async def create_showtime(showtime: ShowtimeCreate):
    try:
        return await ShowtimeService.create(showtime)
    except Exception as exc:
        raise handle_service_error(exc) from exc


@router.put("/{showtime_id}", summary="Обновить сеанс", response_model=ShowtimeRead)
async def update_showtime(showtime_id: int, showtime: ShowtimeUpdate):
    try:
        return await ShowtimeService.update(showtime_id, showtime)
    except Exception as exc:
        raise handle_service_error(exc) from exc


@router.delete("/{showtime_id}", summary="Удалить сеанс", status_code=status.HTTP_204_NO_CONTENT)
async def delete_showtime(showtime_id: int):
    try:
        await ShowtimeService.delete(showtime_id)
    except Exception as exc:
        raise handle_service_error(exc) from exc