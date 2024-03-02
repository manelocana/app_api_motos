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
    return {'Welcome to the collection' : 'my favorite motorcycles'}

# funciona ok
@motos_router.get("/motos")
async def get_motos():
    # conectamos a bd, hacemos select * en bd, (fetchall==*)
    cursor = conn.execute(motosbd.select()).fetchall()
    # sacamos los nombres de las columnas
    column_names = [column.name for column in motosbd.columns]
    # convertimos las filas a dict, usando los nombres d las columnas
    motos_list = [dict(zip(column_names, row)) for row in cursor]
    return {'motos_list':motos_list}

# funciona ok
@motos_router.get("/motos/{id}")
async def get_motillo(id: str):
    result = conn.execute(motosbd.select().where(motosbd.c.id == id)).fetchone()
    if result is None:
        raise HTTPException(status_code=404, detail='no existe')
                # con zip unimos los dos elementos
    return dict(zip(id, result))
    
# añadir, funciona OK
@motos_router.post('/motos')
async def create_moto(motosbd: Moto):
    # new_moto = {'marca':moto.marca, 'modelo': moto.modelo, 'cilindrada': moto.cilindrada, 'año': moto.año, 'peso':moto.peso}
    new_moto = Moto
    result = conn.execute(motosbd.insert().values(new_moto))
    conn.commit()
    return result.lastrowid, new_moto

# borrar, funciona OK
@motos_router.delete("/motos/{id}")
async def delete_moto(id: str):
    result = conn.execute(motosbd.delete().where(motosbd.c.id == id))
    conn.commit()
    if result is None:
        raise HTTPException(status_code=404, detail='no existe')
    return  'id delete', id