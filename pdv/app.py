"""Copyright (c) 2024."""

from fastapi import FastAPI

from pdv.routers import categorias, clientes, despesas, fornecedores, produtos

"""Módulo principal da aplicação."""

app = FastAPI()


app.include_router(categorias.router)
app.include_router(produtos.router)
app.include_router(fornecedores.router)
app.include_router(despesas.router)
app.include_router(clientes.router)


@app.get("/")
def read_root() -> dict[str, str]:
    """Retorna uma mensagem de boas-vindas.

    Returns:
        dict[str, str]: Retorna uma mensagem de boas-vindas.

    """
    return {"message": "Hello, World!"}
