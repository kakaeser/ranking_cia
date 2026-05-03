from backend.entities.pontuacao import Pontuacao
from backend.repositories.interfaces.ipontuacao_repo import IPontuacao_Repo

class Pontuacao_Repo(IPontuacao_Repo):
    def __init__(self, session):
        self.session = session

    def criar(self, e_id: int, p_id: int, pontos =0):
        pontuacao = Pontuacao(e_id=e_id, p_id=p_id, pontos=pontos)
        self.session.add(pontuacao)
        return pontuacao

    def listar_por_equipe(self, e_id: int):
        return self.session.query(Pontuacao).filter(Pontuacao.e_id == e_id).all()

    def listar_por_prova(self, p_id: int):
        return self.session.query(Pontuacao).filter(Pontuacao.p_id == p_id).all()
    
    def atualizar_pontos(self, e_id: int, p_id: int, pontos: int):
        pontuacao = self.session.query(Pontuacao).filter(Pontuacao.e_id==e_id, Pontuacao.p_id==p_id).first()
        if pontuacao:
            pontuacao.pontos = pontos
        else:
            nova = Pontuacao(e_id=e_id, p_id=p_id, pontos=pontos)
            self.session.add(nova)