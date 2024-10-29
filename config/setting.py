from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DEBUG: bool = False
    VERSION: str = "0.1.0"
    PROJECT_NAME: str = "Job Board"


settings = Settings(_env_file=".env")
