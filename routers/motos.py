# en routes las peticiones http

# importamos
from fastapi import APIRouter
from schemas.motos import Moto
from crud.crud import see_motos, find_moto, borrar_moto, fun_hola, nueva_moto, actualizar_moto




motos_router = APIRouter()


# home, hola
@motos_router.get('/')
async def hola():
    return fun_hola()
    

# ver todas las motos
@motos_router.get('/motos')
async def get_motos():
    return see_motos()


# busqueda de motobd por id
@motos_router.get('/motos/{id}')
async def get_motillo(id: str):
    return find_moto(id)
    

# insertar 
@motos_router.post('/motos') 
async def create_moto(moto:Moto):
    return nueva_moto(moto)
    
   
# modificar
@motos_router.put('/motos/{id}')
async def update_moto(id:str, datos_actualizados):
    return actualizar_moto(id)


# borrar
@motos_router.delete('/motos/{id}')
async def delete_moto(id: str):
    return borrar_moto(id)
