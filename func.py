import sqlite3
import os
from datetime import datetime
import datetime as dt
import random

import arrow

from db import db_items, db_item_filter


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
    date_days_in_month = int(len(
        arrow.Arrow.range('day', _start, _end)) - 1
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

def random_calendar(amount=150):
    calendar = {}

    month_detail = get_month()
    item_select = db_item_filter(amount)

    for day in month_detail[-1]:
        calendar[day] = '.'

    for item in item_select:
        random_date = random.choice(month_detail[-1])
        calendar[random_date] = item

    return calendar

def generate_calendar(amount=150):
    calendar = random_calendar(amount)
    value = 0
    overall_value = 0
    overall_cost = 0

    month_detail = get_month()
    days_of_month = month_detail[-1]
    item_select = db_item_filter(amount)
    item = random.choice(item_select)


    for value in calendar.items():
        if value[1] != '.':
            overall_value += value[1][1]
            overall_cost += value[1][2]

    month_detail = month_detail[0:-1]
    month_detail.append(tuple([overall_value, overall_cost]))
    month_detail.append(calendar)

    return month_detail

def keepem_db():
    if os.path.isfile('./keepem.db'):
        os.remove('keepem.db')
        conn = sqlite3.connect('keepem.db')
        c = conn.cursor()
        # create table
        c.execute('''CREATE TABLE keepem
            (id integer primary key, name text, value integer, cost real)'''
        )
        # commit and close connections
        conn.commit()
    return conn

def keepem_insert(name, value, cost):
    conn = sqlite3.connect('keepem.db')
    c = conn.cursor()
    # insert single item
    c.execute("INSERT INTO keepem VALUES (NULL, name, value, cost)")
    # save and close connection
    conn.commit()
    conn.close()

def keepem_insertmany(list):
    conn = sqlite3.connect('keepem.db')
    c = conn.cursor()
    # insert multiple items
    token_list = [
        (None, 'test_data_name', 10, 10.0),
        (None, 'test_data_name', 10, 10.0),
        (None, 'test_data_name', 10, 10.0),
        ]
    c.executemany('INSERT INTO keepem VALUES (?,?,?,?)', token_list)
    # save and close connection
    conn.commit()
    conn.close()

def keepem_find(string):
    conn = sqlite3.connect('keepem.db')
    c = conn.cursor()
    # retrive single item
    search_query = ('test_data_name',)
    c.execute('SELECT * FROM keepem WHERE name=?', search_query)
    one_item = c.fetchone()
    all_item = c.fetchall()
    # save and close connection
    conn.commit()
    conn.close()
