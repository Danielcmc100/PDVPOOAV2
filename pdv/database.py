"""Copyright (c) 2024."""

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from pdv.settings import Settings

"""Módulo de acesso ao banco de dados. """

engine = create_engine(Settings().DATABASE_URL)


def get_session() -> Session:
    """Retorna uma sessão do banco de dados.

    Yields:
        Session: Uma sessão do banco de dados.

    """
    with Session(engine) as session:
        yield session
