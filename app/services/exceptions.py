class ServiceError(Exception):
    """Base exception for service-layer errors."""


class EntityNotFoundError(ServiceError):
    """Raised when an entity cannot be found by the requested identifier."""


class EntityAlreadyExistsError(ServiceError):
    """Raised when a unique business constraint is violated."""


class EmptyUpdateError(ServiceError):
    """Raised when an update request does not contain any fields to change."""
