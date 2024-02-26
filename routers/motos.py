# en routes las funciones o peticiones http

# importamos
from fastapi import APIRouter
from config.db import conn
from models.motos import motosbd
from schemas.motos import Moto
from starlette.status import HTTP_204_NO_CONTENT



motos_router = APIRouter()

@motos_router.get('/')
async def hola():
    return 'Welcome to the collection of my favorite motorcycles'


# funciona ok, pero no devuelve un json...
@motos_router.get("/motos")
async def get_motos():
    result = conn.execute(motosbd.select()).fetchall()
    return str(result)



@motos_router.get("/motos/{id}")
async def get_motillo(id: str):
    result = conn.execute(motosbd.select().where(motosbd.c.id == id))
    return str(result)
    



# añadir, funciona OK
@motos_router.post('/motos')
async def create_moto(moto: Moto):
    new_moto = {'marca':moto.marca, 'modelo': moto.modelo, 'cilindrada': moto.cilindrada, 'año': moto.año, 'peso':moto.peso}
    result = conn.execute(motosbd.insert().values(new_moto))
    conn.commit()
    return result.lastrowid, new_moto

# borrar, funciona OK
@motos_router.delete("/motos/{id}")
async def delete_moto(id: str):
    conn.execute(motosbd.delete().where(motosbd.c.id == id))
    conn.commit()
    return conn(status_code=HTTP_204_NO_CONTENT)


