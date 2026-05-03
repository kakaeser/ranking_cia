from backend.entities.competicao import Competicao
from backend.repositories.interfaces.icompeticao_repo import ICompeticao_Repo

class Competicao_Repo(ICompeticao_Repo):
    def __init__(self, session):
        self.session = session
    
    def criar(self, nome: str):
        competicao = Competicao(nome=nome)
        self.session.add(competicao)
        return competicao
    
    def listar(self):
        return self.session.query(Competicao).all()

    def deletar(self, id: int):
        competicao = self.session.get(Competicao, id)
        if competicao:
            self.session.delete(competicao)