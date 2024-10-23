import unittest
import sqlite3
import os
from import_data import create_connection, create_table, insert_data

class TestImportData(unittest.TestCase):

    def setUp(self):
        """Set up a temporary database and CSV file for testing."""
        self.database = "test_sous_vide.db"
        self.csv_file = "test_sous_vide.csv"
        self.conn = create_connection(self.database)
        create_table(self.conn)
        with open(self.csv_file, 'w') as file:
            file.write("id,food_type,temperature,cooking_time\n")
            file.write("1,Test Food,85,30 minutes\n")

    def tearDown(self):
        """Clean up the temporary database and CSV file after testing."""
        self.conn.close()
        os.remove(self.database)
        os.remove(self.csv_file)

    def test_create_connection(self):
        """Test creating a database connection."""
        conn = create_connection(self.database)
        self.assertIsNotNone(conn)
        conn.close()

    def test_create_table(self):
        """Test creating the SousVideTimes table."""
        create_table(self.conn)
        c = self.conn.cursor()
        c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='SousVideTimes'")
        table = c.fetchone()
        self.assertIsNotNone(table)

    def test_insert_data(self):
        """Test inserting data from the CSV file into the SousVideTimes table."""
        insert_data(self.conn, self.csv_file)
        c = self.conn.cursor()
        c.execute("SELECT * FROM SousVideTimes")
        rows = c.fetchall()
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0][1], "Test Food")

if __name__ == '__main__':
    unittest.main()
