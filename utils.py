import json
from config import DATA_FILE

def fixEmptyFile():
    empty = False

    with open(DATA_FILE, "r") as file:
        if not file.read().strip():
            empty = True

    if empty:
        with open(DATA_FILE, "w") as file:
            json.dump([], file)

def loadData():
    with open(DATA_FILE, "r") as file:
        return json.load(file)
