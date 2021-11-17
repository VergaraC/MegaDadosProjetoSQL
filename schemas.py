from typing import List, Optional
from pydantic import BaseModel


class DisciplinaGet(BaseModel):
    id: int
    nome: str
    professor: Optional[str] = None
    comentario: str
    class Config:
        orm_mode = True
class DisciplinaDelete(BaseModel):
    id: int
    nome: str
    professor: Optional[str] = None
    comentario: str

    class Config:
        orm_mode = True
class DisciplinaCreate(BaseModel):
    id : int
    nome: str
    professor: Optional[str] = None
    comentario: str

class DisciplinaUpdate(BaseModel):
    id : Optional[int] = None
    nome: Optional[str] = None
    professor: Optional[str] = None
    comentario: Optional[str] = None

class NotaGet(BaseModel):

    id: int
    id_disciplina: int
    nome_disciplina: str
    nota: float

class NotaDelete(BaseModel):
    id: int
    id_disciplina: int
    nome_disciplina: str
    nota: float

class NotaCreate(BaseModel):
    id: int
    id_disciplina: int
    nome_disciplina: str
    nota: float

class NotaUpdate(BaseModel):
    id : Optional[int] = None
    id_disciplina: Optional[str] = None
    nome_disciplina: Optional[str] = None
    nota: Optional[float] = None
