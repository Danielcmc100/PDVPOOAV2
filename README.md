# Projeto PDV

Para rodar esse projeto em seu ambiente local, certifique-se queu você possui os seguintes softwares instalados em seu sistema:

- Docker
- Docker Compose
- Node (versão 20 ou superior)
- NPM
- GIT

Tendo isso istalado, siga os passos abaixo:

1. Baixe o projeto no repositório
2. Usando o programa de CLI (terminal) do seu siistema operacional, acesse o diretório onde o repositório foi baixado
3. Rode o comando abaixo para montar o conteiner Docker
```bash
   docker compose build
   ```
   4. Rode o comando abaixo para colocar o conteiner no ar
   ```bash
   docker compose up
   ```
   5. Feito isso, o servidor estará funcionando. Para interagir com o sistema, pelo terminal acesse o diretório /frontend
   ```bash
   cd frontend
   ```
   6. Agora rode o comando abaixo para iniciar o  frontend do projeto
   ```bash
   npm run dev
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