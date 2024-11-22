"""Copyright (c) 2024."""

from collections.abc import Generator
from typing import Any

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from pdv.models import registro_tabela


@pytest.fixture
def session() -> Generator[Session, Any, None]:
    """Fixture para criar uma sessão de teste.

    Yields:
        Session: Retorna uma sessão de teste.

    """
    engine = create_engine("sqlite:///:memory:")
    registro_tabela.metadata.create_all(engine)

    with Session(engine) as session:
        yield session

    registro_tabela.metadata.drop_all(engine)
