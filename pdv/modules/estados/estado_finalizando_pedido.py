from numbers import Number
from modules.interfaces.estados_pdv import EstadoPDV

class EstadoFinalizandoPedido(EstadoPDV):
    def AplicarDesconto(self, TipoDesconto, valor) -> Number:
        pass

    def escolher_forma_pagamento(self, FormaPagamento) -> None:
        pass