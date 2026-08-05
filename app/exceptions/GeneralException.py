from fastapi import HTTPException, status


class SeatOrShowtimeNotFound(HTTPException):
    def __init__(self, airport_id: int):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Место с id {airport_id} не найдено"
        )


class ServiceError(Exception):
    """Base exception for service-layer errors."""


class EntityNotFoundError(ServiceError):
    """Raised when an entity cannot be found by the requested identifier."""


class EntityAlreadyExistsError(ServiceError):
    """Raised when a unique business constraint is violated."""


class EmptyUpdateError(ServiceError):
    """Raised when an update request does not contain any fields to change."""

def handle_service_error(exc: Exception) -> HTTPException:
    if isinstance(exc, EntityNotFoundError):
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc))
    if isinstance(exc, (EntityAlreadyExistsError, EmptyUpdateError)):
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc))
    return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(exc))