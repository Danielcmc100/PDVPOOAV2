"""Copyright (c) 2024."""

from fastapi import FastAPI

"""Módulo principal da aplicação."""

app = FastAPI()


@app.get("/")
def read_root() -> dict[str, str]:
    """Retorna uma mensagem de boas-vindas.

    Returns:
        dict[str, str]: Retorna uma mensagem de boas-vindas.

    """
    return {"message": "Hello, World!"}
