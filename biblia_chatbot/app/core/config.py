from pathlib import Path
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    openai_api_key: str = Field(..., min_length=1)

    openai_model: str = Field(default="gpt-5", min_length=1)

    bible_data_path: Path = Path(__file__).resolve().parents[1] / "data" / "nvi.json"

    model_config = SettingsConfigDict(
        env_file=Path(__file__).resolve().parents[2] / ".env",
        extra="ignore",
        case_sensitive=False,
    )


settings = Settings()