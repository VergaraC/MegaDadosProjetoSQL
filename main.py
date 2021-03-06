from fastapi import FastAPI,HTTPException, Path
from typing import Optional
from pydantic import BaseModel

from typing import List
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
import crud, models, schemas

from database import SessionLocal, engine, Base

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
    try:
        return crud.get_disciplinas(db, skip=skip, limit=limit)
    except IOError as e:
        return {"Resposta": "Não há disciplinas"}
    

@app.get("/disciplinas/{nome}")
async def getDisciplinaByName(nomeQ: str, db: Session = Depends(get_db)):
    try:
        return crud.get_disciplina_por_nome(db, nome = nomeQ)
    except IOError as e:
        raise HTTPException(status_code = 404, detail = "'nome' not found")

@app.post("/disciplinas")
async def createDisciplinas(item: schemas.DisciplinaCreate, db: Session = Depends(get_db)):
    nomes = crud.get_nomes_disciplina(db)
    if item.nome in nomes:
        raise HTTPException(status_code = 400, detail = "'nome' already in use")
    return crud.create_disciplina(db, disciplina = item)

@app.delete("/disciplinas/{nome}")
async def delDisciplina(nome: str,db: Session = Depends(get_db)):
    try:
        return crud.delete_disciplinas(db, nome)
    except IOError as e:
        return {"Resposta": "Não foi possível deletar"}
    
    
@app.get("/disciplinas/get-nomes/")
async def getListaDisciplinas(db: Session = Depends(get_db)):
    try:
        return crud.get_nomes_disciplina(db)
    except IOError as e:
        return {"Resposta": "Não há disciplinas"}

@app.put("/disciplinas/{nome}")
async def updateDisciplina(nome: str , item: schemas.DisciplinaUpdate, db: Session = Depends(get_db)):
    try:
        return crud.update_disciplinas(db,nome,item)
    except IOError as e:
        return {"Resposta": "Não há disciplinas"}


#########################################################################
#########################################################################
############################   NOTA  #################################### 
#########################################################################
#########################################################################

@app.post("/notas")
async def createNotas(nota: schemas.NotaCreate, db: Session = Depends(get_db),  id: int = 0):
    valores = crud.get_notas(db)
    if nota.nome_disciplina in valores:
        raise HTTPException(status_code = 400, detail = "'nota' already in use")
    return crud.create_nota(db, nota = nota,id = id)



@app.delete("/notas/{id}")
async def delNota(db: Session = Depends(get_db), id: int = 0):
    try:
        return crud.delete_nota(db, id = id)
    except IOError as e:
        return {"Resposta": "Não foi possível deletar"}



@app.get("/notas")
async def getNotas(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    try:
        return crud.get_notas(db, skip=skip, limit=limit)
    except IOError as e:
        return {"Resposta": "Não há notas"}


@app.put("/notas/{id}")
async def updateNota(id: int, notaNow: schemas.NotaUpdate, db: Session = Depends(get_db)):
    try:
        return crud.update_nota(db, id, notaNow)
    except IOError as e:
        return {"Resposta": "Não há notas"}
    