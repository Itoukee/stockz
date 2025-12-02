from abc import ABC, abstractmethod
from typing import Optional

from domain.user.entity import User


class UserRepository(ABC):
    """_summary_
    Interface for the UserRepo
    Args:
        ABC (_type_): _description_
    """

    def __init__(self) -> None:
        pass

    @abstractmethod
    def find_by_email(self, email: str) -> Optional[User]:
        pass

    @abstractmethod
    def save(self, user: User) -> User:
        pass
