from typing import Protocol

from src.domain.types_module import WhiteListItem


class Whitelist(Protocol):
    def is_whitelisted(self, domain: str) -> bool:
        """Check if a domain is whitelisted."""
        pass

    def get_domains(self) -> list[WhiteListItem]:
        """Get the list of whitelisted domains."""
        pass
