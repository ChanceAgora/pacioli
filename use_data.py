from config import DATA_FILE
import json
from json_utils import loadData, exportData
from models import session

def calc_analytics(jsonData: list[dict[str, int]]) -> dict[str, int]:
    analytics = {
            "total_minutes": 0,
            "by_topic": {}
            }

    for i in jsonData:
        if type(i) != dict:
            continue

        analytics["total_minutes"] += i["minutes"]
        try:
            analytics["by_topic"][i["topic"]] += i["minutes"]
        except KeyError:
            analytics["by_topic"][i["topic"]] = i["minutes"]

    return analytics

def summarize() -> None:
    summary = loadData(DATA_FILE)
    summary = calc_analytics(summary)
    print(json.dumps(summary, indent=4))


def saveSession() -> None:
    jsonData = loadData(DATA_FILE)
    session = getSessionData()
    jsonData.append(session)
    exportData(jsonData, DATA_FILE)



def getSessionData() -> dict[str, int]:
    while True:
        topic_text = input("What topic did you study? ")
        minutes_text = input("Number of minutes? ")

        try:
            return parse_session(topic_text, minutes_text)
        except ValueError as error:
            print(error)

def parse_session(topic: str, minutes_text: str) -> session:
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



def showAll() -> None:
    session = loadData(DATA_FILE)
    print(json.dumps(session, indent=4))
