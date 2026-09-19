import useData
from copy import deepcopy

empty_result = useData.getSummary([])

assert empty_result == {
        "total_minutes": 0,
        "by_topic": {},
        }, (
                f"Unexpected result for empty input in getSummary: {empty_result}"
                )

sessions = [
    {"topic": "objects", "minutes": 35},
    {"topic": "functions", "minutes": 30},
    {"topic": "objects", "minutes": 25},
]

original_sessions = deepcopy(sessions)

result = useData.getSummary(sessions)

assert result == {
    "total_minutes": 90,
    "by_topic": {
        "objects": 60,
        "functions": 30,
    },
}, f"Unexpected summary: {result}"

assert original_sessions == sessions, (
        f"Function getSummary mutated input. Expected {original_sessions}, got {sessions}"
        )

print("All use_data checks passed.")
