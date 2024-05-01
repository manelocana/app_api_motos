# y en schemas definimos el tipo de dato que usaremos


from pydantic import BaseModel
#from typing import Optional


# cramos la clase, con BaseModel, para la estructura

class Moto(BaseModel):
    id : str |None
    #id : Optional[str]
    marca: str
    modelo: str
    cilindrada: str
    año: str
    peso: str


