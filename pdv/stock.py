"""Copyright (c) 2024."""

from typing import Any

from sqlalchemy.orm import Session

from pdv.models import Produto


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
