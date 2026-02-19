from pydantic_settings import BaseSettings

class Config(BaseSettings):
    api_host: str | None = None
    db_type: str | None = None
    db_host: str | None = 'localhost'
    db_port: int | None = 5432

    postgres_user: str | None = None
    postgres_pass: str | None = None
    postgres_db: str | None = None

    debug: bool = False

    class Config:
        env_file = '.env'

settings = Config()