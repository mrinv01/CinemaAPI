from fastapi import HTTPException, status


class MovieByKpIdNotFound(HTTPException):
    def __init__(self, id: int):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Фильм с kp-id {id} не найден"
        )


class MovieByIdNotFound(HTTPException):
    def __init__(self, id: int):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Фильм с id {id} не найден"
        )

