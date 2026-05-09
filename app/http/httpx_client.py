import httpx
from .client_interface import HttpClientProtocol
from core.config import settings

class HttpxClient(HttpClientProtocol):
    """Конкретная реализация (SRP)"""
    def __init__(self):
        self._client = httpx.AsyncClient(
            headers=settings.SESSION_HEADERS,
            follow_redirects=True,
            timeout=30.0,
        )

    async def get(self, url: str, follow_redirects: bool = True) -> bytes:
        async with self._client as client:
            resp = await client.get(url)
            resp.raise_for_status()
            return resp.content

    async def stream(self, url: str) -> "httpx.Response":
        async with self._client as client:
            return await client.get(url, stream=True)