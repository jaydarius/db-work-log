from collections import OrderedDict
import os
from datetime import datetime

from peewee import *

from db_config import Entry, db, initialize
from display import (
    clear_screen, 
    invalid_input,
    menu_loop
)
from search_route import (
    search_records,
    page_entries,
    search_route
)
from add_route import add_route


if __name__ == "__main__":
    clear_screen()
    initialize()
    menu_loop()

 