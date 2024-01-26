
# routes=funciones, models=datos, schemas=tipos_de_datos, config=base_datos 

from fastapi import FastAPI

app = FastAPI(tittle="fastapi_motos", 
              description="moto_collection", 
              version="1.0.1")


@app.get("/")
async def get():
    return "primer: get"

@app.get("/")
async def get():
    return "primer get"

@app.get("/")
async def get():
    return "primer get"

@app.get("/")
async def get():
    return "primer get"