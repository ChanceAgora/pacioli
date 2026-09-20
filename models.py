from typing import TypedDict

class Session(TypedDict):
    topic: str
    minutes: int


class Analytics(TypedDict):
    total_minutes: int
    by_topic: dict[str, int]
