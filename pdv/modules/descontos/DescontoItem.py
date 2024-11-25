from modules.interfaces.desconto import Desconto
from modules.models.Produto import Produto


class DescontoItem(Desconto):
    def __init__(self, produto: Produto, valor: float):
        self.produto = produto
        self.valor = valor

    def aplicar(self, valor: float):
        pass
