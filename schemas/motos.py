# y en schemas definimos el tipo de dato que usaremos


from pydantic import BaseModel
from typing import Optional

# cramos la clase, con BaseModel, para la estructura

class Moto(BaseModel):
    id : Optional[str]
    marca: str
    modelo: str
    cilindrada: str
    año: str
    peso: str





'''
class Moto(BaseModel):
    def __init__(self):
        self.id: Optional[str]
        self.marca: str
        self.modelo: str
        self.cilindrada: int
        self.año: int
        self.peso: int
'''

'''
class Motos(Moto):
    def __init__(self, id, marca, modelo, cilindrada, año, peso):
        super(). __init__()
        self.id = Optional[str]
        self.marca = marca
        self.modelo = modelo
        self.cilindrada = cilindrada
        self.año = año
        self.peso = peso

moto1 = Motos(1,"Yamaha", "SR", 125, 1996, 120)
moto2 = Motos(2, "Honda", "CR", 125, 1998, 87.5)

print(moto1.peso)
'''