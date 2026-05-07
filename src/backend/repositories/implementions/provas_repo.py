from backend.entities.prova import Prova
from backend.repositories.interfaces.iprovas_repo import IProva_Repo

class Prova_Repo(IProva_Repo):
    def __init__(self, session):
        self.session = session
    
    def criar(self, nome: str, c_id: int):
        prova = Prova(nome=nome, c_id=c_id)
        self.session.add(prova)
        return prova
    
    def listar_por_cid(self, c_id: int):
        return self.session.query(Prova).filter(Prova.c_id == c_id).all()

    def deletar(self, id: int):
        prova = self.session.get(Prova, id)
        if prova:
            self.session.delete(prova)