from models.__init__ import CONN, CURSOR


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

    @classmethod
    def insert_drink_order(cls, customer_name, customer_id, drink_name):
        sql = '''
            INSERT INTO drink_orders(customer_name, customer_id, drink_name),
            VALUES (%s, %s, %s, %s);
        '''
        CURSOR.execute(sql, (customer_name, customer_id, drink_name))
        CONN.commit()

    @classmethod
    def drinks_database(cls):
        sql = "SELECT name, id FROM customer;"
        CURSOR.execute(sql)
        return CURSOR.fetchall()
    
    # @classmethod
    # def cli_drink_orders(cls):
    #     customers = cls.drinks_database
    #     drinks = cls.cli_drink_orders
    #     print("Open Tabs: ")
    #     for idx, (name, _) in enumerate(customers, 1):
    #         print(f"{idx}. {name}")
    #     customer_choice = int(input("Select a Customer Name"))
    #     customer_name, customer_id = customers[customer_choice -1]
    #     print("\n Availble Drinks")
    #     for idx, (drink_name, _) in enumerate(drinks, 1):
    #         print(f"{idx}, {drink_name}")
    #     drink_choice = int(input("Select a Drinks"))


    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT * FROM drink_orders
            WHERE customer_id = ?;
        """

        row = CURSOR.execute(sql, (id,)).fetchall()
        if row:
            return cls.instance_from_row(row)
        else:
            return None
    
    
    def update(self):
        sql = """
            UPDATE drink_orders
            SET customer_name = ?,
            WHERE customer_id = ?;
        """
        CURSOR.execute(sql, (self.name, self.id))
        CONN.commit()




