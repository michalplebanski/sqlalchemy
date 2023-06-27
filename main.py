from sqlalchemy import Table, Column, Date, Float, Integer, Text, MetaData
from sqlalchemy import create_engine


clean_db = create_engine('sqlite:///clean.db')

meta = MetaData()

clean_measure = Table(
    'clean_measure', meta,
    Column('id', Integer, primary_key=True),
    Column('station', Text),
    Column('date', Text),
    Column('precib', Float),
    Column('tobs', Text)
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
    Column('state', Text)
)

meta.create_all(clean_db)

#insert data to database
#clean_measure

ins_measure = clean_measure.insert()
conn = clean_db.connect()
conn.execute(ins_measure, [
   {'station': 'USC00519397', 'date': '2010-01-01', 'precib': '0.08', 'tobs': '65'},
   {'station': 'USC00519397', 'date': '2010-01-02', 'precib': '0.0', 'tobs': '63'},
   {'station': 'USC00519397', 'date': '2010-01-03', 'precib': '0.0', 'tobs': '74'},
   {'station': 'USC00519397', 'date': '2010-01-04', 'precib': '0.0', 'tobs': '76'},
   {'station': 'USC00519397', 'date': '2010-01-06', 'precib': '0.0', 'tobs': '73'},
   {'station': 'USC00519397', 'date': '2010-01-07', 'precib': '0.06', 'tobs': '70'},
   {'station': 'USC00519397', 'date': '2010-01-09', 'precib': '0.0', 'tobs': '68'},
   {'station': 'USC00519397', 'date': '2010-01-10', 'precib': '0.0', 'tobs': '54'}
])

#clean_station

ins_stations = clean_stations.insert()
conn = clean_db.connect()
conn.execute(ins_stations, [
   {'station': 'USC00519397', 'latitude': '21.2716', 'longitude': '-157.8168', 'elevation': '3.0', 'name': 'WAIKIKI 717.2', 'country': 'US', 'state': 'HI'},
   {'station': 'USC00513117', 'latitude': '21.4234', 'longitude': '-157.8015', 'elevation': '14.6', 'name': 'KANEOHE 838.1', 'country': 'US', 'state': 'HI'},
   {'station': 'USC00514830', 'latitude': '21.5213', 'longitude': '-157.8374', 'elevation': '7.0', 'name': 'KUALOA RANCH HEADQUARTERS 886.9', 'country': 'US', 'state': 'HI'},
   {'station': 'USC00517948', 'latitude': '21.3934', 'longitude': '-157.9751', 'elevation': '11.9', 'name': 'PEARL CITY', 'country': 'US', 'state': 'HI'},
   {'station': 'USC00518838', 'latitude': '21.4992', 'longitude': '-158.0111', 'elevation': '306.6', 'name': 'UPPER WAHIAWA 874.3', 'country': 'US', 'state': 'HI'},
   {'station': 'USC00519523', 'latitude': '21.33556', 'longitude': '-157.71139', 'elevation': '19.5', 'name': 'WAIMANALO EXPERIMENTAL FARM', 'country': 'US', 'state': 'HI'},
   {'station': 'USC00519281', 'latitude': '21.45167', 'longitude': '-157.84888999999998', 'elevation': '32.9', 'name': 'WAIHEE 837.5', 'country': 'US', 'state': 'HI'},
   {'station': 'USC00511918', 'latitude': '21.3152', 'longitude': '-157.9992', 'elevation': '0.9', 'name': 'HONOLULU OBSERVATORY 702.2', 'country': 'US', 'state': 'HI'},
   {'station': 'USC00516128', 'latitude': '21.3331', 'longitude': '-157.8025', 'elevation': '152.4', 'name': 'MANOA LYON ARBO 785.2', 'country': 'US', 'state': 'HI'}
])

print(conn.execute("SELECT * FROM clean_measure LIMIT 5").fetchall())
print(conn.execute("SELECT * FROM clean_stations LIMIT 5").fetchall())


