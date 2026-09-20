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

def parse_menu_choice(choice: str, num_options: int) -> int:
    int_choice = int(choice) - 1
    if int_choice < 0 or int_choice >= num_options:
        raise ValueError
    return int_choice

if __name__ == "__main__":
    main()
