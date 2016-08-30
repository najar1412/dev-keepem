import unittest
from datetime import datetime

import arrow

from cal_tools import get_day_name, number_of_days_in_month, get_month

class TestCal_Tools(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass

    def test_get_day_name(self):
        day_int = 2
        day_name = 'Tuesday'
        call_func = get_day_name(day_int)

        self.assertEqual(day_name, call_func)

    def test_number_of_days_in_month(self):
        _arrow_date = arrow.utcnow()
        date_today = tuple(str(_arrow_date.format()).split(' ')[0].split('-'))

        _start = datetime(int(date_today[0]), int(date_today[1]), int(date_today[2]))
        _end = datetime(int(date_today[0]), int(date_today[1]) + 1, int(date_today[2]))
        date_days_in_month = int(len
            (arrow.Arrow.range('day', _start, _end)) - 1
            )

        call_func = number_of_days_in_month(date_today)

        self.assertEqual(call_func, date_days_in_month)

    def test_get_month(self):
        call_func = get_month()
        print(call_func)

    def test_populated_calendar(self):
        pass

    def test_generate_calendar_data(self):
        pass


if __name__ == '__main__':
    unittest.main()
