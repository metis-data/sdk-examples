Get all songs: [http://localhost:8004/songs](http://localhost:8004/songs)


[![metis](https://static-asserts-public.s3.eu-central-1.amazonaws.com/metis-min-logo.png)](https://www.metisdata.io/)

# SQLAlchemy, Python, FastAPI (Async) and PostgreSQL RESTful API

Using the [Documentation](https://docs.metisdata.io/metis/sdk-integration/python-sqlalchemy) of [Metis](https://app.metisdata.io/).

## Setup

### 1. Installation
1. generate a .env file with the followings:
    ```
    DATABASE_URL=
    METIS_API_KEY=
    METIS_SERVICE_VERSION=
    METIS_SERVICE_NAME=
    METIS_INSTRUMENTATION_STR=
    ```
### docker
- exec `docker-compose up -d --build`
- exec `docker-compose exec web alembic upgrade head`

### otherwise
- install virtual env \
 `python3 -m venv venv`
- activate virtual env \
`. venv/bin/activate`
- install deps \
`pip install -r requirements.txt`
- migrate db \
`alembic upgrade head`
- launch the app: \
`uvicorn app.main:app --env-file ./.env --workers 1 --host 0.0.0.0 --port 8000`