# en routes las funciones o peticiones http

# importamos
from fastapi import APIRouter
from config.db import conn
from models.motos import motos
from schemas.motos import Moto

motos_router = APIRouter()

@motos_router.get('/')
async def hola():
    return 'Welcome to the collection of my favorite motorcycles'


@motos_router.get('/motos2')
async def get_motos():
    getmoto = conn.execute(motos.select())
    return getmoto

@motos_router.get('/motos1')
async def get_motos():
    return conn.execute(motos.select()).fetchall()

@motos_router.get("/motos3")
async def get_motos():
    result = conn.execute(motos_router.select())
    conn.commit()
    return result



@motos_router.post('/motos')
async def create_moto(moto: Moto):
    new_moto = {'marca':moto.marca, 'modelo': moto.modelo, 'cilindrada': moto.cilindrada, 'año': moto.año, 'peso':moto.peso}
    print(new_moto)
    result = conn.execute(motos.insert().values(new_moto))
    conn.commit()
    print(result)
    return moto.id, new_moto




