from Compra import Compra


class ClienteFiado:
    def __init__(
        self, nome: str, cpf: str, limite_de_credito: float, compras: [Compra]
    ):
        self.nome = nome
        self.cpf = cpf
        self.limite_de_credito = limite_de_credito
        self.compras = compras

    def adicionar_compra(self, compra):
        pass

    def calcular_total_compras(self):
        pass
