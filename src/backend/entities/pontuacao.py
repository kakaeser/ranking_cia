from sqlalchemy import Column, Integer, ForeignKey, UniqueConstraint
from backend.config.base import Base
from sqlalchemy.orm import relationship




class Pontuacao(Base):
    __tablename__ = "resultados"

    id = Column(Integer, primary_key= True)
    e_id = Column(Integer, ForeignKey("equipes.id"), nullable= False)
    p_id = Column(Integer, ForeignKey("provas.id"), nullable= False)
    pontos = Column(Integer, default= 0)
    equipe = relationship("Equipe", back_populates="pontuacoes")
    prova = relationship("Prova", back_populates="pontuacoes")

    __table_args__ = (UniqueConstraint("e_id", "p_id"),)
