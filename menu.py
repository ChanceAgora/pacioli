import useData

mainMenuOptions = {
        "Save a Session": useData.saveSession,
        "Summarize History": useData.summarize,
        }

def welcome():
    print("=" * 25, "Welcome!", "=" * 25)

def mainMenu():
    for i in range(len(mainMenuOptions.keys())):
        print(f"{i + 1}. {list(mainMenuOptions.keys())[i]}")
