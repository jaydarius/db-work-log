import os
import csv
from datetime import datetime


from display import (
    main_menu,
    clear_screen, 
    invalid_input
)
from search_route import (
    search_records,
    page_records,
    search_route
)
from add_route import add_route

class Entry(Model):
    content = TextField()
    timestamp = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db

def initialize():
    """Create the database and the table if they do not exist."""
    db.connect()
    db.create_tables([Entry], safe=True)

### menu conversion ##########
def menu_loop():
    """Show the menu."""
    choice = None
    while choice !='c':
            clear_screen()
            main_menu()
            
            choice = input("> ")
            choice = choice.lower()

            clear_screen()

            if choice == "a":
                add_route()

            elif choice == "b":
                search_route()

            elif choice == "c":
                print("Thanks for using the Work Log! See ya soon.")
                break

            else:
                invalid_input()
###############################

menu = OrderedDict([
    ('a', add_entry),
    ('v', view_entries),
    ('s', search_entries)
])

if __name__ == "__main__":
    clear_screen()
    initialize()
    menu_loop()

 