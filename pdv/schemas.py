"""Copyright (c) 2024."""
from datetime import datetime

from pydantic import BaseModel, Field, constr
from pydantic_extra_types.phone_numbers import PhoneNumber

"""Esquemas de dados da aplicação."""


class CategoriaSchema(BaseModel):
    """Esquema de dados para uma categoria."""

    nome: str
    descricao: str


class PublicCategoria(CategoriaSchema):
    """Esquema publico de dados para uma categoria."""

    id: int


class ProdutoSchema(BaseModel):
    """Esquema de dados para um produto."""

    cod_barras: int
    nome: str
    quantidade_estoque: int
    preco: float
    categoria_id: int
    estoque_minimo: int


class PublicProduto(ProdutoSchema):
    """Esquema publico de dados para um produto."""

    id: int


class FornecedorSchema(BaseModel):
    """Esquema de dados para um fornecedor."""

    nome: str
    cnpj: constr(pattern=r"^\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}$")
    telefone: PhoneNumber = Field(..., example="+1234567890")


class PublicFornecedor(FornecedorSchema):
    """Esquema publico de dados para um fornecedor."""

    id: int


class DespesaSchema(BaseModel):
    """Esquema de dados para uma despesa."""

    titulo: str
    valor: float
    tipo: str
    data_vencimento: datetime
    data_pagamento: datetime


class PublicDespesa(DespesaSchema):
    """Esquema publico de dados para uma despesa."""

    id: int


class ClienteSchema(BaseModel):
    """Esquema de dados para um cliente."""

    nome: str
    cpf: str
    telefone: PhoneNumber = Field(..., example="+1234567890")
    email: str
    endereco: str
    data_nascimento: datetime
    cliente_especial: bool
    periodo_pagamento: str


class PublicCliente(ClienteSchema):
    """Esquema publico de dados para um cliente."""

    id: int
