def summarize(jsonData):

    analytics = {
            "total_minutes": 0,
            "by_topic": []
            }

    for i in jsonData:
        analytics["total_minutes"] += i["minutes"]

        try:
            analytics["by_topic"][i["topic"]] += i["minutes"]
        except KeyError:
            analytics["by_topic"][i["topic"]] = i["minutes"]

    print(analytics)

def saveSession(session, jsonData):
    jsonData.append(session)
