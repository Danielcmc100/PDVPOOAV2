from modules.autenticador.Autenticador import Autenticador
from modules.interfaces.estados_pdv import EstadoPDV
from modules.models.Pedido import Pedido


class PDV:
    def __init__(
        self,
        estado_atual: EstadoPDV,
        pedido_atual: Pedido,
        autenticador: Autenticador,
    ):
        self.estado_atual = estado_atual

    def set_estado(self, novo_estado: EstadoPDV):
        self.estado_atual = novo_estado

    def abrir(self):
        self.estado_atual.abrir()

    def fechar(self):
        self.estado_atual.fechar()

    def iniciar_venda(self):
        self.estado_atual.iniciar_venda()

    def suspender(self):
        self.estado_atual.suspender()

    def retornar(self):
        self.estado_atual.retornar()
