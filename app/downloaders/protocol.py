from typing import Protocol
from models.download_info import DownloadInfo


class DownloaderProtocol(Protocol):
    async def get_download_info(self) -> DownloadInfo:
        ...