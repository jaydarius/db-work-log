import unittest
from unittest import mock

from get_inputs import (
    get_user,
    get_date, 
    get_title,
    get_time, 
    get_notes,
    get_keyword, 
    )


class WorkLogTest(unittest.TestCase):
    
    @mock.patch('builtins.input')
    def test_get_user(self, mocked_input):
        mocked_input.return_value = "jay"
        self.assertEqual(get_user(), "jay")

    @mock.patch('builtins.input')
    def test_get_date(self, mocked_input):
        mocked_input.side_effect = "11/11/20102"
        self.assertEqual(get_user(), "11/11/20102")

       


if __name__ == "__main__":
    unittest.main()