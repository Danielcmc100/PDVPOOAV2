"""Copyright (c) 2024."""

from http import HTTPStatus
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from pdv.database import get_session
from pdv.models import Fornecedor
from pdv.schemas import FornecedorSchema, PublicFornecedor

router = APIRouter(prefix="/api/fornecedores", tags=["fornecedores"])
Session = Annotated[Session, Depends(get_session)]


@router.post("/", status_code=HTTPStatus.CREATED)
def create_fornecedor(
        fornecedor: FornecedorSchema,
        session: Session = Session,
    ) -> PublicFornecedor:
    """Cria um novo fornecedor.

    Returns:
        Fornecedor: Fornecedor criado.

    """
    fornecedor = Fornecedor(**fornecedor.dict())
    session.add(fornecedor)
    session.commit()
    return fornecedor


@router.get("/", status_code=HTTPStatus.OK)
def get_fornecedor(
        session: Session,
        id_fornecedor: int | None = None,
    ) -> PublicFornecedor | list[PublicFornecedor]:
    """Le um fornecedor usando o id_fornecedor ou todos caso não especificado.

    Returns:
        Fornecedor | list[Fornecedor]: Fornecedor | Fornecedores lidos.

    Raises:
        HTTPException: 404 NOT_FOUND Caso o fornecedor não seja encontrado.

    """
    if not id_fornecedor:
        fornecedor = session.query(Fornecedor).all()
    else:
        fornecedor = session.query(Fornecedor).get(id_fornecedor)

    if not fornecedor:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail="Fornecedor não encontrado.",
        )

    return fornecedor


@router.put("/", status_code=HTTPStatus.OK)
def update_fornecedor(
        id_fornecedor: int,
        session: Session = Session,
    ) -> PublicFornecedor:
    """Atualiza um fornecedor.

    Returns:
        Fornecedor: Fornecedor atualizado.

    """
    fornecedor = session.query(Fornecedor).get(id_fornecedor)
    fornecedor.nome = fornecedor.nome
    fornecedor.cnpj = fornecedor.cnpj
    fornecedor.telefone = fornecedor.telefone

    session.commit()
    return fornecedor


@router.delete("/", status_code=HTTPStatus.NO_CONTENT)
def delete_fornecedor(
        id_fornecedor: int,
        session: Session = Session,
    ) -> None:
    """Deleta um fornecedor."""
    fornecedor = session.query(Fornecedor).get(id_fornecedor)
    session.delete(fornecedor)
    session.commit()
