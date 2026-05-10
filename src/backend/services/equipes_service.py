from backend.repositories.implementions.equipe_repo import Equipe_Repo
from backend.repositories.implementions.provas_repo import Prova_Repo
from backend.repositories.implementions.pontuacao_repo import Pontuacao_Repo
from backend.config.db_init import DBConnectionHandler

class Equipes_Service():

    def criar(self, nome:str, c_id: int):
        with DBConnectionHandler() as db:
            equipe_repo = Equipe_Repo(db.session)
            prova_repo = Prova_Repo(db.session)
            pontuacao_repo = Pontuacao_Repo(db.session)

            equipe = equipe_repo.criar(nome, c_id)

            provas = prova_repo.listar_por_cid(c_id)
            if provas:
                for p in provas:
                    pontuacao_repo.criar(equipe.id, p.id)

            return{
                "id" : equipe.id,
                "nome": equipe.nome,
            }

    def criar_lista(self, lista: dict, c_id: int):
        with DBConnectionHandler() as db:
            repo = Equipe_Repo(db.session)

            for nome in lista:
                repo.criar(nome, c_id)
    
    def listar(self, c_id: int):
        with DBConnectionHandler() as db:
            repo = Equipe_Repo(db.session)

            equipes = repo.listar_por_cid(c_id)
            return [
            {
                "id" : c.id,
                "nome": c.nome,
                "c_id": c.c_id
            } 
            for c in equipes
            ]
    
    def deletar(self, id: int):
        with DBConnectionHandler() as db:
            repo = Equipe_Repo(db.session)
            repo.deletar(id)
             
