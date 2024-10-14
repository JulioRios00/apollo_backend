# Product Management API

  ## Descrição
  Esta é uma API de gerenciamento de produtos desenvolvida com Django e Django REST Framework. A aplicação permite cadastrar, listar e calcular o preço promocional dos produtos com base em suas categorias.

## Funcionalidades
  Cadastro de novos produtos com os campos: nome, descrição, cor, categoria e preço.
  Cálculo automático do preço promocional baseado na categoria do produto.
  Listagem dos produtos cadastrados.


  ## Tecnologias Utilizadas
  - Python 3.11
  - Django 5.x
  - Django REST Framework
  - SQLite 
  
  ## Como Configurar e Executar a Aplicação


  Clone este repositório para a sua máquina local:

  https://github.com/JulioRios00/apollo_backend.git

  No diretório raiz do projeto, crie um ambiente virtual:

  python -m venv venv
  - source venv/bin/activate  # Para Mac/Linux

  ## Instale as dependências necessárias:

  pip install -r requirements.txt

  ### Configurar o Banco de Dados

  Rode as migrações para configurar o banco de dados:

  python manage.py migrate

  ## Rodar o Servidor de Desenvolvimento

  python manage.py runserver

  A aplicação estará disponível em http://127.0.0.1:8000/.

  ## Rotas Disponíveis

  - GET /products/ – Listar todos os produtos.
  - POST /products/ – Criar um novo produto
    
  Exemplo de Requisição POST para Cadastro de Produto
  URL: http://127.0.0.1:8000/products/
