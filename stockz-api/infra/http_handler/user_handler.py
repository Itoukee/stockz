from fastapi import APIRouter, HTTPException, Depends

from infra.user.repository import PgsqlUserRepository
from infra.jwt import require_user
from application.user.cases.auth_user import (
    AuthRequestDto,
    CreateUserUseCase,
    LoginUserUseCase,
)

user_repo = PgsqlUserRepository()
users_router = APIRouter()


@users_router.post("/user/register")
def register(future_user: AuthRequestDto):
    try:
        user = CreateUserUseCase(user_repo).execute(
            future_user.email, future_user.password
        )
        return {"id": user.id, "email": user.email}
    except ValueError as v_err:
        raise HTTPException(
            status_code=400, detail="The user could not be created"
        ) from v_err


@users_router.post("/user/login")
def login(user: AuthRequestDto):
    try:
        access = LoginUserUseCase(user_repo).execute(user.email, user.password)
        return access

    except ValueError as v_err:
        raise HTTPException(status_code=401, detail="Unauthorized") from v_err


@users_router.get("/user/me")
def me(user=Depends(require_user)):
    return {"user_id": user["sub"]}
