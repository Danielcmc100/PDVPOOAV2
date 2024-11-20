# Python Project

This is a Python project project that incorporates the following tools for fast development and testing:

- **uv:** A modern, fast, and versatile Python package manager.
- **Pytest:** A flexible testing framework.
- **Ruff:** A powerful linter and code formatter.
- **Mypy:** A static type checker for Python.
- **GitHub Actions:** Automated linting and testing workflows.

## Getting Started
1. **Install `uv`:**

   Windows:
   ```bash
   powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/installps1 | iex"
   ```

   MacOS and Linux
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```
   
2. **Run the application:**
   ```bash
   uv run src/main.py
   ```

## Making the Most of It

### Using `uv`

`uv` is a modern Python package manager that simplifies dependency management and environment setup, for more information on how to use uv while managing this project read: [Working with uv projects](https://docs.astral.sh/uv/guides/projects)

1. **Install Dependencies:**
   ```bash
   uv install
   ```

2. **Add a New Dependency:**
   ```bash
   uv add <package-name>
   ```

3. **Remove a Dependency:**
   ```bash
   uv remove <package-name>
   ```

### Using `Ruff`

`Ruff` is a powerful linter and code formatter that helps maintain code quality. It also has a Visual Studio Code extension for easier integration.

1. **Lint the Code:**
   ```bash
   uv run ruff check .
   ```

2. **Automatically Fix Issues:**
   ```bash
   uv run ruff fix .
   ```

### Using `Pytest`

`Pytest` is a flexible testing framework that makes it easy to write simple and scalable test cases.

1. **Run All Tests:**
   ```bash
   uv run pytest
   ```

2. **Run Specific Tests:**
   ```bash
   uv run pytest path/to/test_file.py
   ```

3. **Generate a Test Report:**
   ```bash
   uv run pytest --html=report.html
   ```

### Using `Mypy`

`Mypy` is a static type checker for Python that helps ensure your code is type-safe. It also has a Visual Studio Code extension for easier integration.

1. **Check Types:**
   ```bash
   uv run mypy src/
   ```

2. **Check Specific File:**
   ```bash
   uv run mypy src/file.py
   ```

3. **Generate a Type Report:**
   ```bash
   uv run mypy --html-report report/ src/
   ```


# Instruções para entrega (necessário seguir à risca):
##### ● O trabalho deve ser entregue por um representante de cada equipe no Canvas via arquivo ZIP;
##### ● O arquivo ZIP deverá possuir o seguinte conteúdo:
##### ○ O nome dos integrantes do grupo, em um arquivo de texto;
##### ○ Uma pasta ou um link em um repositório do Github contendo os arquivos
## Necessários para a reprodução do projeto;
##### ○ Um arquivo de texto contendo um link para acesso a um arquivo de vídeo referente à gravação de tela feita pela equipe, mostrando todas as funcionalidades da aplicação em execução, como também a explicação do respectivo código-fonte. Caso a equipe opte por apresentar o trabalho remotamente (por questões pessoais ou por problemas técnicos), é necessário avisar o professor de antemão o mais breve possível para que a apresentação de sua solução e equipe seja agendada via Meet;
##### ● Para a gravação do vídeo, recomenda-se a utilização do software OBS Studio
(https://obsproject.com/download);
##### ● O trabalho deve ser feito, de preferência, em grupo de 3 a 4 integrantes;
##### ● Prazo de entrega: impreterivelmente 10/12/2024.
# TRABALHO 2: IMPLEMENTAÇÃO DE UM SISTEMA PDV E CONTROLE DE ESTOQUE
### 1. INTRODUÇÃO
Para esta parte do trabalho, utilize os requisitos levantados e a modelagem de classes
realizada para implementar um MVP (Minimum Viable Product)1 do sistema PDV hipotético
introduzido no trabalho anterior. É recomendável atentar-se às soluções disponibilizadas via
gabarito, juntamente com as devolutivas feitas pelo Canvas. Para a implementação do MVP,
sugere-se como stack de desenvolvimento uma aplicação Desktop implementada em C# com
Windows Forms, i.e. a stack que foi vista ao longo das aulas e materiais auxiliares. Contudo, o
grupo pode escolher outra stack de desenvolvimento que seja de preferência unânime de todos
os integrantes do grupo.
### 2. FUNCIONALIDADES DO MVP
De maneira macro, o MVP deverá simular (i) a operação de controle de estoque de produtos,
(i) controle e histórico de vendas e seus modos de pagamento (incluindo o modelo de crédito
“fiado”) e (iii) cadastro e controle de clientes e seus dependentes com limite de crédito no
estabelecimento. Mais precisamente, serão verificados os requisitos funcionais elencados no
gabarito. Vale enfatizar que cada requisito abaixo deverá possuir funcionalidades de
manipulação de dados (chamado CRUD2), além de funcionalidades mais refinadas, listadas a
seguir.
##### ● RF1. Gestão de Vendas: a aplicação deve controlar as vendas realizadas. O usuário pode utilizar filtros de datas para recuperar vendas específicas realizadas dentro de um período de tempo;
##### ● RF3. Gerenciamento de Crédito Cliente: o usuário do sistema deve ser capaz de consultar contas de clientes, receber pagamentos das faturas, alterar limites de crédito, alterar períodos de cobrança, bloquear o limite. Também deve poder incluir, atualizar e remover tanto o titular da conta, como os dependentes;
##### ● RF4. Controle de Estoque: a partir das vendas realizadas, o estoque dos produtos deve ser atualizado automaticamente. Alertas devem ser emitidos quando um determinado produto possuir uma quantidade igual ou menor à quantidade mínima estabelecida para o produto;
##### ● RF5. Gestão de Fornecedores: o sistema deve ser capaz de informar ao usuário os fornecedores de um produto consultado via texto ou código de barras, como também seus respectivos vendedores e contatos. 2 CRUD é um acrônimo em inglês para as quatro operações básicas realizadas em banco de dados ou aplicações: C - Create (Criar) R - Read (Ler) U - Update (Atualizar) D - Delete (Deletar). 1 O MVP é uma versão básica e funcional de um produto que contém apenas as características essenciais para atender às necessidades principais dos usuários iniciais e validar a proposta de valor do projeto.
### 3. CONSIDERAÇÕES FINAIS
Materiais de apoio, como vídeos e códigos-fonte contendo a formalização dos principais
conceitos, como também exemplos de criação e consulta a banco de dados serão
disponibilizados. Para o trabalho, recomenda-se a utilização do banco relacional SQLite. Os
materiais de apoio serão baseados nele. Quaisquer dúvidas referentes a banco de dados que
não estiverem sendo devidamente sanadas pelos materiais de apoio devem ser relatadas
imediatamente pelo professor via e-mail institucional: gabrielmachado@unifeso.edu.br.