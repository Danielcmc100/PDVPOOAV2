"""Copyright (c) 2024."""

from pydantic import BaseModel

"""Esquemas de dados da aplicação."""


class CategoriaSchema(BaseModel):
    """Esquema de dados para uma categoria."""

    nome: str
    descricao: str
