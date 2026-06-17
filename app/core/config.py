from pydantic_settings import BaseSettings, SettingsConfigDict 
from pydantic import SecretStr
class Settings(BaseSettings):
    SECRET_KEY : SecretStr
    DATABASE_URL:str
    algorithm : str = "HS256"
    access_token_expire_minutes : int = 5
    model_config = SettingsConfigDict(
        env_file=".env"
    )




settings = Settings()
