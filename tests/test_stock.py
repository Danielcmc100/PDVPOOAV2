"""Copyright (c) 2024."""

from sqlalchemy.orm.session import Session

from pdv.models import Produto
from pdv.stock import (
    create_produto,
    delete_produto,
    read_produto,
    update_produto,
)

PRECO = 10.0


def create_test_produto() -> Produto:
    """Cria um produto de teste.

    Returns:
        Produto: Retorna um produto de teste.

    """
    return Produto(
    nome="Produto Teste",
    preco=PRECO,
    quantidade_estoque=10,
    categoria="Categoria Teste",
    estoque_minimo=5,
    )


def test_create_produto(session: Session) -> None:
    """Testa a função create_produto."""
    produto = create_test_produto()
    create_produto(produto, session)
    result = session.query(Produto).filter_by(cod_barras=1).first()
    assert result is not None
    assert result.nome == "Produto Teste"
    assert result.preco == PRECO


def test_read_produto(session: Session) -> None:
    """Testa a função read_produto."""
    produto = create_test_produto()
    session.add(produto)
    session.commit()
    result = read_produto(1, session)
    assert result is not None
    assert result.nome == "Produto Teste"
    assert result.preco == PRECO


def test_update_produto(session: Session) -> None:
    """Testa a função update_produto."""
    produto = create_test_produto()
    session.add(produto)
    session.commit()

    nome_atualizado = "Produto Atualizado"
    preco_atualizado = 20.0

    update_produto(1, session, nome=nome_atualizado, preco=preco_atualizado)
    result = session.query(Produto).filter_by(cod_barras=1).first()
    assert result is not None
    assert result.nome == nome_atualizado
    assert result.preco == preco_atualizado


def test_delete_produto(session: Session) -> None:
    """Testa a função delete_produto."""
    produto = create_test_produto()
    session.add(produto)
    session.commit()
    delete_produto(1, session)
    result = session.query(Produto).filter_by(cod_barras=1).first()
    assert result is None
