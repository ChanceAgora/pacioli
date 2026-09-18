from config import DATA_FILE
import json
from utils import loadData

def getSummary(jsonData):
    analytics = {
            "total_minutes": 0,
            "by_topic": {}
            }

    for i in jsonData:
        analytics["total_minutes"] += i["minutes"]
        try:
            analytics["by_topic"][i["topic"]] += i["minutes"]
        except KeyError:
            analytics["by_topic"][i["topic"]] = i["minutes"]

    return analytics

def summarize():
    jsonData = loadData()
    print(json.dumps(getSummary(jsonData), indent=4))

def saveSession():
    jsonData = []

    with open(DATA_FILE, "r") as file:
        jsonData = json.load(file)

    session = getSessionData()

    jsonData.append(session)

    with open(DATA_FILE, "w") as file:
        json.dump(jsonData, file)

def getSessionData():
    topic = input("What topic did you study? ").strip().lower()
    minutes = int(input("Number of minutes? "))

    return {"topic": topic, "minutes": minutes}
