import httpx
from pathlib import Path

from core.config import settings

from httpx_client import HttpxClient
from downloaders.github_downloader import GithubDownloader

session = HttpxClient(settings.SESSION_HEADERS)

github = GithubDownloader(session)


def get_latest_release_download(owner: str, repo: str, asset_pattern: str = None):
    url = f"https://api.github.com/repos/{owner}/{repo}/releases/latest"

    headers = {
        "Accept": "application/vnd.github+json"
    }

    response = httpx.get(url, headers=headers, follow_redirects=True)
    response.raise_for_status()
    data = response.json()

    # data["tag_name"] — версия (например v6.1)
    # data["assets"] — список файлов

    for asset in data["assets"]:
        name = asset["name"]
        download_url = asset["browser_download_url"]

        if asset_pattern is None or asset_pattern.lower() in name.lower():
            return {
                "version": data["tag_name"],
                "name": name,
                "download_url": download_url,
                "size": asset["size"],
                "created_at": data["created_at"]
            }

    raise ValueError(f"Не найдено ассетов с паттерном '{asset_pattern}'")


# Пример использования для твоего Bulk Crap Uninstaller
if __name__ == "__main__":
    info = get_latest_release_download(
        owner="Klocman",
        repo="Bulk-Crap-Uninstaller",
        # asset_pattern="portable"  # или "setup" для установщика
    )
    print(info)

    # Скачиваем
    r = httpx.get(info["download_url"], follow_redirects=True)
    Path(info["name"]).write_bytes(r.content)
    print(f"Скачано: {info['name']}")