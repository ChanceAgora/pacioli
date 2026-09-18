import json
import menu

FILE = "sessions.json"

def main():

    menu.welcome()
    while(True):
        menu.mainMenu()
        choice = input()
        try:
            choice = int(choice) - 1
            choice = list(menu.mainMenuOptions.keys())[choice]
            menu.mainMenuOptions[choice]()
        except ValueError:
            print("Invalid option")
            print()
            continue
main()
