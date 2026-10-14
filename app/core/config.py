from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Cutit Materiales y Formulas"
    environment: str = "local"
    debug: bool = False
    database_url: str = "sqlite:///./cutit.db"
    inventory_base_url: str = "http://localhost:8001"
    inventory_timeout_seconds: float = 5.0
    patents_base_url: str = "http://localhost:8002"
    patents_timeout_seconds: float = 5.0
    log_level: str = "INFO"
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
