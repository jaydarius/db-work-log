from get_inputs import (
    get_date, 
    get_title,
    get_time, 
    get_notes,
    get_keyword, 
    get_regex
    )
from csv_access import insert_record
from display import clear_screen, pause
from db_config import Entry


def add_entry(date, title, time_spent, notes):
    """Add params to dictionary and insert it into 
    csv.

    :param date: string containing date
    :param title: string containing title
    :param time_spent: string containing time
    :param notes: string containing notes
    :return: None
    """
    
    Entry.create(
        date=date, 
        title=title, 
        time_spent=time_spent,
        notes=notes)
    print("Entered!")


def add_route():
    """Add an entry"""

    date = get_date()
    title = get_title()
    time_spent = get_time()
    notes = get_notes() 
    
    add_entry(date, title, time_spent, notes)
    clear_screen()
    print("The entry has been added!\n")
    pause()
        
