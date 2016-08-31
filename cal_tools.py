from datetime import datetime
import random

import arrow

from db import db_items, db_item_filter


class Month():
    """Build out class to access everything 'calandar month' related"""

    _date = arrow.utcnow()
    date_day_int = datetime(int(_date.year), int(_date.month), int(_date.day)).isoweekday()

    def get_day_name(self):
        day_name = {
            1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday',
            5: 'Friday', 6: 'Saturday', 7: 'Sunday'
            }
        return day_name[self.date_day_int]

test = Month()

print(test.get_day_name())



def get_day_name(monday=1):
    day_name = {
        1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday',
        5: 'Friday', 6: 'Saturday', 7: 'Sunday'
        }
    return day_name[monday]


def number_of_days_in_month(date_today):
    _arrow_date = arrow.utcnow()
    date_today = tuple(str(_arrow_date.format()).split(' ')[0].split('-'))

    _start = datetime(int(date_today[0]), int(date_today[1]), int(date_today[2]))
    _end = datetime(int(date_today[0]), int(date_today[1]) + 1, int(date_today[2]))
    date_days_in_month = int(len
        (arrow.Arrow.range('day', _start, _end)) - 1
        )
    return date_days_in_month


def get_month(month=''):
    result_month = []
    minus_days = []

    _arrow_date = arrow.utcnow()
    date_today = tuple(str(_arrow_date.format()).split(' ')[0].split('-'))

    date_days_in_month = number_of_days_in_month(date_today)
    date_day_int = datetime(int(date_today[0]), int(date_today[1]), 1).isoweekday()
    date_day_list = list(range(date_days_in_month + 1)[1:])

    # Minus day padding
    if date_day_int != 1:
        for i in range(date_day_int - 1):
            _minus_day = '-{}'.format(i)
            minus_days.append(_minus_day)

    result_month.append(date_today)
    result_month.append(get_day_name(date_day_int))
    result_month.append(date_days_in_month)
    result_month.append(minus_days)
    result_month.append(date_day_list)

    return result_month


def populated_calendar(amount=150):
    calendar = {}

    month_detail = get_month()
    item_select = db_item_filter(amount)

    for day in month_detail[-1]:
        calendar[day] = '.'

    for item in item_select:
        random_date = random.choice(month_detail[-1])
        calendar[random_date] = item

    return calendar


def generate_calendar_data(amount=150):
    calendar = populated_calendar(amount)
    value = 0
    overall_value = 0
    overall_cost = 0

    month_detail = get_month()
    days_of_month = month_detail[-1]
    item_select = db_item_filter(amount)

    for value in calendar.items():
        if value[1] != '.':
            overall_value += value[1][1]
            overall_cost += value[1][2]

    calendar_data = month_detail[0:-1]
    calendar_data.insert(-1, tuple([overall_value, overall_cost]))
    calendar_data.append(calendar)

    return calendar_data
