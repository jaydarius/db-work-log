import unittest
from unittest import mock
from contextlib import contextmanager

from get_inputs import (
    get_user,
    get_date, 
    get_title,
    get_time, 
    get_notes,
    get_keyword, 
    )


class WorkLogTest(unittest.TestCase):
    
    def test_get_user(self):
        with mock.patch('builtins.input', return_value="yes"):
            self.assertEqual(get_user(), "yes")



if __name__ == "__main__":
    unittest.main()