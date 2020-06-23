import sqlite3
import sys
import csv


# Import CSV data to db

# Connecting to database
connection = sqlite3.connect("shootings.db")

# Creat Cursor object
cur = connection.cursor()

# Create db table
cur.execute('''
CREATE TABLE IF NOT EXISTS shootings(

    id INT, name VARCHAR(255), day DATE, manner_of_death VARCHAR(1000),
    armed VARCHAR(15), age INT, gender CHAR(1), race CHAR(1), city VARCHAR(255),
    state CHAR(2), signs_of_mental_illness VARCHAR(255), threat_level VARCHAR(255),
    flee VARCHAR(255), body_camera VARCHAR(255))
            ''')

# # Insert rows from CSV into db
with open("fatal-police-shootings-data.csv") as csvFile:
    reader = csv.DictReader(csvFile)

    # Get column:row data
    for row in reader:
        id = int(row['id'])
        name = row['name']
        day = row['date']
        manner_of_death = row['manner_of_death']
        armed = row['armed']
        age = row['age']
        gender = row['gender']
        race = row['race']
        city = row['city']
        state = row['state']
        signs_of_mental_illness = row['signs_of_mental_illness']
        threat_level = row['threat_level']
        flee = row['flee']
        body_camera = row['body_camera']


        # Insert column:row into db
        cur.execute('''
            INSERT INTO shootings(
            id, name, day, manner_of_death, armed, age, gender, race, city, state,
            signs_of_mental_illness, threat_level, flee, body_camera)
            VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    ''', [id, name, day, manner_of_death, armed, age, gender, race, city, state,
                    signs_of_mental_illness, threat_level, flee, body_camera]
                    )

# Save changes in database. If we skip this, nothing will be saved in the database.
connection.commit()

# Close the connection
connection.close()
