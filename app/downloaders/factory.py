import asyncio
from pathlib import Path
from tqdm import tqdm
from core.config import settings
from models.download_info import DownloadInfo
from downloaders.protocol import DownloaderProtocol


class DownloadService:
    """Оркестратор (высокий уровень — зависит только от абстракций)"""
    def __init__(self, downloader: DownloaderProtocol):
        self.downloader = downloader
        settings.DOWNLOAD_DIR.mkdir(parents=True, exist_ok=True)

    async def download(self):
        info: DownloadInfo = await self.downloader.get_download_info()
        filepath = settings.DOWNLOAD_DIR / info.filename

        print(f"📥 Скачиваем: {info.filename}")
        async with self.downloader.client.stream(info.url) as response:  # type: ignore
            total = int(response.headers.get("content-length", 0))
            with tqdm(total=total, unit="B", unit_scale=True) as progress:
                with open(filepath, "wb") as f:
                    async for chunk in response.aiter_bytes(8192):
                        f.write(chunk)
                        progress.update(len(chunk))

        print(f"✅ Готово: {filepath}")