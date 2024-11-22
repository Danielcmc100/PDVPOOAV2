"""Copyright (c) 2024."""

from sqlalchemy import select
from sqlalchemy.orm import Session

from pdv.models import Produto


def test_criar_produto(session: Session) -> None:
    """Testa a criação de um produto."""
    novo_produto = Produto(
        nome="Café",
        quantidade_estoque=10,
        preco=5.0,
        categoria="Bebida",
        estoque_minimo=5,
    )

    session.add(novo_produto)
    session.commit()

    produto = session.scalar(select(Produto).where(Produto.nome == "Café"))

    assert type(produto) is Produto

    assert {
        "nome": produto.nome,
        "quantidade_estoque": produto.quantidade_estoque,
        "preco": produto.preco,
        "categoria": produto.categoria,
        "estoque_minimo": produto.estoque_minimo,
    } == {
        "nome": "Café",
        "quantidade_estoque": 10,
        "preco": 5.0,
        "categoria": "Bebida",
        "estoque_minimo": 5,
    }
