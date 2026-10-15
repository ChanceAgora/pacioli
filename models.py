from typing import TypedDict

class Session(TypedDict):
    topic: str
    minutes: int

def create_session(topic: str, minutes: int) -> Session:
    if not isinstance(topic, str):
        raise TypeError("Topic must be a string")
    if not isinstance(minutes, int):
        raise TypeError("Minutes must be an integer")

    topic = topic.lower().strip()

    if not topic:
        raise ValueError("Topic cannot be empty")
    if minutes < 1:
        raise ValueError("Minutes must be greater than 0")

    return Session({"topic": topic, "minutes": minutes})


def validate_session(obj: dict) -> bool:
    if not set(obj) == {"topic", "minutes"}:
        return False

    if not isinstance(obj["topic"], str):
        return False

    if not isinstance(obj["minutes"], int):
        return False

    if (
            not obj["topic"].strip()
            or obj["minutes"] < 1
            ):
        return False

    return True


class Analytics(TypedDict):
    total_minutes: int
    by_topic: dict[str, int]
