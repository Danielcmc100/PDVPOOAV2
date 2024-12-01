"""Copyright (c) 2024."""

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
