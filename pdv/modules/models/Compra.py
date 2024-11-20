import datetime

from modules.models.ItemPedido import ItemPedido

class Compra:
    def __init__(self, valor:float, data:datetime.date, itens:[ItemPedido]):
        self.valor = valor
        self.data = data
        self.itens = itens
