from sqlalchemy.orm import Session
from . import models, schemas

def get_nomes_disciplina(db: Session):
    return db.query(models.Disciplina.nome).all()

def get_disciplina_por_nome(db: Session, nome: str):
    return db.query(models.Disciplina).filter(models.Disciplina.nome == nome).first()

def get_disciplinas(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Disciplina).offset(skip).limit(limit).all()

def create_disciplina(db: Session, disciplina: schemas.DisciplinaCreate):

    db_disciplina = models.Disciplina(**disciplina.dict())

    db.add(db_disciplina)

    db.commit()

    db.refresh(db_disciplina)

    return db_disciplina

def update_disciplinas(db: Session, nome: str, disciplina: models.Disciplina):
    db.query(models.Disciplina).filter(models.Disciplina.nome == nome).update({models.Disciplina.nome: disciplina.nome, models.Disciplina.professor: disciplina.professor, models.Disciplina.comentario: disciplina.comentario})
    db.commit()
    return disciplina

def delete_disciplinas(db: Session, nome: str ):
    db.query(models.Disciplina).filter(models.Disciplina.nome == nome).delete()
    db.commit()
    # return f"{nome} foi removida"

##########################################################################################

def get_notas(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Nota).offset(skip).limit(limit).all()



def create_nota(db: Session, nota: schemas.NotaCreate, id: int):

    db_nota = models.Nota(**nota.dict(), id_disciplina=id)

    db.add(db_nota)

    db.commit()

    db.refresh(db_nota)

    return db_nota



def update_nota(db: Session, id: int, notaNow: models.Nota):
    db.query(models.Nota).filter(models.Nota.id == id).update({models.Nota.id_disciplina: notaNow.id_disciplina, models.Nota.nome_disciplina: notaNow.nome_disciplina, models.Nota.nota: notaNow.nota})
    db.commit()
    return notaNow
    
def delete_nota(db: Session, id:int):
    db.query(models.Nota).filter(models.Nota.id == id).delete()
    db.commit()
    # return f"{id} foi removida"