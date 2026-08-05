from fastapi import APIRouter, Query, status

from app.exceptions.GeneralException import handle_service_error
from app.schemas.ticket_schemas import TicketCreate, TicketRead, TicketUpdate
from app.services.ticket_service import TicketService

router = APIRouter(prefix="/tickets", tags=["Билеты"])


@router.get("/", summary="Получить все билеты", response_model=list[TicketRead])
async def get_tickets(
    booking_id: int | None = Query(default=None),
    showtime_id: int | None = Query(default=None),
):
    if booking_id is not None:
        return await TicketService.get_by_booking(booking_id)
    if showtime_id is not None:
        return await TicketService.get_by_showtime(showtime_id)
    return await TicketService.get_all()


@router.get("/{ticket_id}", summary="Получить билет", response_model=TicketRead)
async def get_ticket(ticket_id: int):
    try:
        return await TicketService.get(ticket_id)
    except Exception as exc:
        raise handle_service_error(exc) from exc


@router.post("/", summary="Создать билет", response_model=TicketRead, status_code=status.HTTP_201_CREATED)
async def create_ticket(ticket: TicketCreate):
    try:
        return await TicketService.create(ticket)
    except Exception as exc:
        raise handle_service_error(exc) from exc


@router.put("/{ticket_id}", summary="Обновить билет", response_model=TicketRead)
async def update_ticket(ticket_id: int, ticket: TicketUpdate):
    try:
        return await TicketService.update(ticket_id, ticket)
    except Exception as exc:
        raise handle_service_error(exc) from exc


@router.delete("/{ticket_id}", summary="Удалить билет", status_code=status.HTTP_204_NO_CONTENT)
async def delete_ticket(ticket_id: int):
    try:
        await TicketService.delete(ticket_id)
    except Exception as exc:
        raise handle_service_error(exc) from exc