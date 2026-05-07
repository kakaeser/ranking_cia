from backend.repositories.implementions.competicao_repo import Competicao_Repo
from backend.config.db_init import DBConnectionHandler

class Competicao_Service():

    def criar(self, nome:str):
        with DBConnectionHandler() as db:
            repo = Competicao_Repo(db.session)

            competicao = repo.criar(nome)

            return{
                "id" : competicao.id,
                "nome": competicao.nome
            }
    
    def listar(self):
        with DBConnectionHandler() as db:
            repo = Competicao_Repo(db.session)

            competicoes = repo.listar()
            return [
            {
                "id" : c.id,
                "nome": c.nome
            } 
            for c in competicoes
            ]
    
    def deletar(self, id: int):
        with DBConnectionHandler() as db:
            repo = Competicao_Repo(db.session)
            repo.deletar(id)
             
