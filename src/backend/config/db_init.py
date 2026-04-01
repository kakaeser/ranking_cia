from backend.config.connection import DBConnectionHandler
from backend.config.base import Base

# IMPORTANTE: importar TODAS as entidades
from backend.entities.equipe import Equipe
from backend.entities.prova import Prova
from backend.entities.pontuacao import Pontuacao
from backend.entities.competicao import Competicao


def init_db():
    db = DBConnectionHandler()
    engine = db.get_engine()
    Base.metadata.create_all(engine)
