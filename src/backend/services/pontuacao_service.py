from backend.repositories.implementions.pontuacao_repo import Pontuacao_Repo
from backend.config.db_init import DBConnectionHandler

class Pontuacao_Service():    
    def listar_por_prova(self, p_id: int):
        with DBConnectionHandler() as db:
            repo = Pontuacao_Repo(db.session)

            pontuacoes = repo.listar_por_prova(p_id)
            return [
            {
                "id" : p.id,
                "nome": p.equipe.nome,
                "e_id": p.e_id,
                "p_id": p.p_id,
                "pontos": p.pontos
            } 
            for p in pontuacoes
            ]
    
    def atualizar_pontos(self, e_id, p_id, pontos):
        with DBConnectionHandler() as db:
            repo = Pontuacao_Repo(db.session)
            repo.atualizar_pontos(e_id, p_id, pontos)
    
             
