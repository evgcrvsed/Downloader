import asyncio
from downloaders.factory import DownloaderFactory
from services.download_service import DownloadService


async def main():
    programs = ["pycharm", "telegram", "7z"]

    for program in programs:
        downloader = DownloaderFactory.create(program)
        service = DownloadService(downloader)
        await service.download()


if __name__ == "__main__":
    asyncio.run(main())