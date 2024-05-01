# aqui voy a separar las funciones de las peticiones, para hacerlo mas facil de leer


# aqui un crud core, directamente a la base datos sin usar orm


from fastapi import HTTPException
from schemas.motos import Moto
from config.db import conn
from models.motos import motosbd


# presentacion
def fun_hola():
    try:
        return {'Welcome to the collection of motorcycles':'/docs in path for see documentation'}
    except Exception as e:
        raise HTTPException(status_code=402, detail='error')


# crear nueva moto
def nueva_moto(moto:Moto):
    try:
        new_moto = {'marca':moto.marca, 
                    'modelo': moto.modelo, 
                    'cilindrada': moto.cilindrada, 
                    'año': moto.año, 
                    'peso':moto.peso}
        cursor = conn.execute(motosbd.insert().values(new_moto))
        conn.commit()
        return new_moto, cursor
    except Exception as e:
        raise #HTTPException(status_code=444, detail='motobd no creada')


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
        cursor = conn.execute(motosbd.select().where(motosbd.c.id == id)).fetchone()
        # obtenemos los nombres de las tablas
        column_names = [column.name for column in motosbd.columns]
        return dict(zip(column_names, cursor))
    except Exception as e:
        if cursor is None:
            raise HTTPException(status_code=404, detail='Moto no encontrada')


# borrar 
def borrar_moto(id:str):
    try:
        result = conn.execute(motosbd.select().where(motosbd.c.id == id)).fetchone()
        # obtenemos los nombres de las tablas
        column_names = [column.name for column in motosbd.columns]
        resultado = dict(zip(column_names, result))
        return {'delete' : resultado}
    except Exception as e:
        if result is None:
            raise HTTPException(status_code=404, detail='no puedes borrarla si no existe')


# actualizar moto
'''
def actualizar_moto(self, id, modelo):
    try:
        result = conn.execute(motosbd.select().where(motosbd.c.id==id))

        self.cursor.execute(sql)
        self.connection.commit()
    except Exception as e:
        raise HTTPException(status_code=444, detail='no se ha creado la motillo')
'''