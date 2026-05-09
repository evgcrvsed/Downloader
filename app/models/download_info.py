from dataclasses import dataclass


@dataclass(frozen=True)
class DownloadInfo:
    filename: str
    url: str
    size: int | None = None