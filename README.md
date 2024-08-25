# Projeto Django
## Projeto em Django desenvolvido para a imersão na Fábrica de Software da Unipê

## A API utilizada para o desenvolvimento do projeto foi a [RestCountries](https://restcountries.com/).
### Com essa API foi possível retornar os dados de um País como o Nome, População, Capital, dentre outras informações.

## Primeiros passos com o Django Rest Framework
### Criando a Venv
```shell
py -m venv venv
```

### Ativando a Venv
```shell
.\venv\Scripts\activate
```

### Instalando o Django Rest Framework (Com a venv ativa)
```shell
pip install djangorestframework
```

### Criando arquivo requirements.txt
```shell
pip freeze > requirements.txt
```

### Criando a pasta do projeto
```shell
django-admin startproject mapeando
```

### Criando o app
```shell
py manage.py startapp mapas_paises .
```

### Migração do banco de dados
```shell
py manage.py makemigrations
```
```shell
py manage.py migrate
```

### Criando um usuário administrador para o banco de dados Django
```shell
py manage.py createsuperuser
```

### Rodando o servidor
```shell
py manage.py runserver
```