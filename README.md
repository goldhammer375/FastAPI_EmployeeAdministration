# Employee Administration API

> API for administrating employees

Minimal API for administrating employees, offices and departments, and relating eachother, with SQLite or PostgreSQL

## Installation

Because it is a python application, you need to have Python installed.

```sh
pip install -r ./requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

## Usage example

This API supports every CRUD operation, mapped to its corresponding HTTP verb (GET, POST, PATCH, DELETE)

You can see the API details in the `/docs` endpoint

## Development environment

It is recommended to create a Python virtual environment for development, and then install the dependencies:

```sh
python -m venv .venv
```

For development, it is useful to have the following package, which supports hot reload:

```sh
pip install "fastapi[standard]"
```

To create the hot reload environment, you have to execute:

```sh
fastapi dev ./app/main.py
```

## Docker installation

Using only containers

```sh
docker build -t TAG .
docker run -p PORT:8000 -e VARIABLE=VALUE TAG
```

With Docker Compose (using PostgreSQL)

```sh
docker-compose up .
```

 Modify the docker-compose file as you see fit.

### Docker environment variables

```yaml
DB_TYPE=postgres # (sqlite / postgres)
POSTGRES_DB=DB_NAME
POSTGRES_USER=postgres
POSTGRES_PASS=example
DB_HOST=DB_CONTAINER_NAME
```


