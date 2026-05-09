import httpx

from core.config import settings

from .base import BaseDownloader

class GithubDownloader(BaseDownloader):
    async def ping(self, url: str) -> bool:
        async with self.session as client:
            response = httpx.get(url, headers=settings.SESSION_HEADERS, follow_redirects=True)
            response.raise_for_status()
            return response.json()