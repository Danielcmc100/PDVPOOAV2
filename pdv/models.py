"""Copyright (c) 2024."""

from datetime import datetime, timedelta

from sqlalchemy import ForeignKey, func
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


@registro_tabela.mapped_as_dataclass
class Despesa:
    """Modelo da despesa."""

    __tablename__ = "despesas"

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    titulo: Mapped[str]
    valor: Mapped[float]
    tipo: Mapped[str]
    data_vencimento: Mapped[datetime]
    data_pagamento: Mapped[datetime]


@registro_tabela.mapped_as_dataclass
class Cliente:
    """Modelo do cliente."""

    __tablename__ = "clientes"

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    nome: Mapped[str]
    cpf: Mapped[str]
    telefone: Mapped[str]
    email: Mapped[str]
    endereco: Mapped[str]
    data_nascimento: Mapped[datetime]
    limite_de_credito: Mapped[float]
    cliente_especial: Mapped[bool]
    periodo_pagamento: Mapped[timedelta]


@registro_tabela.mapped_as_dataclass
class Usuario:
    """Modelo do usuário."""

    __tablename__ = "usuarios"

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    nome: Mapped[str] = mapped_column(unique=True)
    email: Mapped[str] = mapped_column(unique=True)
    senha: Mapped[str]
    admin: Mapped[bool]
    data_criacao: Mapped[datetime] = mapped_column(
        init=False, server_default=func.now()
    )
    data_atualizacao:  Mapped[datetime] = mapped_column(
        init=False, server_default=func.now(), onupdate=func.now()
    )
