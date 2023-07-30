# Metis Flask API - Setup and Run Guide

![metis](https://static-asserts-public.s3.eu-central-1.amazonaws.com/metis-min-logo.png)

## Introduction

This guide provides instructions on setting up and running the Metis Flask API. The Metis Flask API allows you to interact with the Metis platform and query aircraft data using a web interface. It offers two methods for running the API: running directly from the terminal or using Docker.

## Prerequisites

Before you begin, ensure that you have the following software installed on your system:

- [Python 3.6](https://www.python.org/downloads/release/python-365/)
- [Pip](https://pip.pypa.io/en/stable/installing/)
- [Virtualenv](https://virtualenv.pypa.io/en/latest/installation.html)
- [PostgreSQL](https://www.postgresql.org/)
- [Docker](https://www.docker.com/)

## Setting up and Running the API

### Method 1: Running from Terminal

1. Clone the repository from the [Metis GitHub](https://github.com/metis-data/metis-flask-api).

2. Open a terminal and navigate to the project directory.

3. Create a virtual environment and activate it using the following command: 
```
virtualenv env && source env/bin/activate
```


4. Install the required dependencies using Pip from the `requirements.txt` file: 

 ```
 pip install -r requirements.txt
 ```

5. Obtain your Metis API key and put it in the `.env` file in the project directory.

6. Run the Flask API: 
 ```
 ./env/bin/flask  run
```


7. Access the API in your web browser at [http://127.0.0.1:5000/all_aircraft](http://127.0.0.1:5000/all_aircraft).

8. Open the Metis app and the query span to interact with the API.

### Method 2: Running using Docker

1. Clone the repository from the [Metis GitHub](https://github.com/metis-data/metis-flask-api).

2. Open a terminal and navigate to the project directory.

3. Obtain your Metis API key and replace `METIS_API_KEY` with your API key in the `Dockerfile`.

4. Build the Docker image using the following command:


5. Run the Docker container and map the host port to the container port:


6. Access the API in your web browser at [http://localhost:8080/aircraft](http://localhost:5000/all_aircraft).
