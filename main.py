from fastapi import FastAPI,HTTPException, Path
from typing import Optional
from pydantic import BaseModel

from typing import List
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

"""
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
"""

app = FastAPI()

@app.get("/")
async def Home():
    return {"Mensagem":"Bem vindo!"}


@app.get("/disciplinas")
async def getDisciplinas(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    disciplinas = crud.get_disciplinas(db, skip=skip, limit=limit)
    if disciplinas is None:
        return {"Resposta": "Não há disciplinas"}
    else:
        return disciplinas
    

@app.get("/disciplinas/{nome}")
async def getDisciplinaByName(nomeQ: str, db: Session = Depends(get_db)):
    
    disciplinas = crud.get_disciplina_por_nome(db, nome = nomeQ)
    raise HTTPException(status_code = 404, detail = "'nome' not found")
    return disciplinas
    
@app.post("/disciplinas")
async def createDisciplinas(item: Disciplina ):
    for disciplina in  disciplinas:
        if disciplina.nome == item.nome:
            raise HTTPException(status_code = 400, detail = "'nome' already in use")
    disciplinas.append(item)
    return item

@app.delete("/disciplinas/{nome}")
async def delDisciplina(nome: str = Path(None, title="Nome", description="Nome da disciplina")):
    for disciplina in disciplinas:
        if disciplina.nome == nome:
            disciplinas.pop(disciplinas.index(disciplina))
            return {"Success":"Disciplina deleted"}
    raise HTTPException(status_code = 404, detail = "'nome' not found")

@app.get("/disciplinas/get-nomes/")
async def getListaDisciplinas():
    list_disciplinas_nomes = []
    for disciplina in disciplinas:
        list_disciplinas_nomes.append(disciplina.nome)
    return list_disciplinas_nomes

@app.put("/disciplinas/{nome}")
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
