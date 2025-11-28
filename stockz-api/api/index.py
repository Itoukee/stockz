import uvicorn

from fastapi import APIRouter

from domain.user.create_user import CreateUserDto, CreateUserUseCase
from infra.user.repository import PgsqlUserRepository
from settings import settings
from app import create_app


app = create_app()

app_base_configs = {
    "host": settings.host,
    "port": settings.ports,
    "workers": settings.workers,
    "access_log": True,
}

users_router = APIRouter()
user_repo = PgsqlUserRepository()


@users_router.post("/users/create")
def get_users(future_user: CreateUserDto):
    user = CreateUserUseCase(user_repo).execute(future_user.name)
    return user


if __name__ == "__main__":
    app.include_router(users_router)
    uvicorn.run("index:app", **app_base_configs)
