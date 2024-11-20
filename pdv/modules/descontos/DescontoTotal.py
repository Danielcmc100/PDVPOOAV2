from modules.interfaces.desconto import Desconto

class DescontoItem(Desconto):
    def __init__(self, valor: float):
        self.valor = valor

    def aplicar(self, valor: float):
        pass

