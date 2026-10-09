from typing import Typed_dict

class Session(Typed_dict):
    topic: str
    minutes: int


class Analytics(Typed_dict):
    total_minutes: int
    by_topic: dict[str, int]
