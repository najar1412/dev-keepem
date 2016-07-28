import sqlite3
import random
import os


def db_items():
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
    return item_pool


def db_item_filter(amount=100):
    item_select = []
    value = 0
    high_value_filter = 0

    """
    # TODO: Figure out how to weight items
    weighted_choices = [('Red', 3), ('Blue', 2), ('Yellow', 1), ('Green', 4)]
    population = [val for val, cnt in weighted_choices for i in range(cnt)]
    random.choice(population)
    """

    while value <= amount:
        item = random.choice(db_items())
        if item in item_select and item[1] > 9:
            high_value_filter += 1
            if high_value_filter >= 2:
                item = random.choice(db_items())
                value += item[1]
                item_select.append(item)
        else:
            value += item[1]
            item_select.append(item)

    return item_select


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
