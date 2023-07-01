# Import required modules
import csv
import sqlite3
import sys
import os

def log(message) -> None:
    print(f'[CONVERTER] {message}' + '.' * message[-1] != '.')

# Deleting the old database
# if exists
if os.path.exists('dump.db'):
    log('Found old database. Deleting...')
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
log('Connected to dump.db')

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
log('Created table')

# Opening the dump.csv file
file = open('dump.csv')

# Reading the contents of the
# dump.csv file

contents = csv.reader(file, delimiter=';')
log('dump.csv parsed')

# SQL query to insert data into the
# write table
insert_records = "INSERT INTO write (ip, url, page, law, cause, date) VALUES(?, ?, ?, ?, ?, ?)"

# Importing the contents of the file
# into our table
log('Inserting data into database...')
cursor.executemany(insert_records, contents)
log('Data inserted.')

# Committing the changes
log('Commiting changes...')
connection.commit()
log('Commited.')

# closing the database connection
connection.close()
log('Connection closed')

while True:
    ans = input('Do you want to delete dump.csv? [Y/n]: ').lower()
    if ans == 'y':
        log('Deleting dump.csv...')
        os.remove('dump.csv')
        break
    elif ans == 'n': break
