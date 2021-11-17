from fastapi import FastAPI,HTTPException, Path
from typing import Optional
from pydantic import BaseModel

from os import name
from fastapi import FastAPI,status,HTTPException, APIRouter,Depends

from typing import Optional, List
from pydantic import BaseModel
import uvicorn

from src.model.subject import Subject
from src.crud.utils import ExistenceException, NonExistenceException
from src.schema.subject import SubjectInDB, SubjectOutDB,SubjectCreate,SubjectUpdate
from src.schema.note import NoteInDB, NoteOutDB,NoteCreate,NoteUpdate
from src.database.database import Base, engine,SessionLocal
from src.crud.subject import get_all_subjects,get_subject,create_subject
from sqlalchemy.orm import Session


class Disciplina(BaseModel):
    nome: str
    professor: Optional[str] = None
    comentario: str

class Nota(BaseModel):
    materia: str
    nota: float

ex_d = Disciplina(nome="Megadados",professor="Ayres",comentario="Entrega para 8/11")
ex_n = Nota(materia="Megadados",nota=10.0)

disciplinas = [ex_d]
notas = [ex_n]


appDisciplinas = FastAPI()

@appDisciplinas.get("/")
async def Home():
    return {"Mensagem":"Bem vindo!"}

@appDisciplinas.get("/disciplinas")
async def getDisciplinas():
    return disciplinas

@appDisciplinas.get("/disciplinas/{nome}")
async def getDisciplinaByName(nome: str = Path(None, title="Nome", description="Nome da disciplina")):
    for disciplina in disciplinas:
        if disciplina.nome == nome:
            return disciplina
    raise HTTPException(status_code = 404, detail = "'nome' not found")

@appDisciplinas.post("/disciplinas")
async def createDisciplinas(item: Disciplina ):
    for disciplina in  disciplinas:
        if disciplina.nome == item.nome:
            raise HTTPException(status_code = 400, detail = "'nome' already in use")
    disciplinas.append(item)
    return item

@appDisciplinas.delete("/disciplinas/{nome}")
async def delDisciplina(nome: str = Path(None, title="Nome", description="Nome da disciplina")):
    for disciplina in disciplinas:
        if disciplina.nome == nome:
            disciplinas.pop(disciplinas.index(disciplina))
            return {"Success":"Disciplina deleted"}
    raise HTTPException(status_code = 404, detail = "'nome' not found")

@appDisciplinas.get("/disciplinas/get-nomes/")
async def getListaDisciplinas():
    list_disciplinas_nomes = []
    for disciplina in disciplinas:
        list_disciplinas_nomes.append(disciplina.nome)
    return list_disciplinas_nomes

@appDisciplinas.put("/disciplinas/{nome}")
async def updateDisciplina(nome: str , item: Disciplina):
    idx = 0
    for disciplina in disciplinas:
        if disciplina.nome == nome:
            disciplinas[idx] = item
            return  disciplinas[idx]
        idx += 1
    raise HTTPException(status_code = 404, detail = "'nome' not found")

#########################################################################
############################   Funções  ################################# 

def getLastId(notas):
    if notas:
        ultima_nota = notas[-1]
        return ultima_nota["id"]
    return 0

#########################################################################
#########################################################################

appNotas = FastAPI()


@app.post("/notas")
async def createNotas(item: Nota):   
    for d in disciplinas:
        if d.nome == item.materia:
            new = item.dict()
            ultimo_id = getLastId(notas)
            new["id"] = ultimo_id+1
            notas.append(new)
            return new
    raise HTTPException(status_code = 404, detail = "'disciplina' not found")

@app.delete("/notas/{id}")
async def delNota(id: int = Path(None, title="Id", description="Id Nota")):
    for nota in notas:
        if nota["id"] == id:
            notas.pop(notas.index(nota))
            return {"message":"nota has been deleted"}
    raise HTTPException(status_code = 404, detail = "'nota id' not found")

@app.get("/notas")
async def getNotas():
    return notas

@app.put("/notas/{id}")
async def updateNota(item: Nota, id: int):
    idx = 0
    for nota in notas:
        if nota["id"] == id:
            for d in disciplinas:
                if d.nome == item.materia:
                    update = item.dict()
                    update["id"] = id
                    notas[idx] = update
                    return notas[idx]
            raise HTTPException(status_code = 404, detail="'disciplina' not found")
        idx += 1
    raise HTTPException(status_code = 404, detail = "'nota id' not found")


app.include_router(router_Note, prefix="/Note",tags=["Notes"])


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
