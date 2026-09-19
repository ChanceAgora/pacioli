import utils
import menu
from config import DATA_FILE

def main():

    utils.fixEmptyFile(DATA_FILE)
    menu.welcome()

    while True:
        menu.mainMenu()
        choice = input()

        try:
            choice = int(choice) - 1
            if choice < 0 or choice >= len(menu.mainMenuOptions.keys()):
                raise ValueError("Invalid Option")
        except ValueError:
            print("Invalid Selection")
            choice = 0
            continue

        choice = list(menu.mainMenuOptions.keys())[choice]
        menu.mainMenuOptions[choice]()

if __name__ == "__main__":
    main()
