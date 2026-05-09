from typing import Protocol

class HttpClientProtocol(Protocol):
    """Маленький интерфейс (ISP + DIP)"""
    async def get(self, url: str, follow_redirects: bool = True) -> bytes:
        ...

    async def stream(self, url: str) -> "httpx.Response":  # type: ignore
        ...
    