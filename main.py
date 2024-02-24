
# routes=funciones, models=datos, schemas=tipos_de_datos, config=base_datos 

# usamos sql como db. hacemos la conexion con sqlalchemy


#  importamos
from fastapi import FastAPI
from routers.motos import motos_router


# iniciamos fastapi
app = FastAPI(tittle="fastapi_motos", 
              description="moto_collection", 
              version="1.0.1")

app.include_router(motos_router)


