from ..http.client_interface import HttpClientProtocol
from ..models.download_info import DownloadInfo
from .protocol import DownloaderProtocol


class DirectDownloader(DownloaderProtocol):
    def __init__(self, client: HttpClientProtocol, url: str, filename: str):
        self.client = client
        self.url = url
        self.filename = filename

    async def get_download_info(self) -> DownloadInfo:
        return DownloadInfo(filename=self.filename, url=self.url)
