from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import Float

from database import Base


class Disciplina(Base):
    __tablename__ = "disciplinas"

    nome = Column(String(45),primary_key=True, nullable=False)
    professor = Column(String(45), nullable=True)
    comentario = Column(String(45), nullable=False)


class Nota(Base):
    __tablename__ = "notas"


    id = Column(Integer, primary_key=True, index=True)
    
    nome_disciplina= Column(String(45), ForeignKey("disciplinas.nome"),nullable=False)
    nota = Column(Float, nullable=False)