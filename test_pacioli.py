from pacioli import parse_menu_choice
from menu import mainMenuOptions as menu_options

options_length = len(menu_options)

invalid_choices = ("-1", "0", options_length + 1, "apple", "")

for choice in invalid_choices:
    try:
        parse_menu_choice(choice, 4)
    except ValueError:
        pass
    else:
        raise AssertionError(
                f"Function exited normally. Expected ValueError for {choice!r}"
                )

assert parse_menu_choice(1, options_length) == 0
assert parse_menu_choice(2, options_length) == 1
assert parse_menu_choice(options_length, options_length) == options_length - 1

print("All main Pacioli checks passed.")
