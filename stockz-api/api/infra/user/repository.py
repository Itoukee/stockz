from sqlalchemy import Integer, String
from sqlalchemy.orm import mapped_column, declarative_base

from infra.pgsql import session, Base
from domain.user.entity import User
from ports.user_interface import UserRepository


class UserModel(Base):
    __tablename__ = "users"

    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    name = mapped_column(String)


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

        session.commit()
        return user
