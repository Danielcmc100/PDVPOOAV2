from ItemPedido import ItemPedido
from modules.interfaces.desconto import Desconto
from modules.interfaces.forma_pagamento import FormaPagamento
from Produto import Produto


class Pedido:
    def __init__(
        self,
        itens: ItemPedido,
        total: float,
        desconto: Desconto,
        forma_pagamento: FormaPagamento,
    ):
        self.itens = itens
        self.total = total
        self.desconto = desconto
        self.forma_pagamento = forma_pagamento

    def adicionar_item(self, produto: Produto, quantidade: int):
        pass

    def remover_item(self, produto: Produto):
        pass

    def editar_item(self, produto: Produto, quantidade: int):
        pass

    def aplicar_desconto(self, desconto):
        pass

    def set_forma_pagamento(self, forma_pagamento):
        pass

    def calcular_total(self):
        pass
