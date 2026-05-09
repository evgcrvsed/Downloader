from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    SESSION_HEADERS: dict = {
        "Accept": "application/vnd.github+json"
    }
    GITHUB_DOWNLOAD_LINKS: list[str] = [
        'https://api.github.com/repos/Klocman/Bulk-Crap-Uninstaller/releases/latest'
    ]

    DEBUG: bool = True


settings = Settings()
