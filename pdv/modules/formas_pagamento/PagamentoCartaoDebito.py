from modules.interfaces.pagamento import Pagamento


class PagamentoCartaoDebito(Pagamento):
    def pagar(self, valor: float):
        pass
