# importamos
from fastapi import APIRouter
from pydantic import BaseModel


motos = APIRouter()

# cramos la clase, con BaseModel, para la estructura


class Moto(BaseModel):
    def __init__(self):
        self.id: int
        self.marca: str
        self.modelo: str
        self.cilindrada: int
        self.año: int
        self.peso: int



class Motos(Moto):
    def __init__(self, id, marca, modelo, cilindrada, año, peso):
        super(). __init__()
        self.id = int
        self.marca = marca
        self.modelo = modelo
        self.cilindrada = cilindrada
        self.año = año
        self.peso = peso


moto1 = Motos(1,"Yamaha", "SR", 125, 1996, 120)

moto2 = Motos(2, "Honda", "CR", 125, 1998, 87.5)

print(moto1.peso)


