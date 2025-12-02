from sqlalchemy import create_engine
from sqlalchemy.orm import Session, declarative_base
from settings import settings

engine = create_engine(
    f"postgresql://{settings.db_user}:{settings.db_pwd}@pgsql:{settings.db_port}/{settings.db_name}",
    echo=True,
)
session = Session(engine)

Base = declarative_base()
