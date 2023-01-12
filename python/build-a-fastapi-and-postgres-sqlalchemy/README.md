[![metis](https://static-asserts-public.s3.eu-central-1.amazonaws.com/metis-min-logo.png)](https://www.metisdata.io/)

# SQLAlchemy, Python, FastAPI (Sync) and PostgreSQL RESTful API

Using the [Documentation](https://docs.metisdata.io/metis/sdk-integration/python-sqlalchemy) of [Metis](https://app.metisdata.io/).

## Pre-requisites:
1. Setup a local PostgeSQL Database.

    The example projects expects a postgres database, that has a user with name `postgres` and password as `postgres`.

    <ins><b>Option 1</b></ins>: Native PostgreSLQ
    - Install [PostgreSQL](https://www.postgresql.org/download/) locally.
    - Create a Database with the name `db`.

    <ins><b>Option 2</b></ins>: Docker Database
      ```shell
      (venv) $ docker run -d --name db \
      -e POSTGRES_PASSWORD=postgres \
      -e PGDATA=/var/lib/postgresql/data/pgdata \
      -v $(pwd)/pgdata:/var/lib/postgresql/data \
      -p 5432:5432 \
      postgres:14.4-alpine
      ```

2. generate .env file with the followings:
    ```
    DATABASE_URL=
    METIS_API_KEY=
    PORT=
    METIS_SERVICE_NAME=
    ```
3. Migrate Database 

    ``` python create_db.py ```
## Setup

- ### using docker
  - build image

    ```docker build -t sync_fastapi:latest .```
  - run container

    ```docker run --name sync_fastapi_container -p 8080:1234 --env-file ./.env    sync_fastapi:latest```

- ### otherwise

  - Install

    ```shell
    $ python3 -m venv venv
    $ . venv/bin/activate
    (venv) $ pip install -r requirements.txt
    ```

  - Run
  ``` python main.py ```

Go to Metis
Navigate to [Metis](https://app.metisdata.io) to view your recent activity.

# You're all set! 🎉 
Fore more info visit our - [Documentation](https://docs.metisdata.io)
