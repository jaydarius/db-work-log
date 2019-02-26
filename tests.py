import unittest
from datetime import datetime
from unittest import mock

from get_inputs import (
    get_user,
    get_date, 
    get_title,
    get_time, 
    get_notes,
    get_keyword,
    get_parsed_date 
    )


class WorkLogTest(unittest.TestCase):
    

    @mock.patch('builtins.input', side_effect=['jay'])
    def test_get_user_jay(self, mocked_input):
        result = get_user()
        self.assertEqual(result, 'jay')

    @mock.patch('builtins.input', side_effect=['', '\n'])
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
    def test_get_keyword(self, mocked_input):
        result = get_parsed_date("first")
        self.assertEqual(result, datetime(2009, 11, 11, 0, 0))


if __name__ == "__main__":
    unittest.main()