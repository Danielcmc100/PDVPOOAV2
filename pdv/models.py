"""Copyright (c) 2024."""

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, registry, relationship

registro_tabela = registry()


@registro_tabela.mapped_as_dataclass
class Categoria:
    """Modelo da categoria."""

    __tablename__ = "categorias"

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    nome: Mapped[str] = mapped_column(unique=True)
    descricao: Mapped[str]


@registro_tabela.mapped_as_dataclass
class Produto:
    """Modelo do produto."""

    __tablename__ = "produtos"

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    cod_barras: Mapped[int] = mapped_column(unique=True)
    nome: Mapped[str] = mapped_column(unique=True)
    quantidade_estoque: Mapped[int]
    preco: Mapped[float]
    categoria_id: Mapped[int] = mapped_column(ForeignKey("categorias.id"))
    categoria: Mapped[Categoria] = relationship("Categoria", init=False)
    estoque_minimo: Mapped[int]


@registro_tabela.mapped_as_dataclass
class Fornecedor:
    """Modelo do fornecedor."""

    __tablename__ = "fornecedores"

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    nome: Mapped[str] = mapped_column(unique=True)
    cnpj: Mapped[str] = mapped_column(unique=True)
    telefone: Mapped[str]
