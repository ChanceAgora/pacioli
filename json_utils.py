import json
from models import Session

def fix_empty_file(data_file: str) -> None:
    empty = False

    with open(data_file, "r") as file:
        if not file.read().strip():
            empty = True

    if empty:
        with open(data_file, "w") as file:
            json.dump([], file)

def load_data(data_file: str) -> list[Session]:
    with open(data_file, "r") as file:
        return json.load(file)

def export_data(data: list[Session], data_file: str) -> None:
    with open(data_file, "w") as file:
        json.dump(data, file)
