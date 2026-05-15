from backend.repositories.implementions.provas_repo import Prova_Repo
from backend.repositories.implementions.pontuacao_repo import Pontuacao_Repo
from backend.repositories.implementions.equipe_repo import Equipe_Repo
from backend.config.db_init import DBConnectionHandler

class Provas_Service():

    def criar(self, nome:str, c_id: int):
        with DBConnectionHandler() as db:
            prova_repo = Prova_Repo(db.session)
            pontuacao_repo = Pontuacao_Repo(db.session)
            equipe_repo = Equipe_Repo(db.session)

            prova = prova_repo.criar(nome, c_id)

            equipes = equipe_repo.listar_por_cid(c_id)

            db.session.flush()

            if equipes:
                for e in equipes:
                    pontuacao_repo.criar(e.id, prova.id)

            return{
                "id" : prova.id,
                "nome": prova.nome,
            }
    
    def listar(self, c_id: int):
        with DBConnectionHandler() as db:
            repo = Prova_Repo(db.session)

            provas = repo.listar_por_cid(c_id)
            return [
            {
                "id" : c.id,
                "nome": c.nome,
                "c_id": c.c_id
            } 
            for c in provas
            ]
    
    def deletar(self, id: int):
        with DBConnectionHandler() as db:
            repo = Prova_Repo(db.session)
            repo.deletar(id)
             
