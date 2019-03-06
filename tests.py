import unittest
from datetime import datetime
from unittest import mock

from peewee import *
import app
from db_config import Entry
from add_route import add_route
from search_route import search_route, search_entries
from get_inputs import (
    get_user,
    get_date, 
    get_title,
    get_time, 
    get_notes,
    get_keyword,
    get_parsed_date,
    get_date_range 
)
from display import (
    search_menu, 
    edit_menu, 
    page_menu,
    clear_screen
)
from db_access import (
    date_search,
    user_search,
    keyword_search,
    time_search,
    del_entry
)
from edit_route import edit_value

test_db = SqliteDatabase(":memory:")

class GetInputsTest(unittest.TestCase):
    

    @mock.patch('builtins.input', side_effect=['jay'])
    def test_get_user_jay(self, mock_input):
        result = get_user()
        self.assertEqual(result, 'jay')

    @mock.patch('builtins.input', side_effect=['12/12/2004'])
    def test_get_date(self, mock_input):
        result = get_date()
        self.assertEqual(result, '12/12/2004')

    @mock.patch('builtins.input', side_effect=['Sim Title'])
    def test_get_title(self, mock_input):
        result = get_title()
        self.assertEqual(result, 'Sim Title')
    
    @mock.patch('builtins.input', side_effect=['40'])
    def test_get_time(self, mock_input):
        result = get_time()
        self.assertEqual(result, 40)
    
    @mock.patch('builtins.input', side_effect=['Sim Notes'])
    def test_get_notes(self, mock_input):
        result = get_notes()
        self.assertEqual(result, 'Sim Notes')
    
    @mock.patch('builtins.input', side_effect=['Sim Keyword'])
    def test_get_keyword(self, mock_input):
        result = get_keyword()
        self.assertEqual(result, 'Sim Keyword')

    @mock.patch('builtins.input', side_effect=['11/11/2009'])
    def test_get_parsed_date(self, mock_input):
        result = get_parsed_date("first")
        self.assertEqual(result, datetime(2009, 11, 11, 0, 0))

    @mock.patch('builtins.input', side_effect=['11/11/2009', '13/11/2009'])
    def test_get_date_range(self, mock_input):
        result = get_date_range()
        self.assertEqual(result, ['11/11/2009', '12/11/2009'])

class DisplayTest(unittest.TestCase):

    def test_search_menu(self):
        result = search_menu()
        self.assertEqual(result, (
                "== SEARCH MENU ==\n"
                "Do you want to search by:\n"
                "a) Exact Date\n"
                "b) Range of Dates\n"  
                "c) Exact Search\n"
                "d) Employee\n"
                "e) Time Spent\n"
                "f) Return to Main Menu\n"
            )
        )
    
    def test_edit_menu(self):
        result = edit_menu()
        self.assertEqual(result, (
                "\n== EDIT MENU ==\n"
                "What would you like to edit?\n"
                "a) Date\n"
                "b) Title\n"
                "c) Time Spent\n"
                "d) Notes\n"
                "e) Return to Search Menu\n"
            )
        )
    
    def test_page_menu(self):
        result = page_menu(1, [1])
        self.assertEqual(result, "[E]dit, [D]elete, [R]eturn to Search Menu")

    def test_clear_screen(self):
        result = clear_screen()
        self.assertEqual(result, None)

class DBAccessTest(unittest.TestCase):
    pass

class AddRouteTest(unittest.TestCase):

    @mock.patch('builtins.input', side_effect=['Max K', '11/11/2009','Reading', 66, 'grabbing my wallet'])
    def test_add_route(self, mock_input):
        result = add_route()
        self.assertEqual(result, "The entry has been added!\n")

class SearchRouteTest(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.test_db = SqliteDatabase(":memory:")
        test_db.bind(Entry)

        cls.test_db.connect()
        test_db.create_tables([Entry], safe=True)

        Entry.create(
            user='Jay',
            date='12/12/2002',
            title='Building additional pylons',
            time_spent=32,
            notes='' 
    )

    @mock.patch('builtins.input', side_effect=['12/12/2002'])
    def test_entry_search_by_date(self, mock_input):
        result = search_entries(get_date, date_search)
        compare = Entry.select().where(Entry.date.contains('12/12/2002'))
        self.assertEqual(len(result), len(compare))

    @mock.patch('builtins.input', side_effect=['Jay'])
    def test_entry_search_by_user(self, mock_input):
        result = search_entries(get_user, user_search)
        compare = Entry.select().where(Entry.user.contains('Jay'))
        self.assertEqual(len(result), len(compare))

    @classmethod
    def tearDownClass(cls):
        test_db.drop_tables([Entry])
        cls.test_db.close()

class EditRouteTest(unittest.TestCase):
    
    def setUp(self):
        test_db.bind(Entry)

        test_db.connect()
        test_db.create_tables([Entry], safe=True)

        Entry.create(
            user='Jay',
            date='12/12/2002',
            title='Building additional pylons',
            time_spent=32,
            notes='' 
        )

    @mock.patch('builtins.input', side_effect=['Rolling in the dough'])
    def test_edit_value(self, mock_input):
        entry = Entry.select().where(Entry.user.contains('Jay'))
        entry_id = entry.id.get()
        result = edit_value(entry, entry_id, 'Title', get_title, edit_title_query)
        compare = Entry.select().where(Entry.user.contains('Rolling in the dough'))
        self.assertEqual(len(result), len(compare))


if __name__ == "__main__":
    unittest.main()