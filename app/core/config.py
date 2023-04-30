import os

from dotenv import load_dotenv


load_dotenv()


class Settings:
    PROJECT_NAME: str = "dawits-buchi-app37"
    VERSION: str = "0.1.0"

    # Postgres Cloude SQL Connection Information
    POSTGRES_USER: str = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_SERVER: str = os.getenv("POSTGRES_SERVER")
    POSTGRES_PORT: str = os.getenv("POSTGRES_PORT", default="5432")
    POSTGRES_DB: str = os.getenv("POSTGRES_DB")
    DATABASE_URL = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}'


settings = Settings()
