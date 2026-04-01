from sqlalchemy import Column, Integer, ForeignKey
from backend.config.base import Base

class Pontuacao(Base):
    __tablename__ = "resultados"

    id = Column(Integer, primary_key= True)
    c_id = Column(Integer, ForeignKey("competicoes.id"), nullable= False)
    e_id = Column(Integer, ForeignKey("equipes.id"), nullable= False)
    p_id = Column(Integer, ForeignKey("provas.id"), nullable= False)
    pontos = Column(Integer, default= 0)
