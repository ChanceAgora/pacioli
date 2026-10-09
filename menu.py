import sys
import use_data

def welcome() -> None:
    print("=" * 25, "Welcome!", "=" * 25)

def main_menu() -> None:
    for i in range(len(main_menu_options.keys())):
        print(f"{i + 1}. {list(main_menu_options.keys())[i]}")

def quit_pacioli() -> None:
    print("Goodbye!")
    sys.exit(0)

main_menu_options = {
        "Show All Stats": use_data.show_all,
        "Summarize History": use_data.summarize,
        "Save a Session": use_data.save_session,
        "Quit": quit_pacioli,
        }

