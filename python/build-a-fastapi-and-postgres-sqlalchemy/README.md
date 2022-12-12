[![metis](https://static-asserts-public.s3.eu-central-1.amazonaws.com/metis-min-logo.png)](https://www.metisdata.io/)

# SQLAlchemy, Python, FastAPI (Sync) and PostgreSQL RESTful API

Using the [Documentation](https://docs.metisdata.io/metis/sdk-integration/python-sqlalchemy) of [Metis](https://app.metisdata.io/).

## Setup

### 1. Install
```shell
$ python3 -m venv venv
$ . venv/bin/activate
(venv) $ pip install -r requirements.txt
```

### 2. Setup a local PostgeSQL Database.

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

### 3. Insert API Key
Insert your api key into `<API_KEY>` at `./main.py line:26`

### 4. Migrate Database
Run \
``` python create_db.py ```

### 5. Run
``` uvicorn main:app ```

### 6. Go to Metis
Navigate to [Metis](https://app.metisdata.io) to view your recent activity.

# You're all set! 🎉 
Fore more info visit our - [Documentation](https://docs.metisdata.io)
