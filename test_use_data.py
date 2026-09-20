import use_data
from copy import deepcopy
from unittest.mock import patch

empty_result = use_data.calc_analytics([])

assert empty_result == {
        "total_minutes": 0,
        "by_topic": {},
        }, (
                f"Unexpected result for empty input: {empty_result}"
                )

sessions = [
    {"topic": "objects", "minutes": 35},
    {"topic": "functions", "minutes": 30},
    {"topic": "objects", "minutes": 25},
]

original_sessions = deepcopy(sessions)

result = use_data.calc_analytics(sessions)

assert result == {
    "total_minutes": 90,
    "by_topic": {
        "objects": 60,
        "functions": 30,
    },
}, f"Unexpected summary: {result}"

assert original_sessions == sessions, (
        f"Function mutated input. Expected {original_sessions}, got {sessions}"
        )


assert use_data.parse_session("python", "10") == {
        "topic": "python",
        "minutes": 10
        }
assert use_data.parse_session("   FUNCTIONS   ", "30") == {
        "topic": "functions",
        "minutes": 30
        }
assert use_data.parse_session("objects", "  30  ") == {
        "topic": "objects",
        "minutes": 30
        }

invalid_sessions = (
        ( "", "30" ),
        ( "tests", "" ),
        ( "tests", "  -3  " ),
        ( "procedural code", "0" ),
        ( "python", "fifteen" )
        )

for topic_text, minutes_text in invalid_sessions:
    try:
        use_data.parse_session(topic_text, minutes_text)
    except ValueError:
        pass
    else:
        raise AssertionError(f"Expected ValueError. Function ran normally for {i}")


with patch(
        "builtins.input",
        side_effect=["   PYthOn  ", "15"]
        ):
    result = use_data.getSessionData()

    assert result == {
            "topic": "python",
            "minutes": 15
            }, (
                    f"Unexpected output. {result}"
                    )


print("All use_data checks passed.")
