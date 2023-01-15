[![metis](https://static-asserts-public.s3.eu-central-1.amazonaws.com/metis-min-logo.png)](https://www.metisdata.io/)

# SQLAlchemy, Python, FastAPI (Async) and PostgreSQL RESTful API

Using the [Documentation](https://docs.metisdata.io/metis/sdk-integration/python-sqlalchemy) of [Metis](https://app.metisdata.io/).

## Setup

### 1. Install
```shell
$ python3 -m venv venv
$ . venv/bin/activate
(venv) $ pip install -r requirements.lock
```

### 2. Setup a local PostgreSQL Database.

<ins><b>Option 1</b></ins>: Native PostgreSLQ
- Install [PostgreSQL](https://www.postgresql.org/download/) locally.
- Create a Database with the name 'db'.

<ins><b>Option 2</b></ins>: Docker Database
```shell
(venv) $ docker run -d --name db \
  -e POSTGRES_PASSWORD=password \
  -e PGDATA=/var/lib/postgresql/data/pgdata \
  -v $(pwd)/pgdata:/var/lib/postgresql/data \
  -p 5432:5432 \
  postgres:14.4-alpine
```

### 3. Migrate Database
Run
```
(venv) $ APP_CONFIG_FILE=local alembic upgrade head
```

### 4. Insert API Key
Insert your api key into `<API_KEY>` at `./app/main.py line:21`

## Run

```shell
(venv) $ APP_CONFIG_FILE=local uvicorn app.main:app --reload-dir app
```

### 5. Trigger your Database.
Open [localhost:8000](http://localhost:8000/docs) and play around. 

### 6. Go to Metis
Navigate to [Metis](https://app.metisdata.io/activities) to view your recent activity.

# You're all set! 🎉 
Fore more info vist our - [Documentation](https://docs.metisdata.io)




