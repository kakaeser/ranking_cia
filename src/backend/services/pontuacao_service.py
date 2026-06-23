from backend.repositories.implementions.pontuacao_repo import Pontuacao_Repo
from backend.repositories.implementions.equipe_repo import Equipe_Repo
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
    
    def calcular_rank(self, c_id):
        with DBConnectionHandler() as db:
            p_repo = Pontuacao_Repo(db.session)
            e_repo = Equipe_Repo(db.session)

            ranking_data = []

            equipes = e_repo.listar_por_cid(c_id)

            for equipe in equipes:
                pontuacao = p_repo.listar_por_equipe(equipe.id)

                if not pontuacao:
                    nota_formatada = "-"
                    nota_ordenacao = -1
                else:
                    nota_final = sum(p.pontos for p in pontuacao)
                    nota_formatada = nota_final
                    nota_para_ordenacao = nota_final
                    ranking_data.append({
                        "nome": equipe.nome,
                        "nota": nota_formatada,
                        "_ordem": nota_para_ordenacao
                    })
            ranking_data.sort(key=lambda x: x["_ordem"], reverse=True)
            
            for item in ranking_data:
                del item["_ordem"]

            return ranking_data

            

            

             
