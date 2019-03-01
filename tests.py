import unittest
from datetime import datetime
from unittest import mock

import app
from add_route import add_route
from search_route import search_route
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
from display import search_menu, edit_menu, page_menu

class GetInputsTest(unittest.TestCase):
    

    @mock.patch('builtins.input', side_effect=['jay'])
    def test_get_user_jay(self, mocked_input):
        result = get_user()
        self.assertEqual(result, 'jay')

    @mock.patch('builtins.input', side_effect=['12/12/2004'])
    def test_get_date(self, mocked_input):
        result = get_date()
        self.assertEqual(result, '12/12/2004')

    @mock.patch('builtins.input', side_effect=['Sim Title'])
    def test_get_title(self, mocked_input):
        result = get_title()
        self.assertEqual(result, 'Sim Title')
    
    @mock.patch('builtins.input', side_effect=['40'])
    def test_get_time(self, mocked_input):
        result = get_time()
        self.assertEqual(result, 40)
    
    @mock.patch('builtins.input', side_effect=['Sim Notes'])
    def test_get_notes(self, mocked_input):
        result = get_notes()
        self.assertEqual(result, 'Sim Notes')
    
    @mock.patch('builtins.input', side_effect=['Sim Keyword'])
    def test_get_keyword(self, mocked_input):
        result = get_keyword()
        self.assertEqual(result, 'Sim Keyword')

    @mock.patch('builtins.input', side_effect=['11/11/2009'])
    def test_get_parsed_date(self, mocked_input):
        result = get_parsed_date("first")
        self.assertEqual(result, datetime(2009, 11, 11, 0, 0))

    @mock.patch('builtins.input', side_effect=['11/11/2009', '13/11/2009'])
    def test_get_date_range(self, mocked_input):
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

class AddRouteTest(unittest.TestCase):

    @mock.patch('builtins.input', side_effect=['Max K', '11/11/2009','Reading', 66, 'grabbing my wallet'])
    def test_add_route(self, mocked_input):
        result = add_route()
        self.assertEqual(result, "The entry has been added!\n")

class SearchRouteTest(unittest.TestCase):

    # setUp()

    @mock.patch('builtins.input', side_effect=['a', '12/12/2009','r'])
    def test_searche_route(self, mocked_input):
        result = search_route()
        self.assertEqual(result, True)

    # tearDown()
    


if __name__ == "__main__":
    unittest.main()