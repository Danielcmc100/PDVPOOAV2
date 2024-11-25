from abc import ABC, abstractmethod


class Desconto(ABC):
    @abstractmethod
    def aplicar(self, valor: float) -> None:
        pass
