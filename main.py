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
