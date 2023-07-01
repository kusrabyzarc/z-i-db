# Import required modules
import csv
import sqlite3
import sys
import os

# Deleting the old database
# if exists
if os.path.exists('dump.db'):
    os.remove('dump.db')

maxInt = sys.maxsize

while True:
    # decrease the maxInt value by factor 2
    # as long as the OverflowError occurs.

    try:
        csv.field_size_limit(maxInt)
        break
    except OverflowError:
        maxInt = int(maxInt/2)

# Connecting to the database
connection = sqlite3.connect('dump.db')

# Creating a cursor object to execute
# SQL queries on a database table
cursor = connection.cursor()

# Table Definition
create_table = '''CREATE TABLE write(
				ip TEXT,
				url TEXT,
				page TEXT,
				law TEXT,
				cause TEXT,
				date TEXT);
				'''

# Creating the table into our
# database
cursor.execute(create_table)

# Opening the dump.csv file
file = open('dump.csv')

# Reading the contents of the
# dump.csv file

contents = csv.reader(file, delimiter=';')

# SQL query to insert data into the
# write table
insert_records = "INSERT INTO write (ip, url, page, law, cause, date) VALUES(?, ?, ?, ?, ?, ?)"

# Importing the contents of the file
# into our table
cursor.executemany(insert_records, contents)

# SQL query to retrieve all data from
# the table To verify that the
# data of the csv file has been successfully
# inserted into the table
select_all = "SELECT * FROM write"
rows = cursor.execute(select_all).fetchall()

# Committing the changes
connection.commit()

# closing the database connection
connection.close()
