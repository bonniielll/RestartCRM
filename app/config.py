import os
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    SECRET_KEY: str
    ALGORITHM: str

    if os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".env") is not None:
        model_config = SettingsConfigDict(
            env_file=os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".env")
        )
    else:
        model_config = SettingsConfigDict(env_file=os.environ)


settings = Settings()


def get_db_url():
    return (
        f"postgresql+asyncpg://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@"
        f"{settings.DB_HOST}:{settings.DB_PORT}/{settings.POSTGRES_DB}"
    )

def get_auth_data():
    return {"secret_key": settings.SECRET_KEY, "algorithm": settings.ALGORITHM}
