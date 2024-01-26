# importamos
from fastapi import FastAPI
from pydantic import BaseModel


# cramos la clase, con BaseModel, para la estructura
class Moto(BaseModel):
    id: str
    marca: str
    modelo: str
    año: int
    cilindrada: int
    peso: int

