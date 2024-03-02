# y en schemas definimos el tipo de dato que usaremos


from pydantic import BaseModel


# cramos la clase, con BaseModel, para la estructura

class Moto(BaseModel):
    id : str |None
    marca: str
    modelo: str
    cilindrada: str
    año: str
    peso: str


