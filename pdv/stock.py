"""Copyright (c) 2024."""

from typing import Any

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from pdv.models import Produto, registro_tabela


def create_produto(produto: Produto, session: Session) -> None:
    """Adiciona um novo produto ao banco de dados e confirma a transação."""
    session.add(produto)
    session.commit()


def read_produto(cod_barras: int, session: Session) -> Produto | None:
    """Retorna um produto do banco de dados.

    Returns:
        Produto: Retorna um produto do banco de dados.

    """
    return session.query(Produto).filter_by(cod_barras=cod_barras).first()


def update_produto(
        cod_barras: int,
        session: Session,
        **kwargs: Any
    ) -> None:
    """Atualiza um produto no banco de dados e confirma a transação."""
    produto = session.query(Produto).filter_by(cod_barras=cod_barras).first()
    for key, value in kwargs.items():
        setattr(produto, key, value)
    session.commit()


def delete_produto(cod_barras: int, session: Session) -> None:
    """Deleta um produto do banco de dados e confirma a transação."""
    produto = session.query(Produto).filter_by(cod_barras=cod_barras).first()
    session.delete(produto)
    session.commit()


if __name__ == "__main__":
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
