from fastapi import FastAPI, APIRouter
from app.api.storage_api import router as storage_router
from app.storage import object_storage


def register_routes(app: FastAPI) -> None:
    root_router = APIRouter()
    @root_router.get("/")
    def home_page():
        return {
            "message": "Добро пожаловать!"
        }

    app.include_router(root_router, tags=["Приветствие"])
    app.include_router(storage_router)

def create_app() -> FastAPI:
    app = FastAPI(
        title="Кинотеатр",
        description="API для управления кинотеатром.",
        version="1.0.0",
    )

    register_routes(app)

    @app.on_event("startup")
    async def startup_event() -> None:
        await object_storage.ensure_bucket()
    return app

app = create_app()
