from domain.user.entity import User
from infra.user.repository import UserRepository


class CreateUserUseCase:

    def __init__(self, repo: UserRepository):
        self.repo = repo

    def execute(self, name: str) -> User:
        user = User(id=None, name=name)
        return self.repo.create(user)
