"""Copyright (c) 2024."""

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from pdv.models import Produto, registro_tabela
from pdv.stock import create_produto

"""Módulo principal do projeto."""


def main() -> None:
    """Função principal."""
    engine = create_engine("sqlite:///stock.db")
    registro_tabela.metadata.create_all(engine)

    with Session(engine) as session:
        produto = Produto(
            nome="Café",
            quantidade_estoque=10,
            preco=5.0,
            categoria="Bebida",
            estoque_minimo=5
        )
        create_produto(produto, session)


if __name__ == "__main__":
    main()
