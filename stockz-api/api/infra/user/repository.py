from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base, Session
from infra.pgsql import session
from domain.user.entity import User
from ports.user_interface import UserRepository

Base = declarative_base()


class UserModel(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)


class PgsqlUserRepository(UserRepository):
    """_summary_

    Args:
        UserRepository (_type_): _description_
    """

    def find_by_id(self, user_id: int) -> User | None:
        user = session.get(UserModel, user_id)
        if not user:
            return None
        return User(user.id, user.name)

    def create(self, user: User) -> User:
        row = UserModel(name=user.name)

        session.add(row)
        session.flush()
        user.id = row.id

        return user
