import sys
import useData

def welcome():
    print("=" * 25, "Welcome!", "=" * 25)

def mainMenu():
    for i in range(len(mainMenuOptions.keys())):
        print(f"{i + 1}. {list(mainMenuOptions.keys())[i]}")

def quitPacioli():
    print("Goodbye!")
    sys.exit(0)

mainMenuOptions = {
        "Show All Stats": useData.showAll,
        "Summarize History": useData.summarize,
        "Save a Session": useData.saveSession,
        "Quit": quitPacioli,
        }

