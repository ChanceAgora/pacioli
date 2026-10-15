from models import Session, Analytics
from copy import deepcopy
from unittest.mock import patch
import use_data

empty_result = use_data.calc_analytics([])

assert empty_result == {
        "total_minutes": 0,
        "by_topic": {},
        }, (
                f"Unexpected result for empty input: {empty_result}"
                )

sessions: list[Session] = [
    {"topic": "objects", "minutes": 35},
    {"topic": "functions", "minutes": 30},
    {"topic": "objects", "minutes": 25},
]

original_sessions = deepcopy(sessions)

result_1: Analytics = use_data.calc_analytics(sessions)

assert result_1 == {
    "total_minutes": 90,
    "by_topic": {
        "objects": 60,
        "functions": 30,
    },
}, f"Unexpected summary: {result_1}"

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
        raise AssertionError(f"Expected Value_error. Function ran normally for {topic_text}, {minutes_text}")


with patch(
        "builtins.input",
        side_effect=["   PYth_on  ", "15"]
        ):
    result_2: Session = use_data.get_session_data()

    assert result_2 == {
            "topic": "python",
            "minutes": 15
            }, (
                    f"Unexpected output. {result_2}"
                    )

with patch(
        "builtins.input",
        side_effect=[
            "", "45",
            "Objects", "",
            "objects", "10"
            ]
        ):
    with patch("builtins.print"):
        result_2 = use_data.get_session_data()

        assert result_2 == {
            "topic": "objects",
            "minutes": 10
            }


print("All use_data checks passed.")
