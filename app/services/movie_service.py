from app.schemas.movie_schemas import *
from app.repositories.movie_repository import MovieRepository
from app.exceptions.MovieExceptions import MovieByKpIdNotFound, MovieByIdNotFound
from app.services.base_service import BaseService


class MovieService(BaseService):
    repository = MovieRepository
    entity_name="Фильм"

    @classmethod
    async def get_all_movies(cls):
        return await MovieRepository.get_all()

    @classmethod
    async def get_by_kp_id(cls, kp_id: int):
        movies = await MovieRepository.get_by_kp_id(kp_id)
        if not movies:
            raise MovieByKpIdNotFound(kp_id)
        return movies[0]



    @classmethod
    async def update_movie(cls, movie_id: int, update_data: MovieUpdate):
        update_dict = update_data.model_dump(exclude_none=True)
        updated_rows = await MovieRepository.update_movie(movie_id, **update_dict)
        if updated_rows == 0:
            raise MovieByIdNotFound(movie_id)
        return {"message": f"Фильм {movie_id} успешно обновлён"}

    @classmethod
    async def delete_by_kp_id(cls, kp_id: int):
        deleted = await MovieRepository.delete(id=kp_id)
        if deleted == 0:
            raise MovieByKpIdNotFound(kp_id)
        return {"message": f"Фильм с kp-id {kp_id} успешно удалён."}

