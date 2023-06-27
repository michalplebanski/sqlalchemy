from sqlalchemy import Table, Column, Date, Float, Integer, Text, MetaData
from sqlalchemy import create_engine

clean_db = create_engine('sqlite:///clean.db')

meta = MetaData()

clean_measure = Table(
    'clean_measure', meta,
    Column('id', Integer, primary_key=True),
    Column('date', Date),
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
print(clean_db.table_names())





