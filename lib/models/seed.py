import sqlite3

# Create a connection to an SQLite database (it will create the file if it doesn't exist)
conn = sqlite3.connect('company.db')

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Drop the tables if they exist
cursor.execute('DROP TABLE IF EXISTS customer')
cursor.execute('DROP TABLE IF EXISTS drinks')

# Create tables
cursor.execute('''
CREATE TABLE IF NOT EXISTS customer (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER 
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS drinks (
    id INTEGER PRIMARY KEY,
    name TEXT
)
''')

# Function to insert data into the customer and drinks tables
def seed_db():
    # Sample user data
    customers = [
        ('Jay', 23),
        ('Victoria', 25),
        ('Kerissa', 33),
        ('Madison', 20),
        ('Johnathan', 18)
    ]
    drinks = [
        ('Cosmo',),
        ('Manhattan',),
        ('Tequila Sunrise',),
        ('Rum Runner',),
        ('Bees Knees',)
    ]

    # Insert sample customers into the database
    cursor.executemany('''
    INSERT INTO customer (name, age)
    VALUES (?, ?)
    ''', customers)

    # Insert sample drinks into the database
    cursor.executemany('''
    INSERT INTO drinks (name)
    VALUES (?)
    ''', drinks)
    
    # Commit the transaction
    conn.commit()

    print(f"{len(customers)} customers added to the database.")
    print(f"{len(drinks)} drinks added to the database.")

# Run the seed function
if __name__ == "__main__":
    seed_db()

# Close the connection
conn.close()
