from modules.autenticador.Autenticador import Autenticador
from modules.models.Categoria import Categoria
from modules.models.ClientesFiado import ClientesFiado
from modules.models.Fornecedor import Fornecedor
from modules.models.Produto import Produto
from modules.relatorios.GerenciadorRelatorios import GerenciadorRelatorios
from modules.repositorios.RepositorioClientesFiado import (
    RepositorioClientesFiado,
)
from modules.repositorios.RepositorioDespesas import RepositorioDespesas
from modules.repositorios.RepositorioFornecedores import (
    RepositorioFornecedores,
)
from modules.repositorios.RepositorioProdutos import RepositorioProdutos


class Administrador:
    def __init__(
        self,
        autenticador: Autenticador,
        gerenciador_de_relatorios: GerenciadorRelatorios,
        repositorio_de_clientes: RepositorioClientesFiado,
        repositorio_de_fornecedores: RepositorioFornecedores,
        repositorio_de_produtos: RepositorioProdutos,
        repositorio_de_despesas: RepositorioDespesas,
    ):
        self.autenticador = autenticador
        self.gerenciador_de_relatorios = gerenciador_de_relatorios
        self.repositorio_de_clientes = repositorio_de_clientes
        self.repositorio_de_fornecedores = repositorio_de_fornecedores
        self.repositorio_de_produtos = repositorio_de_produtos
        self.repositorio_de_despesas = repositorio_de_despesas

    def gerar_relatorio(self, tipo, periodo):
        pass

    def cadastrar_cliente_fiado(self, cliente: ClientesFiado):
        pass

    def cadastrar_fornecedor(self, fornecedor: Fornecedor):
        pass

    def cadastrar_produto(self, produto: Produto):
        pass

    def cadastrar_categoria(self, categoria: Categoria):
        pass

    def cadastrar_estoque_produto(self, produto: Produto, quantidade: int):
        pass

    def consultar_estoque(self, nome_do_produto: str):
        pass
