import json
import menu

FILE = "sessions.json"

def main():

    sessions = []

    try:
        with open(FILE, "r") as file:
            sessions = json.load(file)
    except json.decoder.JSONDecodeError:
        with open(FILE, "w") as file:
            json.dump([{}], file)
            print(f"{FILE} was empty")

    menu.mainMenu()

main()
