# aqui voy a separar las funciones de las peticiones, para hacerlo mas facil de leer

# aqui un crud core, directamente a la base datos sin usar orm


from fastapi import HTTPException
from schemas.motos import Moto
from config.db import conn
from models.motos import motosbd


# presentacion, un json, lo envio en try/except, para ver si falla la peticion, que me devuelva el error
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


# ver motos, get: conexion en bd y que muestre todo con fetchall(), bucle para sacar los nombres de las columnas, 
# unir y convertir en dict, cada linia que recorra el cursor 
def see_motos():
    try:
        cursor = conn.execute(motosbd.select()).fetchall()
        column_names = [column.name for column in motosbd.columns]
        motos_list = [dict(zip(column_names, row)) for row in cursor]
        return {'motos list':motos_list}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# ver una moto por id, conexion a bd haciendo where en id, y fetchone que muestre solo una linea
# sacamos la columna con un bucle
def find_moto(id: str):
    try:
        cursor = conn.execute(motosbd.select().where(motosbd.c.id == id)).fetchone()
        column_names = [column.name for column in motosbd.columns]
        return dict(zip(column_names, cursor))
    except Exception as e:
        if cursor is None:
            raise HTTPException(status_code=404, detail=str(e))


### hay que corregirla....  borrar 
def borrar_moto(id:str):
    try:
        result = conn.execute(motosbd.select().where(motosbd.c.id == id)).fetchone()
        column_names = [column.name for column in motosbd.columns]
        resultado = dict(zip(column_names, result))
        if result:
            conn.execute(motosbd.delete().where(motosbd.c.id == id))
            conn.commit()
        else:
            raise HTTPException(status_code=404, detail='no puedes borrar lo que no está')
        return {'delete' : resultado}
    except Exception as e:
        if result is None:
            raise HTTPException(status_code=404, detail=str(e))


# actualizar moto, le pasamos la id y los parametros a actualizar en formato dict. where en bd por id, condicional para ver si la moto
# existe, conectamos a bd, hacemos update(), y le pasamos los nuevos valores
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
