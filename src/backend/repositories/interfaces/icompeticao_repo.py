from abc import ABC, abstractmethod
from typing import List, Optional
from backend.entities.competicao import Competicao


class ICompeticao_Repo(ABC):

    @abstractmethod
    def criar(self, nome: str) -> Competicao:
        pass

    @abstractmethod
    def listar(self) -> List[Competicao]:
        pass

    @abstractmethod
    def deletar(self, id: int) -> None:
        pass