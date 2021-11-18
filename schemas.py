from typing import List, Optional
from pydantic import BaseModel


class DisciplinaGet(BaseModel):
    nome: str
    professor: Optional[str] = None
    comentario: str
    class Config:
        orm_mode = True
class DisciplinaDelete(BaseModel):
    nome: str
    professor: Optional[str] = None
    comentario: str

    class Config:
        orm_mode = True
class DisciplinaCreate(BaseModel):
    nome: str
    professor: Optional[str] = None
    comentario: str

class DisciplinaUpdate(BaseModel):
    nome: Optional[str] = None
    professor: Optional[str] = None
    comentario: Optional[str] = None

class NotaGet(BaseModel):
    id: int
    nome_disciplina: str
    nota: float

class NotaDelete(BaseModel):
    id: int
    nome_disciplina: str
    nota: float

class NotaCreate(BaseModel):
    id: int
    nome_disciplina: str
    nota: float

class NotaUpdate(BaseModel):
    id : Optional[int] = None
    nome_disciplina: Optional[str] = None
    nota: Optional[float] = None
