
# routes=funciones, models=datos, schemas=tipos_de_datos, config=base_datos 

# usamos sql como db. hacemos la conexion con sqlalchemy



from fastapi import FastAPI
from routers import motos



app = FastAPI(tittle="fastapi_motos", 
              description="moto_collection", 
              version="1.0.1")


@app.get("/")
async def get():
    return "primer: get"

@app.get("/motos")
async def get():
    return "get en motos"

