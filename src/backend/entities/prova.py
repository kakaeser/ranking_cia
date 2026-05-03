from sqlalchemy import Column, Integer, String, ForeignKey
from backend.config.base import Base
from sqlalchemy.orm import relationship

class Prova(Base):
    __tablename__ = "provas"

    id = Column(Integer, primary_key=True)
    c_id = Column(Integer, ForeignKey("competicoes.id"), nullable= False)
    nome = Column(String, nullable= False)

    pontuacoes = relationship(
        "Pontuacao",
        back_populates="prova",
        cascade="all, delete-orphan"
    )
