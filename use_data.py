from config import DATA_FILE
import json
from json_utils import loadData, exportData

def getSummary(jsonData):
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

def summarize():
    summary = loadData(DATA_FILE)
    summary = getSummary(summary)
    print(json.dumps(summary, indent=4))


def saveSession():
    jsonData = loadData(DATA_FILE)
    session = getSessionData()
    jsonData.append(session)
    exportData(jsonData, DATA_FILE)


def getSessionData():
    topic = input("What topic did you study? ").strip().lower()
    minutes = int(input("Number of minutes? "))

    return {"topic": topic, "minutes": minutes}


def showAll():
    session = loadData(DATA_FILE)
    print(json.dumps(session, indent=4))
