from get_inputs import (
    get_user,
    get_date, 
    get_title,
    get_time, 
    get_notes,
    get_keyword, 
    )

from display import clear_screen, pause
from db_config import Entry


def add_route():
    """Add an entry"""

    Entry.create(
        user=get_user(),
        date=get_date(),
        title=get_title(),
        time_spent=get_time(),
        notes=get_notes() 
    )
    clear_screen()
    return ("The entry has been added!\n")

