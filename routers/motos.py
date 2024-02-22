# en routes las funciones o peticiones http

# importamos
from fastapi import APIRouter
from config.db import conn
from models.motos import motos
from schemas.motos import Moto

motos = APIRouter()

@motos.get('/')
async def hola():
    return 'Welcome to the collection of my favorite motorcycles'

@motos.get('/motos1')
async def get_motos():
    return conn.execute(motos.select()).fetchall()

@motos.post('/motos')
async def create_moto(moto: Moto):
    print(moto)
    return




