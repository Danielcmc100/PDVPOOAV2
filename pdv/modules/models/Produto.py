from Categoria import Categoria

class Produto:
    def __init__(self,
                 nome:str,
                 preco:float,
                 categoria:Categoria,
                 cod_barras:str,
                 quantidade_estoque:int,
                 estoque_minimo:int):
        self.nome = nome
        self.preco = preco
        self.categoria = categoria
        self.cod_barras = cod_barras
        self.quantidade_estoque = quantidade_estoque
        self.estoque_minimo = estoque_minimo