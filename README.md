# API to validate deploy

## []()Getting Started:

## Run with Docker

```
docker-compose up -d --build
```

> Access in: [http://localhost:8000/](http://localhost:8000/)

## Run Locally

### []()Prerequisites

```
Python3
Pip
Virtual environment python
Django
Django Rest Framework
```

Activate your virtual environment before proceeding with the installation.

### []()Installing

To install the requirements:

```
pip install -r requirements.txt
```

To do database migrations:

```
make migrate
```

To run the Rest API:

```
python manage.py runserver
```

> Access in: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## []()Running the tests

To run the tests:

```
make test
```

## []()Running the linters

To run the linters (flake8, black and isort):

```
make linters
```

To run only pyflakes and checks unused imports:

```
make pyflakes
```

To run only isort:

```
make isort
```

To run only black:

```
make black
```

## []()Built With

- [Django Rest Framework](https://www.django-rest-framework.org/)

# REST API

## Endpoints:

Receive release to validate deploy:

`POST /release`

```json
{
  "ReleaseName": "DesafioCD",
  "ReleaseId": "386",
  "TeamProject": "Devx"
}
```

Get status of release with approver token:

`GET /approval?token={token}`

# Improvements:

- Manage sensitive data with Docker secrets


# DESAFIO:

Considere um cenário hipotético de uma empresa que tem no time vários desafios envolvendo integrações entre ferramentas e automação de processos. A ideia do que queremos de você é entender quais soluções você daria pra um cenário similar ao que enfrentamos no nosso dia a dia. Não se preocupe em trazer a melhor solução, ou em achar a solução "*correta*". A ideia é conversamos sobre o que você sabe e o que poderia ser usado pra resolver o problema. 

Vamos descrever algumas tasks que podem te guiar na construção de possíveis soluções. E para esse problema, podemos ter vááárias soluções possíveis ;) 

No nosso cenário hipotético temos várias [pipelines](https://docs.microsoft.com/en-us/azure/devops/pipelines/release/?view=azure-devops) que diariamente fazem dezenas de deploys para vários times. Essas pipelines geram releases (um pacote entregável da app). Quando fazemos uma mudança no código, essa mudança é um trigger para a pipeline, que gera uma release com o código alterado e pode ou não aplicar essa release em produção. Esses deploys precisam de algum tipo de processamento e validação para de fato acontecer.

Propomos que você crie uma API que seja usada para validar deploys. A ideia é que a "pipeline" antes de aplicar a release em produção, ela consulte periodicamente sua API, e quando a mudança estiver aprovada, o deploy aconteça.


1. `/release` : Quando uma release é criada, a pipeline faz uma chamada na sua API passando algumas informações principais relacionadas a release para que você processe e valide. 

    A resposta aqui não demore, por causa do *timeout* da pipeline 🤔


2. Caso os dados dessa release **não estejam** no seu banco, salve e em seguida faça seu processamento. 
    1. No processamento, você precisa fazer a seguinte operação:
        1. Recupere os aprovadores que devem aprovar essa release.
            - Utilize o mock para ajudar nos seus testes:

                [](https://run.mocky.io/v3/857ec66e-d39b-4c6a-85c8-9573cbd42ad7)

            - Para cada aprovador, crie um token único e envie para eles um email com esse ***token***, ***a url de aprovação***, e ***as informações da release***.

                Esse *token* pode ser usado tanto para identificar quem é o aprovador, como pra fazer o encode dos dados da release que ele está aprovado.

                Quando o aprovador receber o email, ele pode aprovar o ticket usando a url de aprovação. Essa aprovação deve ser salva no banco.


3. Caso os dados dessa release **estejam** no seu banco:
    1. Como a pipeline vai chamar sua api periodicamente, você deve informar se a release já foi aprovada, ou se ainda está pendente.

## Payload

POST `/release`

```json
{
    "ReleaseName": "Desafio-CD",
    "ReleaseId": "386",
    "TeamProject": "Devx",
} 
```

GET `/approval?token={token}`
