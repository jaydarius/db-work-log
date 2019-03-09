from get_inputs import (
    get_user,
    get_date, 
    get_title,
    get_time, 
    get_notes,
    get_keyword, 
    )

from display import clear_screen
from db_config import Entry
from exceptions import (InvalidDate, InvalidKeyword, InvalidTime, InvalidTitle, InvalidUser)


def add_route():
    adding = True

    while adding:
        try:
            user = get_user()
        except InvalidUser as e:
            print(e)
            input("\nPress any key to continue")
            clear_screen()
        try:
            date = get_date()
        except ValueError:
            print("\nDoesn't seem to be a valid date and time.")
            input("\nPress any key to continue")
            clear_screen()
            continue
        try:
            title = get_title()
        except InvalidTitle as e:
            print(e)
            input("\nPress any key to continue")
            clear_screen()
        try:
            time_spent = get_time()
        except InvalidTime:
            print("\n{} doesn't seem to be a valid number."
                    .format(time_spent))
            input("\nPress any key to continue")
            clear_screen()
        notes = get_notes()

    Entry.create(
        user=user,
        date=date,
        title=title,
        time_spent=time_spent,
        notes=notes 
    )
