from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    CONTACT: dict = {
        "name": "todo-nextjs-fastapi-app",
        "url": "https://todo-nextjs-fastapi-app.vercel.app/",
        "email": "shahzaibnoor40@gmail.com",
    }
    
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str
    
    ENV: str = "dev"

    if ENV == "dev":
        RELOAD: bool = True
        LOG_LEVEL: str = "debug"
    else:
        RELOAD: bool = False
        LOG_LEVEL: str = "info"

    ALLOWED_HOSTS: list = ["*"]
    
    class Config:
        env_file = "./.env"
        extra = "ignore"
        
settings = Settings()