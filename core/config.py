from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

load_dotenv()




class Settings(BaseSettings):

    DB_USER: str = os.environ.get("DB_USER", "postgres")
    DB_PASSWORD: str=os.environ.get("DB_PASSWORD")
    DB_HOST: str = os.environ.get("DB_HOST", "localhost")
    DB_PORT: str = os.environ.get("DB_PORT", "5432")
    DB_NAME: str = os.environ.get("DB_NAME")
    DATABASE_URL: str = (
        f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )

    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    SECRET_KEY: str

    class Config:
        env_file = ".env"


settings = Settings()
