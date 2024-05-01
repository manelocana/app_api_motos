# en config hacemos la conexion a la base de datos


# importamos
from sqlalchemy import create_engine, MetaData
from config.passw import passw



# sessionmaker prueba
#from sqlalchemy.orm import sessionmaker



# creamos el motor para la conexion con la db usando createengine
engine = create_engine(f'mysql+pymysql://root:{passw}@localhost:3306/app_api_motos')

# hacemos la conexion con sqlalchemy, usando metodo .connect() (conexion directa a la basededatos)
conn = engine.connect()

# llamamos metadata para crear la tabla
meta = MetaData()



# conectamos mediante sqlalcyhemy.orm , para una conexion mas segura con la base de datos
# sessionmaker prueba (fabrica sessiones)
#Session = sessionmaker(bind=engine)

# crear una session en la funcion
#session = Session()

