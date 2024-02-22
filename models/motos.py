# en models definimos los modelos de las tablas

from sqlalchemy import Table, Column
from config.db import meta, engine
from sqlalchemy.sql.sqltypes import Integer, String


# creamos la tabla 
motos = Table('motos1', meta, Column('id', String, primary_key=True), 
              Column('marca', String(255)),
              Column('modelo', String(255)), 
              Column('cilindrada', Integer), 
              Column('año', Integer),
              Column('peso', Integer))

# una vez conectado a sql (usando engine), crea la tabla usando meta
meta.create_all(engine)

