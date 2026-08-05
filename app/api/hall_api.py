from fastapi import APIRouter, status

from app.exceptions.GeneralException import handle_service_error
from app.schemas.hall_schemas import HallCreate, HallRead, HallUpdate
from app.services.hall_service import HallService

router = APIRouter(prefix="/halls", tags=["Залы"])


@router.get("/", summary="Получить все залы", response_model=list[HallRead])
async def get_halls():
    return await HallService.get_all()


@router.get("/{hall_id}", summary="Получить зал", response_model=HallRead)
async def get_hall(hall_id: int):
    try:
        return await HallService.get(hall_id)
    except Exception as exc:
        raise handle_service_error(exc) from exc


@router.post("/", summary="Создать зал", response_model=HallRead, status_code=status.HTTP_201_CREATED)
async def create_hall(hall: HallCreate):
    try:
        return await HallService.create(hall)
    except Exception as exc:
        raise handle_service_error(exc) from exc


@router.put("/{hall_id}", summary="Обновить зал", response_model=HallRead)
async def update_hall(hall_id: int, hall: HallUpdate):
    try:
        return await HallService.update(hall_id, hall)
    except Exception as exc:
        raise handle_service_error(exc) from exc


@router.delete("/{hall_id}", summary="Удалить зал", status_code=status.HTTP_204_NO_CONTENT)
async def delete_hall(hall_id: int):
    try:
        await HallService.delete(hall_id)
    except Exception as exc:
        raise handle_service_error(exc) from exc