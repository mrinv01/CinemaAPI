from fastapi import HTTPException, status


class SeatOrShowtimeNotFound(HTTPException):
    def __init__(self, airport_id: int):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Место с id {airport_id} не найдено"
        )
