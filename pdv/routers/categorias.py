"""Copyright (c) 2024."""

from http import HTTPStatus
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from pdv.database import get_session
from pdv.models import Categoria
from pdv.schemas import CategoriaSchema, PublicCategoria

router = APIRouter(prefix="/api/categorias", tags=["categorias"])
Session = Annotated[Session, Depends(get_session)]


@router.post(
    "/",
    status_code=HTTPStatus.CREATED,
)
def create_categoria(
        categoria: CategoriaSchema,
        session: Session
    ) -> PublicCategoria:
    """Cria uma nova categoria.

    Returns:
        Retorna a categorai e uma mensagem de sucesso.

    """
    db_categoria = Categoria(**categoria.dict())

    session.add(db_categoria)
    session.commit()

    return db_categoria


@router.get("/", status_code=HTTPStatus.OK)
def read_categoria(
        session: Session,
        id_categoria: int | None = None,
    ) -> PublicCategoria | list[PublicCategoria]:
    """Le uma categoria usando o id_categoria ou todas caso não especificado.

    Returns:
        Retorna a / as categoria / as e uma mensagem de sucesso.

    Raises:
        HTTPException: 404 NOT_FOUND Caso a categoria não seja encontrada.

    """
    if not id_categoria:
        db_categoria = session.query(Categoria).all()
    else:
        db_categoria = session.query(Categoria).get(id_categoria)

    if not db_categoria:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail="Categoria não encontrada.",
        )

    return db_categoria


@router.put("/", status_code=HTTPStatus.OK)
def update_categoria(
        id_categoria: int,
        categoria: CategoriaSchema,
        session: Session
    ) -> PublicCategoria:
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


@router.delete("/", status_code=HTTPStatus.NO_CONTENT)
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
