from sqlalchemy import create_engine, Session
from settings import settings

engine = create_engine(
    (
        f"postgresql+psycopg2://{settings.db_user}:{settings.db_pwd}",
        f"@pgsql:{settings.db_port}/{settings.db_name}",
    ),
    echo=True,
)
session = Session(engine)
