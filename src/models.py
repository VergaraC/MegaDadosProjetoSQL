from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import Float

from main import Disciplina


from .database import Base


class Disciplina(Base):

    __tablename__ = "disciplinas"


    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    professor = Column(String)
    comentario = Column(String, nullable=False)


class Nota(Base):

    __tablename__ = "notas"


    id = Column(Integer, primary_key=True, index=True)
    
    id_disciplina= Column(String(80), ForeignKey("disciplinas.id"),nullable=False)
    id_disciplina = relationship(Disciplina, primaryjoin=id_disciplina == Disciplina.id)
    nome_disciplina= Column(String(80), ForeignKey("disciplinas.nome"),nullable=False)
   
    nota = Column(Float)