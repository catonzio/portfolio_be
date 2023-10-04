import os
from dotenv import load_dotenv

from pathlib import Path

from fastapi_mail import ConnectionConfig

env_path = Path("..") / ".env"
load_dotenv(dotenv_path=env_path)


class Settings:
    PROJECT_NAME: str = "portfolio"
    PROJECT_VERSION: str = "1.0.0"

    POSTGRES_USER: str = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_SERVER: str = os.getenv("POSTGRES_SERVER", "localhost")
    POSTGRES_PORT: str = os.getenv(
        "POSTGRES_PORT", 5432
    )  # default postgres port is 5432
    POSTGRES_DB: str = os.getenv("POSTGRES_DB")
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"

    conf: ConnectionConfig = ConnectionConfig(
        MAIL_USERNAME=os.getenv("MAIL_USERNAME"),
        MAIL_PASSWORD=os.getenv("MAIL_PASSWORD"),
        MAIL_FROM=os.getenv("MAIL_FROM"),
        MAIL_PORT=os.getenv("MAIL_PORT"),
        MAIL_SERVER=os.getenv("MAIL_SERVER"),
        # MAIL_FROM_NAME="Danilo Catone",
        MAIL_SSL_TLS=True,
        MAIL_STARTTLS=False,
        TEMPLATE_FOLDER=os.getenv("TEMPLATE_FOLDER"),
        # USE_CREDENTIALS=True,
        # VALIDATE_CERTS=True,
        # TEMPLATE_FOLDER="./../templates",
    )


settings = Settings()

if __name__ == "__main__":
    print(settings.DATABASE_URL)
