from abc import ABC, abstractmethod
from typing import List
from backend.entities.pontuacao import Pontuacao


class IPontuacao_Repo(ABC):

    @abstractmethod
    def criar(self, e_id: int, p_id: int, pontos: int = 0) -> Pontuacao:
        pass

    @abstractmethod
    def atualizar_pontos(self, e_id: int, p_id: int, pontos: int) -> None:
        pass

    @abstractmethod
    def listar_por_equipe(self, e_id: int) -> List[Pontuacao]:
        pass

    @abstractmethod
    def listar_por_prova(self, p_id: int) -> List[Pontuacao]:
        pass
