from modules.models.ClientesFiado import ClientesFiado


class cliente_especial(ClientesFiado):
    def __init__(self, periodoPagamento: str):
        self.periodoPagamento = periodoPagamento

    def verificar_limite_de_credito(self, valor: float):
        pass
