from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):

    model_config = SettingsConfigDict(case_sensitive=True)

    APP_NAME: str = "Connectivity Test Application"
    APP_HOST: str = "0.0.0.0"
    APP_PORT: int = 8000

    # Neo4j Configuration
    NEO4J_URL: str = "localhost"
    NEO4J_USERNAME: str = "neo4j"
    NEO4J_PASSWORD: str = "password"
    NEO4J_PORT: int = 7474

    # Qdrant Configuration
    QDRANT_URL: str = "localhost"
    QDRANT_PORT: int = 6333
    QDRANT_PASSWORD: str = "password"


settings = Settings()
