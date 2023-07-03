from sqlalchemy import Table, Column, Date, Float, Integer, Text, MetaData
from sqlalchemy import create_engine
import csv

clean_db = create_engine('sqlite:///clean.db')

meta = MetaData()

clean_measure = Table(
    'clean_measure', meta,
    Column('id', Integer, primary_key=True),
    Column('station', Text),
    Column('date', Date),
    Column('precib', Float),
    Column('tobs', Text),
)

clean_stations = Table(
    'clean_stations', meta,
    Column('id', Integer, primary_key=True),
    Column('station', Text),
    Column('latitude', Float),
    Column('longitude', Float),
    Column('elevation', Float),
    Column('name', Text),
    Column('country', Text),
    Column('state', Text),
)

meta.create_all(clean_db)

#insert data to database
#clean_measure

conn = clean_db.connect()

with open('clean_measure.csv', 'r') as clean_measure_file:
    csvreader = csv.reader(clean_measure_file)
    
    # Skip header if exists
    next(csvreader)
    
    # Iterate through all rows in CSV file and add them to database
    id = 0
    for row in csvreader:
        id += 1
        station = row[0]
        date = row[1]
        precib = float(row[2])
        tobs = int(row[3])

        conn.execute('INSERT INTO clean_measure VALUES (?, ?, ?, ?, ?)', (id, station, date, precib, tobs))

#clean_station

with open('clean_stations.csv', 'r') as clean_stations_file:
    csvreader = csv.reader(clean_stations_file)
    
    # Skip header if exists
    next(csvreader)
    
    # Iterate through all rows in CSV file and add them to database
    id = 0
    for row in csvreader:
        id += 1
        station = row[0]
        latitude = float(row[1])
        longitude = float(row[2])
        elevation = float(row[3])
        name = row[4]
        country = row[5]
        state = row[6]

        conn.execute('INSERT INTO clean_stations VALUES (?, ?, ?, ?, ?, ?, ?, ?)', (id, station, latitude, longitude, elevation, name, country, state))

print(conn.execute("SELECT * FROM clean_measure LIMIT 5").fetchall())
print(conn.execute("SELECT * FROM clean_stations LIMIT 5").fetchall()) 

conn.close()