# importamos
from sqlalchemy import create_engine, MetaData

# creamos el motor para la conexion con la db usando createengine
engine = create_engine("mysql+pymysql://root:croke@localhost:3306/app_api_motos")

# llamamos metadata
meta = MetaData()

# hacemos la conexion con sqlalchemy
conn = engine.connect()

