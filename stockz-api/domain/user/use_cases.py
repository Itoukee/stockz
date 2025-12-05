from pydantic import BaseModel
from passlib.hash import bcrypt

from domain.user.entity import User
from infra.user.repository import UserRepository
from infra.jwt import create_access_token


class AuthRequestDto(BaseModel):
    email: str
    password: str


class CreateUserUseCase:

    def __init__(self, repo: UserRepository):
        self.repo = repo

    def execute(self, email: str, password: str):
        user = User(id=None, email=email, password=password)
        return self.repo.create(user)


class AccessOutput(BaseModel):
    access_token: str
    token_type: str
    id: int
    email: str


class LoginUserUseCase:

    def __init__(self, repo: UserRepository) -> None:
        self.repo = repo

    def execute(self, email: str, password: str) -> AccessOutput:
        user = self.repo.find_by_email(email)
        if not user or not bcrypt.verify(password, user.password):
            raise ValueError("Invalid credentials")
        token = create_access_token({"sub": str(user.id)})
        out = {
            "access_token": token,
            "token_type": "bearer",
            "id": user.id,
            "email": user.email,
        }

        return AccessOutput(**out)
