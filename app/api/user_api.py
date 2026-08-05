from fastapi import APIRouter, Query, status

from app.exceptions.GeneralException import handle_service_error
from app.schemas.user_schemas import UserCreate, UserRead, UserUpdate
from app.services.user_service import UserService

router = APIRouter(prefix="/users", tags=["Пользователи"])


@router.get("/", summary="Получить всех пользователей", response_model=list[UserRead])
async def get_users():
    return await UserService.get_all()


@router.get("/by-email", summary="Получить пользователя по email", response_model=UserRead)
async def get_user_by_email(email: str = Query(...)):
    try:
        return await UserService.get_by_email(email)
    except Exception as exc:
        raise handle_service_error(exc) from exc


@router.get("/by-phone", summary="Получить пользователя по телефону", response_model=UserRead)
async def get_user_by_phone(phone: str = Query(...)):
    try:
        return await UserService.get_by_phone(phone)
    except Exception as exc:
        raise handle_service_error(exc) from exc


@router.get("/{user_id}", summary="Получить пользователя", response_model=UserRead)
async def get_user(user_id: int):
    try:
        return await UserService.get(user_id)
    except Exception as exc:
        raise handle_service_error(exc) from exc


@router.post("/", summary="Создать пользователя", response_model=UserRead, status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreate):
    try:
        return await UserService.create(user)
    except Exception as exc:
        raise handle_service_error(exc) from exc


@router.put("/{user_id}", summary="Обновить пользователя", response_model=UserRead)
async def update_user(user_id: int, user: UserUpdate):
    try:
        return await UserService.update(user_id, user)
    except Exception as exc:
        raise handle_service_error(exc) from exc


@router.delete("/{user_id}", summary="Удалить пользователя", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id: int):
    try:
        await UserService.delete(user_id)
    except Exception as exc:
        raise handle_service_error(exc) from exc