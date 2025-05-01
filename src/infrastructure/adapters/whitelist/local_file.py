import csv
from pathlib import Path

from src.domain.constants import CSV_SEPARATOR
from src.domain.types_module import WhiteListItem


class LocalFileWhitelist:
    def __init__(self, file_path: Path) -> None:
        self.file_path = file_path
        self._whitelist = self._load()

    def is_whitelisted(self, domain: str) -> bool:
        return any(domain in item.domain_url for item in self._whitelist)

    def get_domains(self) -> list[WhiteListItem]:
        return self._whitelist

    def _load(self) -> list[WhiteListItem]:
        with open(self.file_path, "r", encoding="utf-8") as f:
            reader = csv.reader(f, delimiter=CSV_SEPARATOR)
            return [
                WhiteListItem(*row) for index, row in enumerate(reader) if index > 0
            ]
