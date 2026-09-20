import use_data
from copy import deepcopy

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
        ( "procedural code", "0" )
        )

for i in invalid_sessions:
    try:
        assert use_data.parse_session(i[0], i[1])
    except ValueError:
        pass
    else:
        raise AssertionError("Expected ValueError. Function ran normally.")


print("All use_data checks passed.")
