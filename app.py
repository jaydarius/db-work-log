from collections import OrderedDict
import os
from datetime import datetime

from peewee import *

from db_config import Entry, db, initialize
from display import (
    clear_screen, 
    invalid_input,
    pause
)
from search_route import (
    search_records,
    page_entries,
    search_route
)
from add_route import add_route


def menu_loop():
    """Show the menu."""

    choice = None
    menu = OrderedDict([
        ('a', add_route),
        ('b', search_route)
    ])


    while choice !='c':
        clear_screen()
        print("== WORK LOG==\n")
        for key, value in menu.items():
            print("{}) {}".format(key, value.__doc__))
        print("c) Quit")

        choice = input("\n> ").lower().strip()

        if choice in menu:
            clear_screen()
            if choice == 'a':
                print(menu[choice]())
                pause()
            else:
                menu[choice]()
            

if __name__ == "__main__":
    clear_screen()
    initialize()
    menu_loop()

 