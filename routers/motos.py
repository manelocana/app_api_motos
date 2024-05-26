# en routes las peticiones http

# importamos
from fastapi import APIRouter, HTTPException
from schemas.motos import Moto
from crud.crud import see_motos, find_moto, borrar_moto, fun_hola, nueva_moto, actualizar_moto
from typing import Dict
from fastapi.responses import JSONResponse





motos_router = APIRouter()


# home, pedimos un get a /
@motos_router.get('/')
async def hola():
    return fun_hola()
    

# ver todas las motos
@motos_router.get('/motos')
async def get_motos():
    return see_motos()


# busqueda del objeto por parametro, en este caso id
@motos_router.get('/motos/{id}')
async def get_motillo(id: str):
    return find_moto(id)
    

# insertar objeto, usando la clase que hicimos en schemas
@motos_router.post('/motos') 
async def create_moto(moto:Moto):
    return nueva_moto(moto)
    

# modificar, importamos Dict de typing, y le pasamos los datos en diccionario
# probamos la peticion y si da error, returnamos un json con jsonresponse
@motos_router.put('/motos/{id}')
async def update_moto(id:str, datos_actualizados:Dict[str,str]):
    try:
        actualizar_moto(id, datos_actualizados)
        return {'message':'se actualizó correctamente'}
    except HTTPException as e:
        return JSONResponse(status_code=e.status_code, content={"detail": e.detail})    


# borrar, igual que el get por id, pero pasandole la funcion de borrar
@motos_router.delete('/motos/{id}')
async def delete_moto(id: str):
    return borrar_moto(id)
