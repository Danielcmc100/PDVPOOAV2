"""Copyright (c) 2024."""

from sqlalchemy.orm import Mapped, mapped_column, registry

registro_tabela = registry()


@registro_tabela.mapped_as_dataclass
class Produto:
    """Modelo do produto."""

    __tablename__ = "productos"

    cod_barras: Mapped[int] = mapped_column(init=False, primary_key=True)
    nome: Mapped[str] = mapped_column(unique=True)
    quantidade_estoque: Mapped[int]
    preco: Mapped[float]
    categoria: Mapped[str]
    # TODO(Kleber): Mudar categoria para classe Categoria
    # https://docs.astral.sh/ruff/rules/missing-todo-link/
    estoque_minimo: Mapped[int]
