from backend.entities.equipe import Equipe
from backend.repositories.interfaces.iequipe_repo import IEquipe_Repo

class Equipe_Repo(IEquipe_Repo):
    def __init__(self, session):
        self.session = session
    
    def criar(self, nome: str, c_id: int):
        equipe = Equipe(nome=nome, c_id=c_id)
        self.session.add(equipe)
        return equipe
    
    def listar_por_cid(self, c_id: int):
        return self.session.query(Equipe).filter(Equipe.c_id == c_id).all()

    def deletar(self, id: int):
        equipe = self.session.get(Equipe, id)
        if equipe:
            self.session.delete(equipe)