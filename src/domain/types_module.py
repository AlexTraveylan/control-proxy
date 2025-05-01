from typing import NamedTuple


class WhiteListItem(NamedTuple):
    domain_display_name: str
    domain_url: str
    who_authorizes: str
