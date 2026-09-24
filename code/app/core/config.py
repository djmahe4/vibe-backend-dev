from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Vibe Backend Workshop API"
    environment: str = "dev"
    docs_enabled: bool = False
    jwt_secret: str = Field(default="change-me-in-prod", min_length=16)
    jwt_algorithm: str = "HS256"
    access_token_exp_minutes: int = 30
    cors_allowed_origins: list[str] = ["http://localhost:3000", "http://127.0.0.1:3000"]
    rate_limit_per_minute: int = 60

    model_config = SettingsConfigDict(env_file=".env", env_prefix="VIBE_")


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    return Settings()
