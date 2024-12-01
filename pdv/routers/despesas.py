"""Copyright (c) 2024."""

from http import HTTPStatus
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from pdv.database import get_session
from pdv.models import Despesa
from pdv.schemas import DespesaSchema, PublicDespesa

router = APIRouter(prefix="/api/despesas", tags=["despesas"])
Session = Annotated[Session, Depends(get_session)]


@router.post("/", status_code=HTTPStatus.CREATED)
def create_despesa(
    despesa: DespesaSchema,
    session: Session = Session
) -> PublicDespesa:
    """Cria uma nova despesa.

    Returns:
        PublicDespesa: A nova despesa criada.

    """
    nova_despesa = Despesa(**despesa.dict())
    session.add(nova_despesa)
    session.commit()
    return nova_despesa


@router.get("/", status_code=HTTPStatus.OK)
def get_despesa(
    id_despesa: int | None = None,
    session: Session = Session
) -> PublicDespesa | list[PublicDespesa]:
    """Obtem uma despesa.

    Returns:
        PublicDespesa: A despesa obtida.

    Raises:
        HTTPException: 404 NOT_FOUND Caso a despesa não seja encontrada.

    """
    if id_despesa:
        despesa = session.query(Despesa).get(id_despesa)
    else:
        despesa = session.query(Despesa).all()

    if despesa is None:
        raise HTTPException(HTTPStatus.NOT_FOUND)
    return despesa


@router.put("/", status_code=HTTPStatus.OK)
def update_despesa(
    id_despesa: int,
    despesa: DespesaSchema,
    session: Session = Session
) -> PublicDespesa:
    """Atualiza uma despesa.

    Returns:
        PublicDespesa: A despesa atualizada.

    Raises:
        HTTPException: 404 NOT_FOUND Caso a despesa não seja encontrada.

    """
    despesa_atualizada = session.query(Despesa).get(id_despesa)
    if despesa_atualizada is None:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail="Despesa não encontrada.",
        )

    for campo, valor in despesa.dict().items():
        setattr(despesa_atualizada, campo, valor)

    session.commit()
    return despesa_atualizada


@router.delete("/", status_code=HTTPStatus.NO_CONTENT)
def delete_despesa(
    id_despesa: int,
    session: Session = Session
) -> None:
    """Deleta uma despesa.

    Raises:
        HTTPException: 404 NOT_FOUND Caso a despesa não seja encontrada.

    """
    despesa = session.query(Despesa).get(id_despesa)
    if despesa is None:
        raise HTTPException(HTTPStatus.NOT_FOUND)

    session.delete(despesa)
    session.commit()
