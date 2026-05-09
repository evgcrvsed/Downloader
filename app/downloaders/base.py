import httpx


class BaseDownloader:
    def __init__(self, session: httpx.AsyncClient) -> None:
        self.session: httpx.AsyncClient = session
