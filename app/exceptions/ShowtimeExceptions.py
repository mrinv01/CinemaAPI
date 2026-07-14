from fastapi import HTTPException, status

class ShowtimeNotFound(HTTPException):
    def __init__(self, showtime_id: int):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Сеанс с id {showtime_id} не найден"
        )
