from abc import ABC, abstractmethod
from typing import List, Optional
from backend.entities.equipe import Equipe


class IEquipe_Repo(ABC):

    @abstractmethod
    def criar(self, nome: str, c_id: int) -> Equipe:
        pass

    @abstractmethod
    def listar_por_cid(self, c_id: int) -> List[Equipe]:
        pass

    @abstractmethod
    def deletar(self, id: int) -> None:
        pass