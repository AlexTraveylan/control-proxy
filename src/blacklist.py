from src.constants import BLACKLIST_FILE


class BlackList:
    _blacklist: list[str] = []

    def __init__(self) -> None:
        self._load()

    def is_blocked(self, host: str) -> bool:
        print(f"Checking if {host} is blocked")
        return any(banned in host for banned in self._blacklist)

    def add_url(self, url: str) -> None:
        with open(BLACKLIST_FILE, "a", encoding="utf-8") as f:
            f.write(url + "\n")
        self._load()

    def _load(self) -> None:
        with open(BLACKLIST_FILE, "r", encoding="utf-8") as f:
            self._blacklist = f.read().splitlines()
        print(f"Loaded {len(self._blacklist)} blocked hosts")
