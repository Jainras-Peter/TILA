from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    environment: str = Field(default="development", alias="ENVIRONMENT")
    port: int = Field(default=8000, alias="PORT")

    mongodb_uri: str = Field(
        default="mongodb://localhost:27017",
        alias="MONGODB_URI",
    )
    mongodb_db_name: str = Field(default="tila", alias="MONGODB_DB_NAME")

    auth_secret: str = Field(
        default="change-me-in-production-tila-auth-secret",
        alias="AUTH_SECRET",
    )
    auth_cookie_max_age: int = Field(default=60 * 60 * 24 * 7, alias="AUTH_COOKIE_MAX_AGE")
    auth_cookie_name: str = Field(default="tilaauth", alias="AUTH_COOKIE_NAME")
    csrf_cookie_name: str = Field(default="csrftoken", alias="CSRF_COOKIE_NAME")
    csrf_header_name: str = Field(default="x-csrftoken", alias="CSRF_HEADER_NAME")

    cors_origins: str = Field(
        default="http://localhost:4200",
        alias="CORS_ORIGINS",
    )

    @property
    def is_production(self) -> bool:
        return self.environment.lower() == "production"

    @property
    def cors_origin_list(self) -> list[str]:
        return [origin.strip() for origin in self.cors_origins.split(",") if origin.strip()]


@lru_cache
def get_settings() -> Settings:
    return Settings()
