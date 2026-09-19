import sys
import use_data

def welcome():
    print("=" * 25, "Welcome!", "=" * 25)

def mainMenu():
    for i in range(len(mainMenuOptions.keys())):
        print(f"{i + 1}. {list(mainMenuOptions.keys())[i]}")

def quitPacioli():
    print("Goodbye!")
    sys.exit(0)

mainMenuOptions = {
        "Show All Stats": use_data.showAll,
        "Summarize History": use_data.summarize,
        "Save a Session": use_data.saveSession,
        "Quit": quitPacioli,
        }

