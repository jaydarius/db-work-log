import os
from datetime import datetime, timedelta

from display import clear_screen

def get_user():
    print("Employee name\n")
    user = input("> ")
    if len(user) == 0:
        raise NameError("Please enter a valid name.")
    clear_screen()
    return user

def get_date():
    """Ask the user to add date and return it in a string"""

    while True: 
        try:  
            print( "Date of the task\nPlease use DD/MM/YYYY\n")

            date = input("> ")
            parsed_date = datetime.strptime(date, '%d/%m/%Y')
            formatted_date = parsed_date.strftime('%d/%m/%Y')

            clear_screen()
            return formatted_date
        except ValueError:
            print("\n{} doesn't seem to be a valid date and time."
                  .format(date))
            input("\nPress any key to continue")
            clear_screen()
            continue

def get_parsed_date(index):
    """Ask the user to add date
    
    :param index: string containing position of range (first or second)
    :return: datetime object
    """

    while True: 
        try:
            if index == 'first':  
                print("First Date\nPlease use DD/MM/YYYY\n")
            elif index == 'second':
                print("Second Date\nPlease use DD/MM/YYYY\n")

            date = input("> ")
            parsed_date = datetime.strptime(date, '%d/%m/%Y')

            clear_screen()
            return parsed_date
        except ValueError:
            print("\n{} doesn't seem to be a valid date and time."
                  .format(date))
            input("\nPress any key to continue")
            clear_screen()
            continue

def get_date_range():
    """Ask the user to add 2 dates and return each date between in a list."""
    
    date_list = []
    start = get_parsed_date("first")
    end = get_parsed_date("second")

    date_array = (start + timedelta(days=x) for x in range(0, (end-start).days))

    for date_object in date_array:
        date_list.append(date_object.strftime('%d/%m/%Y'))

    return date_list

def get_title():
    """Ask the user to add title and return it in a string"""
    
    while True:
        try: 
            print("Title of the task\n")
            title = input("> ")
            if len(title) == 0:
                raise NameError("Please enter a valid title.")
            clear_screen()
            return title
        except NameError as e:
            print(e)
            input("\nPress any key to continue")
            clear_screen()
            continue
         
def get_time():
    """Ask the user to add time spent and return it as an integer"""
    while True:
        try:  
            print("Minutes spent on the task (rounded)\n")

            time_spent = input("> ")
            time_spent = int(time_spent)  

            clear_screen()
            return time_spent
        except ValueError:
            print("\n{} doesn't seem to be a valid number."
                  .format(time_spent))
            input("\nPress any key to continue")
            clear_screen()
            continue

def get_notes():
    """Ask the user to add notes and return it in a string"""

    while True:
        print("Notes (optional)\n")
        return input("> ")

def get_keyword():
    """Ask the user to add date and return it in a string"""

    while True:
        try: 
            print("Keyword\n")
            keyword = input("> ")
            if len(keyword) == 0:
                raise NameError("Please enter a valid keyword.")
            clear_screen()
            return keyword
        except NameError as e:
            print(e)
            input("\nPress any key to continue")
            clear_screen()
            continue
