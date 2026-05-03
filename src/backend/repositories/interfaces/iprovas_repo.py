from abc import ABC, abstractmethod
from typing import List, Optional
from backend.entities.prova import Prova


class IProva_Repo(ABC):

    @abstractmethod
    def criar(self, nome: str, c_id: int) -> Prova:
        pass

    @abstractmethod
    def listar_por_cid(self, c_id: int) -> List[Prova]:
        pass

    @abstractmethod
    def deletar(self, id: int) -> None:
        pass