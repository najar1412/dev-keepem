import sqlite3
import os
import arrow
from datetime import datetime
import datetime as dt

import random




def mock_item():
    name='mock_name'
    value = 10
    cost = 10.0
    item = tuple([name, value, cost])
    return item


def get_month(month=''):
    result_month = []
    date_day_name = {
        1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday',
        5: 'Friday', 6: 'Saturday', 7: 'Sunday'
        }

    date_today = arrow.utcnow()
    date_month = date_today.datetime.month
    date_day = date_today.datetime.day
    date_year = date_today.datetime.year

    start = datetime(2016, date_month, 1)
    end = datetime(2016, date_month + 1, 1)
    date_days_in_month = int(len(
        arrow.Arrow.range('day', start, end)) - 1
        )

    date_day_int = datetime(date_year, date_month, 1).isoweekday()
    minus_days = []

    # Helper
    _date_tuple = tuple(str(date_today.format()).split(' ')[0].split('-'))
    _date_day_list = list(range(date_days_in_month + 1)[1:])

    if date_day_int != 1:
        for i in range(date_day_int - 1):
            _minus_day = '-{}'.format(i)
            minus_days.append(_minus_day)

    result_month.append(_date_tuple)
    result_month.append(date_day_name[date_day_int])
    result_month.append(date_days_in_month)
    result_month.append(minus_days)
    result_month.append(_date_day_list)

    return result_month

def generate_calendar(amount=150):
    calendar = {}
    item_pool = [
        ('date night', 7, 60.0, 4),
        ('cinema', 7, 30.0, 4),
        ('Museum of Natural History', 10, 20.0, 1),
        ('Storm King Art Center', 10, 60.0, 1),
        ('Mohonk Mountain house', 10, 100.0, 1),
        ('Excerise', 1, 0.0, 10),
        ('Concert', 7, 100.0, 2),
        ('Wolffer Estate Vineyards', 10, 50.0, 1),
        ('Comedy Show', 7, 30.0, 4),
        ('TV Night', 2, 10.0, 8),
        ('Camping', 10, 60.0, 1),
        ('Go for a Drive', 4, 20.0, 7),
        ('Picnic in the Park', 7, 20.0, 4),
        ('Random Gift Night', 10, 50.0, 1)
        ]

    # TODO: Figure out how to weight items
    weighted_choices = [('Red', 3), ('Blue', 2), ('Yellow', 1), ('Green', 4)]
    population = [val for val, cnt in weighted_choices for i in range(cnt)]
    random.choice(population)


    item_select = []
    value = 0
    overall_value = 0
    overall_cost = 0
    high_value_filter = 0

    month_detail = get_month()
    days_of_month = month_detail[-1]
    item = random.choice(item_pool)
    print(item)


    while value <= amount:
        item = random.choice(item_pool)
        if item in item_select and item[1] > 9:
            high_value_filter += 1
            if high_value_filter >= 2:
                item = random.choice(item_pool)
                value += item[1]
                item_select.append(item)
        else:
            value += item[1]
            item_select.append(item)

    for day in days_of_month:
        calendar[day] = '.'

    for item in item_select:
        random_date = random.choice(days_of_month)
        calendar[random_date] = item

    for value in calendar.items():
        if value[1] != '.':
            overall_value += value[1][1]
            overall_cost += value[1][2]

    month_detail = month_detail[0:-1]
    month_detail.append(tuple([overall_value, overall_cost]))
    month_detail.append(calendar)

    return month_detail

generate_calendar()

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
