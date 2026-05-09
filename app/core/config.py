from pydantic_settings import BaseSettings
from pathlib import Path

class Settings(BaseSettings):
    DOWNLOAD_DIR: Path = Path(__file__).parent / "Autodownloader"
    DOWNLOAD_DIR.mkdir(parents=True, exist_ok=True)

    SESSION_HEADERS: dict = {
        "Accept": "application/vnd.github+json"
    }
    GITHUB_DOWNLOAD_LINKS: list[str] = [
        'https://api.github.com/repos/Klocman/Bulk-Crap-Uninstaller/releases/latest'
    ]

    DEBUG: bool = True


settings = Settings()
