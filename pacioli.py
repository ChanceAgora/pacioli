from json_utils import fix_empty_file
import menu
from config import DATA_FILE

def main():

    fix_empty_file(DATA_FILE)
    menu.welcome()

    while True:
        menu.main_menu()

        try:
            choice = parse_menu_choice(input(), len(menu.main_menu_options))
        except ValueError:
            print("Invalid Selection")
            continue

        choice = list(menu.main_menu_options.keys())[choice]
        menu.main_menu_options[choice]()

def parse_menu_choice(choice: str, num_options: int) -> int:
    int_choice = int(choice) - 1
    if int_choice < 0 or int_choice >= num_options:
        raise ValueError
    return int_choice

if __name__ == "__main__":
    main()
