from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DB_HOST: str = "localhost"
    DB_PORT: str = "3306"
    DB_USER: str = "root"
    DB_PASSWORD: str = "luckydeliv"
    DB_NAME: str = "kasi2"

    class Config:
        env_file = ".env"

settings = Settings()
