import httpx


class HttpxClient:
    def __init__(self, headers: dict) -> None:
        self.headers = headers
        self.session = httpx.AsyncClient(headers=headers)
