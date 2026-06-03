from fastapi import FastAPI, APIRouter


def register_routes(app: FastAPI) -> None:
    root_router = APIRouter()
    @root_router.get("/")
    def home_page():
        return {
            "message": "Добро пожаловать!"
        }

    app.include_router(root_router, tags=["Приветствие"])

def create_app() -> FastAPI:
    app = FastAPI(
        title="Кинотеатр",
        description="API для управления кинотеатром.",
        version="1.0.0",
    )

    register_routes(app)
    return app

app = create_app()
