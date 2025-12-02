from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    test_db_name: str = ""
    db_name: str = ""
    db_pwd: str = ""
    db_user: str = ""
    db_port: int = 5432

    host: str = "0.0.0.0"
    ports: int = 8080
    workers: int = 4

    log_level: str = "INFO"

    jwt_key: str = ""
    jwt_algo: str = "HS256"
    jwt_expire_min: int = 60

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )


settings = Settings()
