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


# buscar mensaje por id
@app.get("/mensajes/{mensaje_id}", response_model=Mensaje)

def obtener_mensaje(msj_id : int):
    for msj in mensajes_db:
        if msj.id == msj_id:
            return msj
    raise HTTPException(status_code=404, detail="Mensaje no encontrado.")
    

# mostrar todos los mensajes
@app.get("/mensajes/", response_model=list[Mensaje])

def mostrar_mensajes():
    return mensajes_db
