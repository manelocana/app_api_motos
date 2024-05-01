# aqui voy a separar las funciones de las peticiones, para hacerlo mas facil de leer

from fastapi import HTTPException
from schemas.motos import Moto
from config.db import conn, session
from models.motos import motosbd


# presentacion
def fun_hola():
    try:
        return {'Welcome to the collection of motorcycles':'/docs in path for see documentation'}
    except Exception as e:
        raise HTTPException(status_code=402, detail='error')


# crear moto, sigue batallando haha

'''
def nueva_moto(moto:Moto):
    try:
        #new_moto = {'marca':moto.marca, 'modelo': moto.modelo, 'cilindrada': moto.cilindrada, 'año': moto.año, 'peso':moto.peso}
        new_moto = moto.model_dump()
        result = conn.execute(motosbd.insert().values(new_moto))
        conn.commit()
        return result
    except Exception as e:
        raise #HTTPException(status_code=444, detail='motobd no creada')
'''

def nueva_moto(moto: Moto):
    sesion = session
    try:

        sesion.add(moto)
        sesion.commit()
    except Exception as e:
        sesion.rollback()
        raise #HTTPException(status_code=444, detail='error ...')
    finally:
        sesion.close()
    return moto







# ver motos, get
def see_motos():
    try:
        cursor = conn.execute(motosbd.select()).fetchall()
        column_names = [column.name for column in motosbd.columns]
        motos_list = [dict(zip(column_names, row)) for row in cursor]
        return {'motos list':motos_list}
    except Exception as e:
        raise HTTPException(status_code=500, detail='error al conectar con el servidor')

# ver una moto por id
def find_moto(id: str):
    try:
        result = conn.execute(motosbd.select().where(motosbd.c.id == id)).fetchone()
        # obtenemos los nombres de las tablas
        column_names = [column.name for column in motosbd.columns]
        return dict(zip(column_names, result))
    except Exception as e:
        if result is None:
            raise HTTPException(status_code=404, detail='Moto no encontrada')

# borrar 
def borrar_moto(id:str):
    try:
        result = conn.execute(motosbd.select().where(motosbd.c.id == id)).fetchone()
        # obtenemos los nombres de las tablas
        column_names = [column.name for column in motosbd.columns]
        resultado = dict(zip(column_names, result))
        return {'delete' : resultado}
        resultdel = conn.execute(motosbd.delete().where(motosbd.c.id == id))
        conn.commit()
        return  {'id delete': id}
    except Exception as e:
        if result is None:
            raise HTTPException(status_code=404, detail='no puedes borrarla si no existe')
# INTENTANDO QUE ME DEVUELVA EL OBJETO COMPLETO, NO SOLO LA QUERY QUE LE PIDO


# actualizar moto

def actualizar_moto(self, id, modelo):
    try:
        result = conn.execute(motosbd.select().where(motosbd.c.id==id))

        self.cursor.execute(sql)
        self.connection.commit()
    except Exception as e:
        raise HTTPException(status_code=444, detail='no se ha creado la motillo')
