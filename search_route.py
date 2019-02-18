from db_access import (
    meta_search,
    date_search,
    user_search,
    keyword_search,
    time_search
)
from edit_route import edit_record
from display import (
    print_entry,
    clear_screen,
    pause,
    invalid_input,
    page_menu,
    search_menu
)                    
from get_inputs import (
    get_user,
    get_date,
    get_date_range, 
    get_title, 
    get_time, 
    get_notes, 
    get_keyword,
)


def page_entries(entries):
    """Display each record with paging options.

    :param entries: list of entries found with search criteria
    :return:None
    """

    index = 0
    paging = True
    edited_record = None
    
    while paging:
        entry = entries[index]

        clear_screen()
        print("Result {} out of {}".format(index+1, len(entries)))
        print('='*10)
        print_entry(entry)
        print('='*10)
        page_menu(index, entries)
        user_choice = input("\n> ")

        if user_choice == "n":
            if index == (len(entries) - 1):
                print("\nCan't go forward!\n")
                pause()
            else:
                index += 1
            continue
        elif user_choice == "b":
            if index < 1:
                print("\nCan't go back!\n")
                pause()
            else:
                index -= 1
            continue
        elif user_choice == "e":
            edit_record(record, origin_csv)
            break
        elif user_choice == "d":
            del_record(record, origin_csv)
            clear_screen()
            print(""""{}" log has been deleted!\n""".format(record['title']))       
            pause()
            break
        elif user_choice == "r":
            break    
        else:
            invalid_input()


def search_records(get_value, search, column=None):
    """Locate matching records.

    :param get_value: object containing user's input
    :param search: function that will apply user's input
    :return: None
    """
    user_input = get_value()
    entries = search(user_input)  
   
    if not entries:
        print("Not found!\n")
        pause()
    else:
        page_entries(entries)

def search_route():
    """Search for record(s)"""
    searching = True

    while searching:
        search_menu()
        
        choice = input("> ")
        choice = choice.lower()
        
        clear_screen()

        if choice == 'a':
            search_records(get_date, date_search)
        elif choice == 'b':
            search_records(get_date_range, date_search)
        elif choice == 'c':
            search_records(get_keyword, keyword_search)
        elif choice == 'd':
            search_records(get_user, user_search)
        elif choice == 'e':
            search_records(get_time, time_search)
        elif choice == 'f':
            break
        else:
            invalid_input()

        clear_screen()

