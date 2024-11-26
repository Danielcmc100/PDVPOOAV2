"""Copyright (c) 2024."""

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from pdv.models import Categoria, Produto, registro_tabela
from pdv.stock import create_produto

"""Módulo principal do projeto."""


def main() -> None:
    """Função principal."""
    engine = create_engine("sqlite:///stock.db")
    registro_tabela.metadata.create_all(engine)

    with Session(engine) as session:
        categoria = Categoria(
            nome="Alimentos",
            descricao="Categoria de alimentos",
        )
        produto = Produto(
            nome="Café",
            quantidade_estoque=10,
            preco=5.0,
            categoria_id=1,
            categoria=categoria,
            estoque_minimo=5,
        )
        create_produto(produto, session)


if __name__ == "__main__":
    main()
