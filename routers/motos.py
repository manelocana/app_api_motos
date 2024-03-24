# en routes las funciones o peticiones http

# importamos
from fastapi import APIRouter, HTTPException
from config.db import conn
from models.motos import motosbd
from schemas.motos import Moto




motos_router = APIRouter()


# home, bienvenida
@motos_router.get('/')
async def hola():
    try:
        return {'Welcome to the collection' : 'my favorite motorcycles'}
    except Exception as e:
        raise

# ver todas las motos
@motos_router.get("/motos")
async def get_motos():
    try:
        cursor = conn.execute(motosbd.select()).fetchall()
        column_names = [column.name for column in motosbd.columns]
        # convertimos las filas a dict, usando los nombres d las columnas
        motos_list = [dict(zip(column_names, row)) for row in cursor]
        return {'motos_list':motos_list}
    except Exception as e:
        raise HTTPException(status_code=500, detail='error al conectar con el servidor')


# busqueda de moto por id
@motos_router.get("/motos/{id}")
async def get_motillo(id: str):
    try:
        result = conn.execute(motosbd.select().where(motosbd.c.id == id)).fetchone()
        # obtenemos los nombres de las tablas
        column_names = [column.name for column in motosbd.columns]
        return dict(zip(column_names, result))
    except Exception as e:
        if result is None:
            raise HTTPException(status_code=404, detail='Moto no encontrada')

    
# añadir
@motos_router.post('/motos')
async def create_moto(motosbd: Moto):
    new_moto = Moto
    try:
        result = conn.execute(motosbd.insert().values(new_moto))
        conn.commit()
        return result.lastrowid, new_moto
    except Exception as e:
        raise HTTPException(status_code=404, detail='moto no creada')

# borrar
@motos_router.delete("/motos/{id}")
async def delete_moto(id: str):
    try:
        result = conn.execute(motosbd.delete().where(motosbd.c.id == id))
        conn.commit()
        return  {'id delete': id}
    except Exception as e:
        if result is None:
            raise HTTPException(status_code=404, detail='no puedes borrarla si no existe')
