from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    DATABASE_URL: str
    AWS_SECRET_ACCESS_KEY: str | None = None
    AWS_ACCESS_KEY_ID: str | None = None
    AWS_SESSION_TOKEN: str | None = None
    AWS_REGION: str | None = None  # optional, can also default to us-east-1

    class Config:
        env_file = ".env"

settings = Settings()
