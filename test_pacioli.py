from pacioli import parse_menu_choice

invalid_choices = ("0", "21e3", "-1", "apple", "")

for choice in invalid_choices:
    try:
        parse_menu_choice(choice, 4)
    except ValueError:
        pass
    else:
        raise AssertionError(
                f"Function exited normally. Expected ValueError for {choice!r}"
                )

print("All main Pacioli checks passed.")
