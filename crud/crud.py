# aqui voy a separar las funciones de las peticiones, para hacerlo mas facil de leer

# aqui un crud core, directamente a la base datos sin usar orm


from fastapi import HTTPException
from schemas.motos import Moto
from config.db import conn
from models.motos import motosbd


# presentacion
def fun_hola():
    try:
        return {'Welcome to the collection of motorcycles':'type /docs in path for see documentation'}
    except Exception as e:
        raise HTTPException(status_code=402, detail=str(e))


# crear nueva moto, creamos una instancia de la clase Moto, le pasamos los datos y hacemos un cursor donde queremos insertar, 
# un commit para escribirlo en la bd, le pedimos que returne el nuevo objeto y el cursor
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
        raise HTTPException(status_code=444, detail=str(e))


# ver motos, get
def see_motos():
    try:
        cursor = conn.execute(motosbd.select()).fetchall()
        column_names = [column.name for column in motosbd.columns]
        motos_list = [dict(zip(column_names, row)) for row in cursor]
        return {'motos list':motos_list}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# ver una moto por id
def find_moto(id: str):
    try:
        cursor = conn.execute(motosbd.select().where(motosbd.c.id == id)).fetchone()
        column_names = [column.name for column in motosbd.columns]
        return dict(zip(column_names, cursor))
    except Exception as e:
        if cursor is None:
            raise HTTPException(status_code=404, detail=str(e))


# borrar 
def borrar_moto(id:str):
    try:
        result = conn.execute(motosbd.select().where(motosbd.c.id == id)).fetchone()
        column_names = [column.name for column in motosbd.columns]
        resultado = dict(zip(column_names, result))
        return {'delete' : resultado}
    except Exception as e:
        if result is None:
            raise HTTPException(status_code=404, detail=str(e))


# actualizar moto
def actualizar_moto(id:str, datos_actualizados: dict):
    try:
        cursor = conn.execute(motosbd.select().where(motosbd.c.id==id))
        moto_existente = cursor.fetchone()
        if moto_existente:   
            conn.execute(motosbd.update().where(motosbd.c.id == id).values(datos_actualizados))
            conn.commit()
        else:
            raise HTTPException(status_code=404, detail='la moto no existe')
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
