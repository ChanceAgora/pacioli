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

    menu.welcome()

    while(True):
        menu.mainMenu()

        choice = input()

        try:
            choice = int(choice) - 1

            choice = list(menu.mainMenuOptions.keys())[choice]

            menu.mainMenuOptions[choice]
        except ValueError:
            print("Invalid option")
            print()
            continue
main()
