import utils
import menu

def main():

    utils.fixEmptyFile()
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
            continue

if __name__ == "__main__":
    main()
