from sqlalchemy import Table, Column
from config.db import engine, meta
from sqlalchemy.sql.sqltypes import String



usersbd = Table('users', meta, 
                Column('id', String(255), primary_key=True, nullable=True),
                Column('name', String(255)),
                Column('email', String(255)))


meta.create_all(engine)

