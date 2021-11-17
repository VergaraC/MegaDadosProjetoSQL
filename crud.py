from sqlalchemy.orm import Session

from . import models, schemas


def get_nomes(db: Session):
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



def get_notas(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Nota).offset(skip).limit(limit).all()



def create_nota(db: Session, nota: schemas.NotaCreate, id: int):

    db_nota = models.Nota(**nota.dict(), id_disciplina=id)

    db.add(db_nota)

    db.commit()

    db.refresh(db_nota)

    return db_nota
