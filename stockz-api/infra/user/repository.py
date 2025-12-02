from sqlalchemy import Integer, String
from sqlalchemy.orm import mapped_column, Session
from passlib.hash import bcrypt

from infra.pgsql import Base, session as default_session
from domain.user.entity import User
from domain.user.repository import UserRepository


class UserModel(Base):
    __tablename__ = "users"

    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    email = mapped_column(String, nullable=False)
    password = mapped_column(String, nullable=False)


class PgsqlUserRepository(UserRepository):
    """_summary_

    Args:
        UserRepository (_type_): _description_
    """

    def __init__(self, session: Session = default_session) -> None:
        super().__init__()
        self.session = session

    def _to_domain(self, model: UserModel) -> User:
        return User(user_id=model.id, email=model.email, password=model.password)

    def _to_model(self, user: User) -> UserModel:
        return UserModel(email=user.email, password=user.password)

    def find_by_email(self, email: str) -> User | None:
        row = self.session.query(UserModel).filter_by(email=email).first()
        if row:
            return User(user_id=row.id, email=row.email, password=row.password)
        return None

    def save(self, user: User) -> User:
        user.password = bcrypt.hash(user.password)

        row = self._to_model(user)
        self.session.add(row)
        self.session.flush()
        user.id = row.id

        self.session.commit()
        return user
