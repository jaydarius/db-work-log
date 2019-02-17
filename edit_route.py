from display import (
    pause,
    clear_screen,
    print_record,
    edit_menu, 
    search_menu, 
    invalid_input
)
from csv_access import edit_item
from get_inputs import (
    get_date, 
    get_title, 
    get_time, 
    get_notes
)


def edit_date(record, origin_csv):
    """Edit a record's date value.

    :param record: dictionary marked for editing
    :param origin_csv: list of records in work-log.csv 
    :return: dictionary that is edited record
    """

    clear_screen()
    print("Edit Date")

    new_item = get_date()
    e_record = edit_item('date', new_item, record, origin_csv)
    record = e_record

    clear_screen()
    print("Date successfully updated!\n")
    pause()
    return record

def edit_title(record, origin_csv):
    """Edit a record's title value.

    :param record: dictionary marked for editing
    :param origin_csv: list of records in work-log.csv 
    :return: dictionary that is edited record
    """

    clear_screen()
    print("Edit Title")

    new_item = get_title()
    e_record = edit_item('title', new_item, record, origin_csv)
    record = e_record

    clear_screen()
    print("Title successfully updated!\n")
    pause()

    return record

def edit_time(record, origin_csv):
    """Edit a record's time spent value.

    :param record: dictionary marked for editing
    :param origin_csv: list of records in work-log.csv 
    :return: dictionary that is edited record
    """

    clear_screen()
    print("Edit Time Spent")

    new_item = get_time()
    e_record = edit_item('time_spent', new_item, record, origin_csv)
    record = e_record

    clear_screen()
    print("Time spent successfully updated!\n")
    pause()

    return record

def edit_notes(record, origin_csv):
    """Edit a record's notes value.

    :param record: dictionary marked for editing
    :param origin_csv: list of records in work-log.csv 
    :return: dictionary that is edited record
    """

    clear_screen()
    print("Edit Notes")

    new_item = get_notes()
    e_record = edit_item('notes', new_item, record, origin_csv)
    record = e_record

    clear_screen()
    print("Notes successfully updated!\n")
    pause()

    return record

def edit_record(record, origin_csv):
    """Continously prompt user to edit record.

    :param record: dictionary marked for editing
    :param origin_csv: list of records in work-log.csv 
    :return: None
    """

    editing = True
    origin_csv = origin_csv
    record = record

    while editing:
        clear_screen()
        print_record(record)
        edit_menu()

        edit_choice = input("> ")

        if edit_choice.lower() == "a":
            edit = edit_date(record, origin_csv)
            record = edit
        elif edit_choice.lower() == "b":
            edit = edit_title(record, origin_csv)
            record = edit
        elif edit_choice.lower() == "c":
            edit = edit_time(record, origin_csv)
            record = edit
        elif edit_choice.lower() == "d":
            edit = edit_notes(record, origin_csv)
            record = edit
        elif edit_choice.lower() == "e":
            break
        else:
            invalid_input()