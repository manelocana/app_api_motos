
# routes=funciones, models=datos, schemas=tipos_de_datos, config=base_datos 

# usamos sql como db. hacemos la conexion con sqlalchemy


#  importamos
from fastapi import FastAPI
from routers.motos import motos_router
from fastapi.staticfiles import StaticFiles
from routers.users import users_router



# iniciamos fastapi
app = FastAPI(tittle="fastapi_motos", 
              description="moto_collection", 
              version="1.0.1")

# incluimos router, donde hago las peticiones
app.include_router(motos_router)
app.include_router(users_router)

# añadimos la ruta staticfiles para las imagenes
app.mount('/static', StaticFiles(directory='static') ,name='static')

