from sqlalchemy import Column, Integer, ForeignKey
from backend.config.base import Base
from sqlalchemy import UniqueConstraint



class Pontuacao(Base):
    __tablename__ = "resultados"

    id = Column(Integer, primary_key= True)
    e_id = Column(Integer, ForeignKey("equipes.id"), nullable= False)
    p_id = Column(Integer, ForeignKey("provas.id"), nullable= False)
    pontos = Column(Integer, default= 0)

    __table_args__ = (UniqueConstraint("equipe_id", "prova_id"))
