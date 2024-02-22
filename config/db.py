# en config hacemos la conexion a la base de datos


# importamos
from sqlalchemy import create_engine, MetaData
from passw import passw

# creamos el motor para la conexion con la db usando createengine
engine = create_engine(f"mysql+pymysql://root:{passw}@localhost:3306/app_api_motos")

# hacemos la conexion con sqlalchemy, usando metodo .connect()
conn = engine.connect()

# llamamos metadata
meta = MetaData()



