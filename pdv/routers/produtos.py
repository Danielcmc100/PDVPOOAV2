"""Copyright (c) 2024."""

from http import HTTPStatus
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from pdv.database import get_session
from pdv.models import Produto
from pdv.schemas import ProdutoSchema, PublicProduto

router = APIRouter(prefix="/api/produtos", tags=["produto"])
Session = Annotated[Session, Depends(get_session)]


@router.post("/", status_code=HTTPStatus.CREATED)
def create_produto(
        produto: ProdutoSchema,
        session: Session = Session,
    ) -> PublicProduto:
    """Cria um novo produto.

    Returns:
        Produto: Produto criado.

    """
    produto = Produto(**produto.dict())
    session.add(produto)
    session.commit()
    return produto


@router.get("/", status_code=HTTPStatus.OK)
def get_produto(
        session: Session,
        id_produto: int | None = None,
    ) -> PublicProduto | list[PublicProduto]:
    """Le um produto usando o id_produto ou todos caso não especificado.

    Returns:
        Produto | list[Produto]: Produto | Produtos lidos.

    Raises:
        HTTPException: 404 NOT_FOUND Caso o produto não seja encontrado.

    """
    if not id_produto:
        produto = session.query(Produto).all()
    else:
        produto = session.query(Produto).get(id_produto)

    if not produto:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail="Produto não encontrado.",
        )

    return produto


@router.put("/", status_code=HTTPStatus.OK)
def update_produto(
        id_produto: int,
        produto: ProdutoSchema,
        session: Session = Session,
    ) -> PublicProduto:
    """Atualiza um produto.

    Returns:
        Produto: Produto atualizado.

    Raises:
        HTTPException: 404 NOT_FOUND Caso o produto não seja encontrado.

    """
    db_produto = session.query(Produto).get(id_produto)

    if not db_produto:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail="Produto não encontrado.",
        )

    for field, value in produto:
        setattr(db_produto, field, value)

    session.commit()
    return db_produto


@router.delete("/", status_code=HTTPStatus.OK)
def delete_produto(
        id_produto: int,
        session: Session = Session,
    ) -> None:
    """Deleta um produto.

    Raises:
        HTTPException: 404 NOT_FOUND Caso o produto não seja encontrado.

    """
    db_produto = session.query(Produto).get(id_produto)

    if not db_produto:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail="Produto não encontrado.",
        )

    session.delete(db_produto)
    session.commit()
