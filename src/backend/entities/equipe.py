from sqlalchemy import Column, Integer, String, ForeignKey
from backend.config.base import Base
from sqlalchemy.orm import relationship

class Equipe(Base):
    __tablename__ = "equipes"

    id = Column(Integer, primary_key= True)
    c_id = Column(Integer, ForeignKey("competicoes.id"), nullable= False)
    nome = Column(String, nullable= False)

    competicao = relationship("Competicao", back_populates="equipes")

    pontuacoes = relationship("Pontuacao", back_populates="equipe",cascade="all, delete-orphan")