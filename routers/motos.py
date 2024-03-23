# en routes las funciones o peticiones http

# importamos
from fastapi import APIRouter, HTTPException
from config.db import conn
from models.motos import motosbd
from schemas.motos import Moto


motos_router = APIRouter()


# funciona ok
@motos_router.get('/')
async def hola():
    try:
        return {'Welcome to the collection' : 'my favorite motorcycles'}
    except Exception as e:
        raise
    
# funciona ok
@motos_router.get("/motos")
async def get_motos():
    try:
        cursor = conn.execute(motosbd.select()).fetchall()
        column_names = [column.name for column in motosbd.columns]
        # convertimos las filas a dict, usando los nombres d las columnas
        motos_list = [dict(zip(column_names, row)) for row in cursor]
        return {'motos_list':motos_list}
    except Exception as e:
        raise

# no me da la moto completa, solo la id
@motos_router.get("/motos/{id}")
async def get_motillo(id: str):
    try:
        result = conn.execute(motosbd.select().where(motosbd.c.id == id)).fetchone()
        resultdict = dict(zip(id, result))
        return {'moto': resultdict}
    except Exception as e:
        if result is None:
            raise HTTPException(status_code=404, detail='no existe')
                # con zip unimos los dos elementos
    
    
# añadir, funciona OK
@motos_router.post('/motos')
async def create_moto(motosbd: Moto):
    # new_moto = {'marca':moto.marca, 'modelo': moto.modelo, 'cilindrada': moto.cilindrada, 'año': moto.año, 'peso':moto.peso}
    new_moto = Moto
    try:
        result = conn.execute(motosbd.insert().values(new_moto))
        conn.commit()
        return result.lastrowid, new_moto
    except Exception as e:
        raise

# borrar, funciona OK
@motos_router.delete("/motos/{id}")
async def delete_moto(id: str):
    try:
        result = conn.execute(motosbd.delete().where(motosbd.c.id == id))
        conn.commit()
        return  'id delete', id
    except Exception as e:
        if result is None:
            raise HTTPException(status_code=404, detail='no existe')
