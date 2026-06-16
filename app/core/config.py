from pydantic_settings import BaseSettings, SettingsConfigDict 
from pydantic import SecretStr
class Settings(BaseSettings):
    DB_USERNAME:str
    DB_PASSWORD:str
    DB_HOST:str
    DB_PORT:int
    DB_NAME:str
    SECRET_KEY : SecretStr
    algorithm : str = "HS256"
    access_token_expire_minutes : int = 5

    model_config = SettingsConfigDict(
        env_file=".env"
    )




settings = Settings()

p = Settings()

print(p.SECRET_KEY)