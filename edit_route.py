from db_config import Entry
from display import (
    pause,
    clear_screen,
    edit_menu, 
    search_menu, 
    invalid_input,
    print_entry
)
from get_inputs import (
    get_date, 
    get_title, 
    get_time, 
    get_notes
)
from db_access import (
    edit_date_query,
    edit_title_query,
    edit_time_query,
    edit_notes_query
)

def edit_value(entry, entry_id, key, get_func, db_query):

    clear_screen()
    print("Edit {}".format(key))
    new_value = get_func()

    entry = db_query(new_value, entry_id)

    clear_screen()
    print("{} successfully updated!\n".format(key))
    pause()
    return entry


def edit_entry(entry, entry_id):
    """Continously prompt user to edit entry.

    :param entry: Entry marked for editing
    :return: None
    """


    editing = True

    while editing:
        clear_screen()
        print_entry(entry)
        edit_menu()

        edit_choice = input("> ")

        if edit_choice.lower() == "a":
            entry = edit_value(entry, entry_id, 'Date', get_date, edit_date_query)
        elif edit_choice.lower() == "b":
            entry = edit_value(entry, entry_id, 'Title', get_title, edit_title_query)
        elif edit_choice.lower() == "c":
            entry = edit_value(entry, entry_id, 'Time', get_time, edit_time_query)
        elif edit_choice.lower() == "d":
            entry = edit_value(entry, entry_id, 'Notes', get_notes, edit_notes_query)
        elif edit_choice.lower() == "e":
            break
        else:
            invalid_input()