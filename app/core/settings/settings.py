import os

from pydantic_settings import BaseSettings
from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()

# app settings
PORT: str | None = os.environ.get("PORT")
HOST: str | None = os.environ.get("HOST")

# database settings
DB_PORT: str | None = os.environ.get("DB_PORT")
DB_HOST: str | None = os.environ.get("DB_HOST")
DB_USER: str | None = os.environ.get("DB_USER")
DB_PASSWORD: str | None = os.environ.get("DB_PASSWORD")
DB_NAME: str | None = os.environ.get("DB_NAME")

DB_URL: str = f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

# external api settings
API_KEY: str | None = os.environ.get("TECDOC_AUTH_KEY")
API_BASE_URL: str | None = os.environ.get("TECDOC_BASE_URL")


models: list[str] = [
    "app.models"
]


class AppSettings(BaseModel):
    port: int = int(PORT)
    host: str | None = HOST


class DatabaseSettings(BaseModel):
    port: int = int(DB_PORT)
    host: str = DB_HOST
    user: str = DB_USER
    password: str = DB_PASSWORD
    name: str = DB_NAME
    url: str = DB_URL
    models: list[str] = models


class ExternalAPISettings(BaseSettings):
    api_key: str = API_KEY
    base_url: str = API_BASE_URL


class Settings(BaseSettings):
    app: AppSettings = AppSettings()
    db: DatabaseSettings = DatabaseSettings()
    external_api: ExternalAPISettings = ExternalAPISettings()
