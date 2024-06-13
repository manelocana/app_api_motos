from fastapi import HTTPException
from schemas.users import User
from config.db import conn
from models.users import usersbd



def new_user(user:User):
    try:
        new_user = {'nombre':user.nombre,
                    'email':user.email}
        cursor = conn.execute(usersbd.insert().values(new_user))
        conn.commit()
        return new_user, cursor
    except Exception as e:
        raise HTTPException
    

