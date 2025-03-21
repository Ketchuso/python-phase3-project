import sqlite3
import ipdb

# Create a connection to an SQLite database (it will create the file if it doesn't exist)
conn = sqlite3.connect('company.db')

# Create a cursor object to interact with the database
cursor = conn.cursor()

cursor.execute('''
DROP TABLE IF EXISTS customer
''')
# Create table (if not already created)

cursor.execute('''
CREATE TABLE IF NOT EXISTS customer (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER 
)
''')



# Function to insert data into the customer table
def seed_db():
    # Sample user data
    customer = [
        ('Jay', 23),
        ('Victoria', 25),
        ('Kerissa', 33),
        ('Madison', 20),
        ('Johnathan', 18)
    ]



    # Insert sample customer into the database
    cursor.executemany('''
    INSERT INTO customer (name, age)
    VALUES (?, ?)
    ''', customer)
    
    
    # Commit the transaction
    conn.commit()
    # cursor.execute()
    print(f"{len(customer)} customer added to the database.")

# Run the seed function
if __name__ == "__main__":
    seed_db()

# Close the connection
conn.close()
