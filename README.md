# REST API Operações CRUD com Django Templates

## Apresentação do projeto

https://github.com/guicamargo19/fullstack_rest_api_templates/assets/133445061/80a6221e-6859-4e73-98b6-08e026501264

O projeto viabiliza a criação de um usuário com a integral preservação de todos os seus dados. Através de uma
interface Front-end simples, minimalista e intuitiva, construída com **Django Templates**, são executáveis operações CRUD (Create, Read, Update, Delete).

O Back-end, elaborado em **Django** com **Python**, incorpora a REST API mediante o **Django Rest Framework**, e o armazenamento de dados
é efetuado utilizando o **PostgreSQL**.

## Sumário

- [Instalação](#instalacao)
- [Rodando o projeto](#rodando-o-projeto)
- [Contribuindo](#configuracao-desenvolvimento)
- [Ferramentas utilizadas](#ferramentas)
- [Sobre](#sobre)
    - [Back-end](#backend)
    - [Front-end](#frontend)
    - [Banco de dados](#banco-de-dados)
    - [Docker](#docker)


<div id="instalacao">

## Instalação

Siga estes passos para instalar e configurar o ambiente necessário para rodar o projeto em sua máquina local.

### Pré-requisitos

Antes de iniciar, você precisará ter instalado em sua máquina as seguintes ferramentas:

- [Git](https://git-scm.com)
- [Docker](https://docker.com/)
- [Docker Compose](https://docs.docker.com/compose/install/)

### Clonando o Repositório

Siga as etapas a seguir para configurar o ambiente de desenvolvimento:

- Clone este repositório em sua máquina local.
```bash
git clone https://github.com/guicamargo19/fullstack_rest_api_templates.git
```
</div>
<div id="rodando-o-projeto">

## Rodando o projeto no Docker

1. Na raiz do projeto, crie o arquivo ".env" a partir do ".env-example". 

2. Execute o comando a seguir e certifique-se de que o Docker Desktop está aberto.
```shell
docker-compose up --build
```
</div>
<div id="configuracao-desenvolvimento">

## Contribuindo

1. Navegue até o diretório clonado
```shell
cd fullstack_rest_api_templates
```
2. Crie e ative o ambiente virtual,(comandos podem variar entre Windows, Linux e Mac.)
```shell
python -m venv venv
source venv/bin/activate
```
Após a ativação do ambiente virtual, selecione o interpretador correto para ele, digitando na barra superior 
de pesquisa do VSCode: **>Python Select Interpreter**

3. Execute o seguinte comando para instalar as dependências:
```shell
pip install -r requirements.txt
```

## Dotenv file (.env)

Na raiz do projeto é possível encontrar o arquivo ".env_example", sendo que, a partir dele, deve-se criar o
arquivo ".env" que deve ser preenchido com variáveis de ambiente com configurações necessárias para o banco
de dados PostgreSQL. Certifique-se de criar este arquivo no mesmo local do exemplo.

## Testes

Foram implementados testes para verificar a integridade do Model, das Views e do
Serializer neste projeto. Também foi utilizado DRF (APITestCase) para simplificar e criar testes 
para verificar se as operações CRUD estão funcionando como esperado.

Executando os testes dentro do Docker:
```shell
docker-compose run --rm web python manage.py test
```

</div>
<div id="ferramentas">

## 🛠️ Ferramentas utilizadas para construção do projeto

* **Python** - Linguagem de programação de alto nível, interpretada de script, imperativa, orientada a objetos, funcional, de tipagem dinâmica e forte.
* **Django** - Framework para desenvolvimento rápido para web, escrito em Python, que utiliza o padrão model-template-view.
* **Django Rest Framework** - Biblioteca que permite a construção de APIs REST utilizando a estrutura do Django.
* **HTML** - Linguagem de marcação utilizada na construção de páginas na Web.
* **CSS** - Cascading Style Sheets é um mecanismo para adicionar estilos a uma página web.
* **PostgreSQL** - Um sistema gerenciador de banco de dados objeto relacional, desenvolvido como projeto de código aberto.
* **Docker** - Conjunto de produtos de PaaS que usam virtualização de nível de sistema operacional para entregar software em pacotes chamados contêineres.

</div>
<div id="sobre">

## Sobre
<div id="backend">

## 1. Back-End (Django com Python)

Back-end desenvolvido em **Django** com **Python** e construção da Rest API com **DRF (Django Rest Framework)**, 
que mantém os dados da Entidade Usuário. Ele provém toda a manutenção (CRUD) dessa entidade. 

O modelo da entidade usuário possui quatro campos (nickname, fullname, email e age), sendo o "nickname" e "name" um campo
do tipo CharField, o campo "email" do tipo EmailField e o "age" sendo um campo tipo PositiveIntegerField, sendo que os
campos "nickname" e "email" não podem ser repetidos na base de dados.

Projeto está na raiz, onde se encontra-se o app api_rest, assim como a pasta api_root onde se localizam os arquivos como
settings.py e wsgi.py. No App api_rest é onde estão localizados o Model, as Views utilizando CBV (Class Based Views), os Serializers e os Testes.

O Back-End é hospedado na porta 8000: [http://localhost:8000/api/api_rest/](http://localhost:8000/api/api_rest/)

## API

### API Endpoint: Listar usuários
**GET /api/api_rest/**

Retorna uma lista de todos os usuários existentes.

#### Resposta
```
HTTP 200 OK
Content-Type: application/json

[
    {
        "id": 1,
        "nickname": "patricio",
        "name": "Patricio de Souza",
        "email": "patricio@gmail.com",
        "age": 45
    },
    {
        "id": 2,
        "nickname": "antonio",
        "name": "Antonio Carlos da Silva",
        "email": "antonio@email.com",
        "age": 56
    }
]
```
-------------------------------------
## API Endpoint: Criar um usuário

**POST /api/api_rest/**

Cria um usuário

#### Resposta
```
HTTP 201 OK
Content-Type: application/json
```
-------------------------------------
## API Endpoint: Atualiza um usuário

**PATCH /api/produtos/${productID}**

Atualiza o usuário solicitado

#### Resposta
```
HTTP 200 OK
Content-Type: application/json
```
-------------------------------------
## API Endpoint: Deletar um usuário

**DELETE /api/api_rest/${userID}**

Apaga o usuário solicitado

#### Resposta
```
HTTP 204 OK
Content-Type: application/json
```
-------------------------------------
## API Endpoint: Deletar todos os usuários

**DETELE /api/api_rest/**

Apaga todos os usuários

#### Resposta
```
HTTP 204 OK
Content-Type: application/json
```

<div id="frontend">

## 2. Front-End (Django Templates)

O Front-end do projeto foi realizado em Django Templates consumindo os dados da API através do contexto passado
para as CBVs na renderização dos templates.

O Front-End é hospedado na porta 8000: [http://localhost:8000/api/](http://localhost:8000/api/)

</div>
<div id="banco-de-dados">

## 3. Banco de Dados (PostgreSQL)

O banco de dados **PostgreSQL** é estruturado de forma simples, composto apenas por uma tabela, a qual abriga os dados dos usuários.

Após a definição dos modelos no Django, é imperativo criar as migrações correspondentes para aplicar as alterações no banco de dados.
Isso é realizado através do comando **"python manage.py makemigrations"**.

Uma vez que as migrações tenham sido criadas, é necessário aplicá-las utilizando o comando **"python manage.py migrate"**.
Esta operação executa todas as migrações pendentes e atualiza o esquema do banco de dados de acordo com as definições do modelo.

O DB-Server é hospedado na porta padrão 5432 do PostgreSQL.

</div>
<div id="docker">

## 4. Docker e Docker Compose

O arquivo "docker-compose.yml" é responsável por definir dois serviços distintos: 'db-server' e o 'web',
cada um com suas próprias configurações e dependências.

- Utiliza-se a imagem 'postgres:latest' disponível no Docker Hub, que é uma imagem pré-configurada do PostgreSQL.
- O ambiente é configurado com os dados necessários, como o nome do banco de dados, usuário e senha, os quais foram previamente especificados no arquivo ".env".
- A seção "volumes" mapeia um diretório de dados do PostgreSQL, garantindo a persistência dos dados entre reinicializações do contêiner.
- Na seção "network", é definida a rede: 'django_network'. A rede é utilizadas para separar a comunicação entre os serviços, simplificando a interação entre os contêineres.
- Na seção entrypoint é adicionado o script de inicialização ["/code/entrypoint.sh"] com os comandos aguardando o banco de dados ser montado e migração dos models.

</div>
</div>

## ✒️ Autor

Guilherme Ferreira Camargo
