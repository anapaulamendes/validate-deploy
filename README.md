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
