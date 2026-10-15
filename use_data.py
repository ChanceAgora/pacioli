from config import DATA_FILE
import json
from json_utils import load_data, export_data
from models import Session, Analytics

def calc_analytics(json_data: list[Session]) -> Analytics:
    analytics: Analytics = {
            "total_minutes": 0,
            "by_topic": {}
            }

    for i in json_data:
        analytics["total_minutes"] += i["minutes"]
        try:
            analytics["by_topic"][i["topic"]] += i["minutes"]
        except KeyError:
            analytics["by_topic"][i["topic"]] = i["minutes"]

    return analytics

def summarize() -> None:
    summary = load_data(DATA_FILE)
    summary = calc_analytics(summary)
    print(json.dumps(summary, indent=4))


def save_session() -> None:
    json_data = load_data(DATA_FILE)
    session = get_session_data()
    json_data.append(session)
    export_data(json_data, DATA_FILE)



def get_session_data() -> Session:
    while True:
        topic_text = input("What topic did you study? ")
        minutes_text = input("Number of minutes? ")

        try:
            return parse_session(topic_text, minutes_text)
        except ValueError as error:
            print(error)

def parse_session(
        topic: str, 
        minutes_text: str
        ) -> Session:
    topic = topic.strip().lower()
    minutes_text = minutes_text.strip()

    if topic == "":
        raise ValueError("Topic cannot be empty.")
    if minutes_text == "":
        raise ValueError("Minutes cannot be empty.")
    
    try:
        minutes = int(minutes_text)
    except ValueError:
        raise ValueError("Minutes must be a number in digits.")

    if minutes < 1:
        raise ValueError("Minutes must be more than 0.")

    return {"topic": topic, "minutes": minutes}



def show_all() -> None:
    session = load_data(DATA_FILE)
    print(json.dumps(session, indent=4))
