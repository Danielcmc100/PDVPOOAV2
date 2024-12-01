O que deve ser cadastrado diretamente (CRUD):
    Categoria
        api/categoria/create
        POST:
        categoria {
            nome
            descricao
        }
        resposta: 201 CREATE

        api/categoria/read
        GET
        api/categoria/update
        PUT
        api/categoria/delete
        Delete
            
    Produto
    Fornecedor

    Despesa
    ClientesFiado

    Usuario
        1-Administrador
        2-Funcionario

O que deve ser cadastrado indiretamente:
    Compra
        Pedido
            ItemPedido
                Produto

DUVIDAS:
1-Multiplos inputs

endpoints diferentes para obter um item especifico e outro para todos os itens

/api/categoria/read/{} - para unidade

/api/categoria/read/ - todas as unidades

uv run alembic revision --autogenerate -m "tabela fornecedores"
uv run alembic upgrad head
