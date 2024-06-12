from pydantic import BaseModel
from typing import Optional



class User(BaseModel):
    id:Optional[str]
    nombre:str
    email:str
    contraseña:str
    