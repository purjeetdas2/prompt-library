from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    USE_SQLITE: bool = True
    SQLITE_DB_URL: str = "sqlite:///./test.db"
    POSTGRES_DB_URL: str = "postgresql://user:password@localhost/db"

    @property
    def database_url(self) -> str:
        return self.SQLITE_DB_URL if self.USE_SQLITE else self.POSTGRES_DB_URL
    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()