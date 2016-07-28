import random

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
