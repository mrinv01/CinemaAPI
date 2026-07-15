from fastapi import HTTPException, status


class BookingNotFound(HTTPException):
    def __init__(self, id: int):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Бронирование с id {id} не найдено"
        )

class BookingForUserNotFound(HTTPException):
    def __init__(self, id: int):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Бронирований у пользователя {id} не найдено"
        )