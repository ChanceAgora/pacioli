from json_utils import fixEmptyFile
import menu
from config import DATA_FILE

def main():

    fixEmptyFile(DATA_FILE)
    menu.welcome()

    while True:
        menu.mainMenu()

        try:
            choice = parse_menu_choice(input(), len(menu.mainMenuOptions))
        except ValueError:
            print("Invalid Selection")
            continue

        choice = list(menu.mainMenuOptions.keys())[choice]
        menu.mainMenuOptions[choice]()

def parse_menu_choice(choice, num_options):
    choice = int(choice) - 1
    if choice < 0 or choice >= num_options:
        raise ValueError
    return choice

if __name__ == "__main__":
    main()
