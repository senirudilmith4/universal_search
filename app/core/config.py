from pydantic_settings import BaseSettings

# configuration settings for database URL and a match threshold for face embeddings
class Settings(BaseSettings):
    DATABASE_URL: str
    MATCH_THRESHOLD: float = 0.9   # The threshold for determining if two face embeddings match.

    class Config:
        env_file = ".env"  # specifies the environment file to load configuration values from 

settings = Settings() # instance of the Settings class to access configuration values