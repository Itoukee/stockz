from domain.user.entity import User
from infra.user.repository import UserRepository
from pydantic import BaseModel


class CreateUserDto(BaseModel):
    name: str


class CreateUserUseCase:

    def __init__(self, repo: UserRepository):
        self.repo = repo

    def execute(self, name: str) -> User:
        user = User(user_id=None, name=name)
        return self.repo.create(user)
