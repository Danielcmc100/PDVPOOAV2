from datetime import datetime

class Despesa:
    def __init__(self, titulo:str, valor:float, tipo:str, dataVencimento:datetime, dataPagamento:datetime):
        self.titulo = titulo
        self.valor = valor
        self.tipo = tipo
        self.dataVencimento = dataVencimento
        self.dataPagamento = dataPagamento