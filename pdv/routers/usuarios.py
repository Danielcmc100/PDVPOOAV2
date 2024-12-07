"""Copyright (c) 2024."""

from http import HTTPStatus
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from pdv.database import get_session
from pdv.models import Usuario
from pdv.schemas import PublicUsuario, UsuarioSchema
from pdv.security import get_password_hash

router = APIRouter(prefix="/api/usuarios", tags=["usuarios"])
DBSession = Annotated[Session, Depends(get_session)]


@router.get("/")
def read_usuarios(
    session: DBSession, id_usuario: int | None = None
    ) -> PublicUsuario | list[PublicUsuario]:
    """Read all users.

    Returns:
        PublicUsuario | list[PublicUsuario]: List of users or a single user.

    Raises:
        HTTPException: If user is not found.

    """
    if id_usuario:
        usuario = session.query(Usuario).get(id_usuario)
        if not usuario:
            raise HTTPException(
                status_code=HTTPStatus.NOT_FOUND,
                detail="Usuario não encontrado",
            )
        return usuario

    return session.query(Usuario).all()


@router.post("/")
def create_usuario(
    usuario: UsuarioSchema, session: DBSession
    ) -> PublicUsuario:
    """Create a new user.

    Returns:
        PublicUsuario: User data.

    """
    usuario.senha = get_password_hash(usuario.senha)
    usuario_db = Usuario(**usuario.model_dump())
    session.add(usuario_db)
    session.commit()
    return usuario_db


@router.put("/")
def update_usuario(
    id_usuario: int, usuario: UsuarioSchema, session: DBSession
    ) -> PublicUsuario:
    """Update a user.

    Returns:
        PublicUsuario: User data.

    Raises:
        HTTPException: If user is not found.

    """
    usuario_db = session.query(Usuario).get(id_usuario)
    if not usuario_db:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail="Usuario não encontrado",
        )

    usuario.senha = get_password_hash(usuario.senha)
    usuario_db.update(usuario.model_dump())
    session.commit()
    return usuario_db


@router.delete("/")
def delete_usuario(id_usuario: int, session: DBSession) -> None:
    """Delete a user.

    Raises:
        HTTPException: If user is not found.

    """
    usuario = session.query(Usuario).get(id_usuario)
    if not usuario:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail="Usuario não encontrado",
        )

    session.delete(usuario)
    session.commit()
