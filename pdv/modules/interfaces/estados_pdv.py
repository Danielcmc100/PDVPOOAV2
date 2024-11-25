from abc import ABC, abstractmethod


class EstadoPDV(ABC):
    @abstractmethod
    def iniciar_pedido(self) -> None:
        pass

    @abstractmethod
    def consultar_produto(self, nome_produto) -> None:
        pass

    def finalizar_pedido(self) -> None:
        pass
