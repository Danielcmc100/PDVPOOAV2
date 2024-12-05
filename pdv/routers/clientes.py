"""Copyright (c) 2024."""

from http import HTTPStatus
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from pdv.database import get_session
from pdv.models import Cliente
from pdv.schemas import ClienteSchema, PublicCliente

router = APIRouter(prefix="/api/clientes", tags=["clientes"])
Session = Annotated[Session, Depends(get_session)]


@router.post("/", status_code=HTTPStatus.CREATED)
def create_cliente(
        cliente: ClienteSchema,
        session: Session
    ) -> PublicCliente:
    """Cria um novo cliente.

    Returns:
        Retorna o cliente e uma mensagem de sucesso.

    """
    db_cliente = Cliente(**cliente.dict())

    session.add(db_cliente)
    session.commit()

    return db_cliente


@router.get("/", status_code=HTTPStatus.OK)
def read_cliente(
        session: Session,
        id_cliente: int | None = None,
    ) -> PublicCliente | list[PublicCliente]:
    """Le um cliente usando o id_cliente ou todos caso não especificado.

    Returns:
        Retorna o / os cliente / s e uma mensagem de sucesso.

    Raises:
        HTTPException: 404 NOT_FOUND Caso o cliente não seja encontrado.

    """
    if not id_cliente:
        db_cliente = session.query(Cliente).all()
    else:
        db_cliente = session.query(Cliente).get(id_cliente)

    if not db_cliente:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail="Cliente não encontrado."
        )

    return db_cliente


@router.put("/", status_code=HTTPStatus.OK)
def update_cliente(
        cliente: ClienteSchema,
        session: Session
    ) -> PublicCliente:
    """Atualiza um cliente.

    Returns:
        Retorna o cliente atualizado e uma mensagem de sucesso.

    Raises:
        HTTPException: 404 NOT_FOUND Caso o cliente não seja encontrado.

    """
    db_cliente = session.query(Cliente).get(cliente.id)

    if not db_cliente:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail="Cliente não encontrado."
        )

    for key, value in cliente.dict().items():
        setattr(db_cliente, key, value)

    session.commit()

    return db_cliente


@router.delete("/", status_code=HTTPStatus.NO_CONTENT)
def delete_cliente(
        id_cliente: int,
        session: Session
    ) -> None:
    """Deleta um cliente.

    Raises:
        HTTPException: 404 NOT_FOUND Caso o cliente não seja encontrado.

    """
    db_cliente = session.query(Cliente).get(id_cliente)

    if not db_cliente:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail="Cliente não encontrado."
        )

    session.delete(db_cliente)
    session.commit()
