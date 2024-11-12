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



# editar mensajes
@app.put("/mensajes/{mensaje_id}", response_model=Mensaje)
def editar_mensaje(msj_id: int, nuevo_mensaje: Mensaje):
    for index, msj in enumerate(mensajes_db):
        if msj.id == msj_id:
            nuevo_mensaje.id = msj_id
            mensajes_db[index] = nuevo_mensaje
            return nuevo_mensaje
    raise HTTPException(status_code=404, detail="Mensaje no encontrado.")




# eliminar mensaje
@app.delete("/mensajes/{mensaje_id}", response_model=dict)

def eliminar_mensaje(msj_id: int):
    for index, mensaje in enumerate(mensajes_db):
        if mensaje.id == msj_id:
            del mensajes_db[index]
            return {"detail": "Mensaje eliminado"}
    raise HTTPException(status_code=404, detail="Mensaje no encontrado.") 
