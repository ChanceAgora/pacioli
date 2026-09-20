import json
from models import Session

def fixEmptyFile(dataFile: str) -> None:
    empty = False

    with open(dataFile, "r") as file:
        if not file.read().strip():
            empty = True

    if empty:
        with open(dataFile, "w") as file:
            json.dump([], file)

def loadData(dataFile: str) -> list[Session]:
    with open(dataFile, "r") as file:
        return json.load(file)

def exportData(data: list[Session], dataFile: str) -> None:
    with open(dataFile, "w") as file:
        json.dump(data, file)
