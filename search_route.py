from csv_access import (
    insert_record,
    open_csv,
    date_search,
    date_range_search,
    keyword_search,
    regex_search,
    time_search,
    del_record
)
from edit_route import edit_record
from display import (
    print_record,
    clear_screen,
    pause,
    invalid_input,
    page_menu,
    search_menu
)                    
from get_inputs import (
    get_date,
    get_date_range, 
    get_title, 
    get_time, 
    get_notes, 
    get_keyword, 
    get_regex
)

def page_records(records):
    """Display each record with paging options.

    :param records: list of records found with search criteria
    :return:None
    """

    index = 0
    origin_csv = open_csv('work-log.csv')
    searching = True
    edited_record = None
    
    while searching:
        record = records[index]

        clear_screen()
        print("Result {} out of {}".format(index+1, len(records)))
        print_record(record)
        page_menu(index, records)
        user_choice = input("> ")

        if user_choice == "n":
            if index == (len(records) - 1):
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


def search_records(get_value, search):
    """Locate matching records.

    :param get_value: object containing user's input
    :param search: function that will apply user's input
    :return: None
    """
    user_input = get_value()
    records = search(user_input)  

    if not records:
        print("Not found!\n")
        pause()
    else:
        page_records(records)

def search_route():
    """Search for record(s)"""
    searching = True

    

    while searching:
        if open_csv("work-log.csv") == False:
            searching = False

            print("Work log is empty! Please add a new entry.\n")
            pause()
            break
            
        search_menu()
        
        choice = input("> ")
        choice = choice.lower()
        
        clear_screen()

        if choice == 'a':
            search_records(get_date, date_search)
        elif choice == 'b':
            search_records(get_date_range, date_range_search)
        elif choice == 'c':
            search_records(get_keyword, keyword_search)
        elif choice == 'd':
            search_records(get_regex, regex_search)
        elif choice == 'e':
            search_records(get_time, time_search)
        elif choice == 'f':
            break
        else:
            invalid_input()

        clear_screen()

