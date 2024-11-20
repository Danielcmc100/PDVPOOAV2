from modules.interfaces.estados_pdv import EstadoPDV

class EstadoPedidoEmAndamento(EstadoPDV):
    def adicionar_produto(self, Produto, quantidade) -> None:
        print("Adicionando produto...")

    def remover_produto(self, Produto) -> None:
        print("Removendo produto...")

    def editar_quantidade(self, Produto, quantidade) -> None:
        print("Adicionando produto...")

    def finalizar(self) -> None:
        pass
