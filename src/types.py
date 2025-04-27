from typing import TypedDict


class ModerationResponse(TypedDict):
    flagged: bool
    categories: list[str]
