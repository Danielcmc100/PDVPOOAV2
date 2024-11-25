from abc import ABC, abstractmethod


class FormaPagamento(ABC):
    @abstractmethod
    def processar(self, valor) -> None:
        pass
