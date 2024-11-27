"""Copyright (c) 2024."""

from http import HTTPStatus
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from pdv.database import get_session
from pdv.models import Categoria
from pdv.schemas import CategoriaSchema

router = APIRouter(prefix="/api/categoria", tags=["categoria"])
Session = Annotated[Session, Depends(get_session)]


@router.post("/create", status_code=HTTPStatus.CREATED)
def create_categoria(
        categoria: CategoriaSchema,
        session: Session
    ) -> Categoria:
    """Cria uma nova categoria.

    Returns:
        Retorna a categorai e uma mensagem de sucesso.

    """
    db_categoria = Categoria(**categoria.dict())

    session.add(db_categoria)
    session.commit()

    return db_categoria


@router.get("/read", status_code=HTTPStatus.OK)
def read_categoria(
        id_categoria: int,
        session: Session
    ) -> Categoria:
    """Le uma categoria usando o id_categoria.

    Returns:
        Retorna a categorai e uma mensagem de sucesso.

    Raises:
        HTTPException: 404 NOT_FOUND Caso a categoria não seja encontrada.

    """
    db_categoria = session.query(Categoria).get(id_categoria)

    if not db_categoria:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail="Categoria não encontrada.",
        )

    return db_categoria


@router.put("/update", status_code=HTTPStatus.OK)
def update_categoria(
        id_categoria: int,
        categoria: CategoriaSchema,
        session: Session
    ) -> Categoria:
    """Atualiza uma categoria.

    Returns:
        Retorna a categorai e uma mensagem de sucesso.

    Raises:
        HTTPException: 404 NOT_FOUND Caso a categoria não seja encontrada.

    """
    db_categoria = session.query(Categoria).get(id_categoria)

    if not db_categoria:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail="Categoria não encontrada.",
        )

    db_categoria.nome = categoria.nome
    db_categoria.descricao = categoria.descricao

    session.commit()

    return db_categoria


@router.delete("/delete", status_code=HTTPStatus.NO_CONTENT)
def delete_categoria(
        id_categoria: int,
        session: Session
    ) -> None:
    """Deleta uma categoria.

    Raises:
        HTTPException: 404 NOT_FOUND Caso a categoria não seja encontrada.

    """
    db_categoria = session.query(Categoria).get(id_categoria)

    if not db_categoria:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail="Categoria não encontrada.",
        )

    session.delete(db_categoria)
    session.commit()
