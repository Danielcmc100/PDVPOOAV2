from modules.models.ClientesFiado import ClientesFiado


class GerenciadorClientes:
    def __init__(self, clientes: [ClientesFiado]):
        self.clientes = clientes

    def cadastrar_cliente(self, cliente: ClientesFiado):
        pass

    def buscar_cliente(self, nome_cliente: str):
        pass
