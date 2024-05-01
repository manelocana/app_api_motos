# en models definimos los modelos de las tablas

from sqlalchemy import Table, Column
from config.db import meta, engine
from sqlalchemy.sql.sqltypes import String


# creamos la tabla 
motosbd = Table('motos1', meta, Column('id', String, primary_key=True, nullable=True), 
              Column('marca', String(255)),
              Column('modelo', String(255)), 
              Column('cilindrada', String(255)), 
              Column('año', String(255)),
              Column('peso', String(255)))

# una vez conectado a sql (usando engine), crea la tabla usando meta
meta.create_all(engine)

