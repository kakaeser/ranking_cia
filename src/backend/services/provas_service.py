from backend.repositories.implementions.provas_repo import Prova_Repo
from backend.config.db_init import DBConnectionHandler

class Provas_Service():

    def criar(self, nome:str, c_id: int):
        with DBConnectionHandler() as db:
            repo = Prova_Repo(db.session)

            competicao = repo.criar(nome, c_id)

            return{
                "id" : competicao.id,
                "nome": competicao.nome,
            }
    
    def listar(self, c_id: int):
        with DBConnectionHandler() as db:
            repo = Prova_Repo(db.session)

            competicoes = repo.listar_por_cid(c_id)
            return [
            {
                "id" : c.id,
                "nome": c.nome,
                "c_id": c.c_id
            } 
            for c in competicoes
            ]
    
    def deletar(self, id: int):
        with DBConnectionHandler() as db:
            repo = Prova_Repo(db.session)
            repo.deletar(id)
             
