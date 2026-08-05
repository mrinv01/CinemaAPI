from fastapi import APIRouter, status

from app.schemas.movie_schemas import *
from app.services.movie_service import MovieService

router = APIRouter(prefix="/movie", tags=["Каталог фильмов"])

@router.get(path="/", summary="Получить весь список фильмов", response_model= list[MovieRead])
async def get_movies():
    return await MovieService.get_all_movies()

@router.get(path="/{kp_id}", summary="Получить фильм по kp-id кинопоиска", response_model=MovieRead)
async def get_movie(kp_id: int):
    return await MovieService.get_by_kp_id(kp_id)

@router.post(path="/", summary="Добавить фильм в библиотеку",
             response_model=MovieRead,
             status_code=status.HTTP_201_CREATED)
async def create_movie(movie: MovieCreate):
    return await MovieService.create(movie)

@router.put(path="/{movie_id}", summary="Обновление информации о фильме")
async def update_movie(movie_id: int, update_data: MovieUpdate):
    return await MovieService.update_movie(movie_id, update_data)


@router.delete(path="/{kp_id}", summary="Удалить фильм из каталога по kp-id",)
async def delete(kp_id: int):
    return await MovieService.delete_by_kp_id(kp_id)




