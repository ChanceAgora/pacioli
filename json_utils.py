import json

def fixEmptyFile(dataFile):
    empty = False

    with open(dataFile, "r") as file:
        if not file.read().strip():
            empty = True

    if empty:
        with open(dataFile, "w") as file:
            json.dump([], file)

def loadData(dataFile):
    with open(dataFile, "r") as file:
        return json.load(file)

def exportData(data, dataFile):
    with open(dataFile, "w") as file:
        json.dump(data, file)
