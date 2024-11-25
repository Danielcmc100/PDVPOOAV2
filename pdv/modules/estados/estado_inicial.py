from modules.interfaces.estados_pdv import EstadoPDV


class EstadoInicial(EstadoPDV):
    def iniciar_pedido(self) -> None:
        print("Iniciando uma nova venda...")

    def consultar_produto(self, nome_produto) -> None:
        print("Iniciando uma nova venda...")
