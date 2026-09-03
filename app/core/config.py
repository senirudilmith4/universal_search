from pydantic_settings import BaseSettings , SettingsConfigDict

# configuration settings for database URL and a match threshold for face embeddings
class Settings(BaseSettings):
    DATABASE_URL: str
    MATCH_THRESHOLD: float = 0.9   # The threshold for determining if two face embeddings match.

    # Configuration for loading environment variables from a .env file
    env_file = SettingsConfigDict(env_file=".env")  

settings = Settings() # instance of the Settings class to access configuration values