from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import Float

from main import Disciplina

from .database import Base


class Disciplina(Base):
    __tablename__ = "disciplinas"


    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    professor = Column(String, nullable=True)
    comentario = Column(String, nullable=False)


class Nota(Base):
    __tablename__ = "notas"


    id = Column(Integer, primary_key=True, index=True)
    
    id_disciplina= Column(Integer, ForeignKey("disciplinas.id"),nullable=False)
    id_disciplina = relationship(Disciplina, primaryjoin=id_disciplina == Disciplina.id)
    nome_disciplina= Column(String, ForeignKey("disciplinas.nome"),nullable=False)
   
    nota = Column(Float, nullable=False)