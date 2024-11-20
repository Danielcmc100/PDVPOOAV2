from datetime import datetime

from modules.interfaces.relatorios import Relatorios

class GerenciadorRelatorios(Relatorios):
    def gerar_relatorio_vendas(self, periodo:datetime.date) -> None:
        pass

    def gerar_relatorio_pagamentos(self, periodo:datetime.date) -> None:
        pass

    def gerar_relatorio_salarios(self, periodo:datetime.date) -> None:
        pass

    def gerar_relatorio_despesas_gerais(self, periodo:datetime.date) -> None:
        pass
