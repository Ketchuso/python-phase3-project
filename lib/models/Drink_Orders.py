from __init__ import CONN, CURSOR


class Drink_Orders():
    def __init__(self):
        pass

    @classmethod
    def customer_drinks(cls):
        sql = '''
            customer_name TEXT,
            customer_id INTEGER,
            drink_name TEXT,
            drink_id INTEGER,
            PRIMARY KEY (customer_name, customer_id, drink_name, drink_id),
            FOREIGN KEY (customer_name) REFERENCES customer(name),
            FOREIGN KEY (customer_id) REFERENCES customer(id),
            FOREIGN KEY (drink_name) REFERENCES drink(name),
            FOREIGN KEY (drink_id) REFERENCES drinks(id);
        '''
        CURSOR.execute(sql)
        CONN.commit()



