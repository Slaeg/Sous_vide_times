import sqlite3
import csv

conn = sqlite3.connect('sous_vide.db')

c = conn.cursor()

c.execute('DROP TABLE IF EXISTS SousVideTimes')
c.execute('''
    CREATE TABLE SousVideTimes(
        id INTEGER PRIMARY KEY, 
        food_type TEXT, 
        temperature REAL, 
        cooking_time TEXT)
''')

with open('sous_vide.csv', 'r') as file:
    # Create a CSV reader
    reader = csv.reader(file)
    
    # Skip the header row
    next(reader)
    
    # Insert each row into the database
    for row in reader:
        # Print out the row data for debugging
        print(f'Row data: {row}')
        if len(row) == 4:
            c.execute('''
                INSERT INTO SousVideTimes (id, food_type, temperature, cooking_time)
                VALUES (?, ?, ?, ?)
            ''', row)
        else:
            print(f'Skipping row due to insufficient columns: {row}')

conn.commit()
conn.close()