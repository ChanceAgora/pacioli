from pacioli import parse_menu_choice

invalid_choices = ("-1", "0", "5", "apple", "")

for choice in invalid_choices:
    try:
        parse_menu_choice(choice, 4)
    except ValueError:
        pass
    else:
        raise AssertionError(
                f"Function exited normally. Expected ValueError for {choice!r}"
                )

assert parse_menu_choice("1", 4) == 0
assert parse_menu_choice("2", 4) == 1
assert parse_menu_choice("4", 4) == 3

print("All main Pacioli checks passed.")
