from fastapi import FastAPI, APIRouter
from app.storage import object_storage

from app.api.storage_api import router as storage_router
from app.api.booked_seat_api import router as booked_seat_router
from app.api.movie_api import router as movie_router
from app.api.booking_api import router as booking_router
from app.api.hall_api import router as hall_router
from app.api.payment_api import router as payment_router
from app.api.seat_api import router as seat_router
from app.api.showtime_api import router as showtime_router
from app.api.ticket_api import router as ticket_router
from app.api.user_api import router as user_router

def register_routes(app: FastAPI) -> None:
    root_router = APIRouter()
    @root_router.get("/")
    def home_page():
        return {
            "message": "Добро пожаловать!"
        }

    app.include_router(root_router, tags=["Приветствие"])
    app.include_router(storage_router)
    app.include_router(booked_seat_router)
    app.include_router(movie_router)
    app.include_router(booking_router)
    app.include_router(hall_router)
    app.include_router(payment_router)
    app.include_router(seat_router)
    app.include_router(showtime_router)
    app.include_router(ticket_router)
    app.include_router(user_router)

def create_app() -> FastAPI:
    app = FastAPI(
        title="Кинотеатр",
        description="API для управления кинотеатром.",
        version="1.0.0",
    )

    register_routes(app)

    # @app.on_event("startup")
    # async def startup_event() -> None:
    #    try:
    #        await object_storage.ensure_bucket()
    #    except:
    #       print("Ошибка подключения к хранилищю S3")

    return app

app = create_app()
