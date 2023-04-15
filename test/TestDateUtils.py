import unittest
from dates.DateUtils import DateUtils


class TestDateUtils(unittest.TestCase):
    def test_get_date_as_str_001(self):
        date_utils = DateUtils()
        fecha = date_utils.get_date_as_str()
        self.assertTrue('2023' in fecha)
