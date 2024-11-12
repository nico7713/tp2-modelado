# uvicorn main:app --reload

from typing import Optional
from pydantic import BaseModel, EmailStr


class Mensaje(BaseModel):
    id: Optional[int] = None
    usuario: str
    mensaje: str


# API
from fastapi import FastAPI, HTTPException

app = FastAPI()

# base de datos
mensajes_db = []


# mandar mensaje
@app.post("/mensajes/", response_model=Mensaje) 

def mandar_mensaje(msj:Mensaje):
    msj.id = len(mensajes_db) + 1
    mensajes_db.append(msj)
    return msj



