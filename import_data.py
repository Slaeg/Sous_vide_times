import sqlite3
import csv

def create_connection(db_file):
    """Create a database connection to the SQLite database specified by db_file."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
    return conn

def create_table(conn):
    """Create the SousVideTimes table in the SQLite database."""
    try:
        c = conn.cursor()
        c.execute('DROP TABLE IF EXISTS SousVideTimes')
        c.execute('''
            CREATE TABLE SousVideTimes(
                id INTEGER PRIMARY KEY, 
                food_type TEXT, 
                temperature REAL, 
                cooking_time TEXT)
        ''')
    except sqlite3.Error as e:
        print(f"Error creating table: {e}")

def insert_data(conn, csv_file):
    """Insert data from the CSV file into the SousVideTimes table."""
    try:
        c = conn.cursor()
        with open(csv_file, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            for row in reader:
                if len(row) == 4:
                    c.execute('''
                        INSERT INTO SousVideTimes (id, food_type, temperature, cooking_time)
                        VALUES (?, ?, ?, ?)
                    ''', row)
                else:
                    print(f'Skipping row due to insufficient columns: {row}')
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error inserting data: {e}")

def main():
    database = "sous_vide.db"
    csv_file = "sous_vide.csv"

    # Create a database connection
    conn = create_connection(database)
    if conn is not None:
        # Create table
        create_table(conn)
        # Insert data
        insert_data(conn, csv_file)
        # Close the connection
        conn.close()
    else:
        print("Error! Cannot create the database connection.")

if __name__ == '__main__':
    main()
