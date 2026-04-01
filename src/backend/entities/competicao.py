from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from backend.config.base import Base

class Competicao(Base):
    __tablename__ = "competicoes"

    id = Column(Integer, primary_key= True)
    nome = Column(String)

    equipes = relationship(
        "Equipe", 
        back_populates="competicao",
        cascade="all, delete-orphan" # <--- O EFEITO DOMINÓ AQUI
    )