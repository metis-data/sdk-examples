FROM python:3.9

WORKDIR /app

COPY ./* ./

RUN pip install --no-cache-dir --upgrade -r ./requirements.lock

CMD ["APP_CONFIG_FILE=", "uvicorn", "app.main:app"]