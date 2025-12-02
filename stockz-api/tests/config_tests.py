import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from infra.pgsql import Base
from infra.user.repository import PgsqlUserRepository
from settings import settings

TEST_DB_URL = f"postgresql://postgres:{settings.db_user}@{settings.db_pwd}:5433/{settings.test_db_name}"


@pytest.fixture(scope="session")
def engine():
    engine = create_engine(TEST_DB_URL)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    return engine


@pytest.fixture(scope="function")
def db_session(engine):
    Session = sessionmaker(bind=engine)
    session = Session()

    yield session

    session.rollback()
    session.close()


@pytest.fixture
def user_repo(db_session):
    return PgsqlUserRepository(db_session)
