configurar read.md

Product Management API
Descrição
Esta é uma API de gerenciamento de produtos desenvolvida com Django e Django REST Framework. A aplicação permite cadastrar, listar e calcular o preço promocional dos produtos com base em suas categorias.

Funcionalidades
Cadastro de novos produtos com os campos: nome, descrição, cor, categoria e preço.
Cálculo automático do preço promocional baseado na categoria do produto.
Listagem dos produtos cadastrados.
Estrutura do Projeto
backend/ – Código da aplicação backend com Django.
new_products/ – Contém a implementação dos modelos, views e rotas.
manage.py – Comando para administrar a aplicação.
Tecnologias Utilizadas
Python 3.11
Django 5.x
Django REST Framework
SQLite (ou Postgres, dependendo da sua configuração)
Como Configurar e Executar a Aplicação
Pré-requisitos
Python 3.x instalado na máquina.
Pip (gerenciador de pacotes do Python).
Virtualenv (opcional, mas recomendado).
Passo a Passo para Executar o Projeto
Clonar o Repositório

Clone este repositório para a sua máquina local:

bash
Copiar código
git clone https://github.com/seu-usuario/seu-repositorio.git
Criar e Ativar um Ambiente Virtual

No diretório raiz do projeto, crie um ambiente virtual (opcional, mas recomendado):

bash
Copiar código
python -m venv venv
source venv/bin/activate  # Para Mac/Linux
.\venv\Scripts\activate  # Para Windows
Instalar as Dependências

Instale as dependências necessárias:

bash
Copiar código
pip install -r requirements.txt
Configurar o Banco de Dados

Rode as migrações para configurar o banco de dados:

bash
Copiar código
python manage.py migrate
Rodar o Servidor de Desenvolvimento

Inicie o servidor local:

bash
Copiar código
python manage.py runserver
A aplicação estará disponível em http://127.0.0.1:8000/.

Rotas Disponíveis
GET /products/ – Listar todos os produtos.
POST /products/ – Criar um novo produto.
Exemplo de Requisição POST para Cadastro de Produto
URL: http://127.0.0.1:8000/products/

Método: POST

Body (JSON):

json
Copiar código
{
  "name": "iPhone 15 Pro",
  "description": "Celular de última geração",
  "color": "Titânio",
  "category": "smartphones",
  "price": 10999.00
}
Respostas Esperadas
POST /products/

Retorna o objeto do produto criado, incluindo o cálculo do preço promocional.

json
Copiar código
{
  "id": 1,
  "name": "iPhone 15 Pro",
  "description": "Celular de última geração",
  "color": "Titânio",
  "category": "smartphones",
  "price": 10999.00,
  "promotional_price": 10718.52
}