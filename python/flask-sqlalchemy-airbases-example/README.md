# Metis Flask API - Setup and Run Guide

![metis](https://static-asserts-public.s3.eu-central-1.amazonaws.com/metis-min-logo.png)

## Introduction
In this short demo you will create a simple Python web app (Flask) which calls a PostgreSQL database using SQLAlchemy. 

### Demo Flow
- **Install** the prerequisites python libraries in a new environment.
- **Configure** the app using a configuration file. You just need to rovide a **Metis API Key**. The Demo Postgres server is up and running so you won’t need to create it. We provide a connection string. 
- **Run the Flask web server** locally
- **Call the REST command**  http://localhost:5000. The request takes long seconds to run since it is not efficient. When the query finishes, the web app shows the data (as JSON).  
- **View the traces** in Metis Web App. View the SQL command, its execution plan and the SQL insights.


## Step 1: Prerequisites

Before you begin, ensure that you have the following software installed on your system:

- [Python 3.6](https://www.python.org/downloads/release/python-365/) or higher
- [Pip](https://pip.pypa.io/en/stable/installation/)
- [Virtualenv](https://virtualenv.pypa.io/en/latest/installation.html)

## Step 2: Run the Flask Web App

### Method 1: Running the code locally, using a Terminal

1. Clone the repository from the [Metis GitHub](https://github.com/metis-data/sdk-examples/tree/main/python/flask-sqlalchemy-airbases-example).
2. Open a terminal and navigate to the project directory.

3. Create a virtual environment and activate it using the following command: 
```
virtualenv env && source env/bin/activate
```


4. Install the required dependencies using Pip from the `requirements.txt` file: 

 ```
 pip install -r requirements.txt
 ```

5. Obtain your Metis API key and put it in the `.env.dev` file in the project directory. (don't forget to rename the file to `.env`)

6. Run the Flask API: 
 ```
 ./env/bin/flask  run
```

- **Call the REST command**  http://localhost:5000.  



### Method 2: Running using Docker

1. Clone the repository from the [Metis GitHub](https://github.com/metis-data/metis-flask-api).

2. Open a terminal and navigate to the project directory.

3. Obtain your Metis API key and replace `METIS_API_KEY` with your API key in the `Dockerfile`.

4. Build the Docker image using the following command:

5. Run the Docker container and map the host port to the container port:

6. Access the API in your web browser at [http://localhost:5000](http://localhost:5000).

## Step 3: Review the Traces in Metis Web App
Open the Metis web app.  and the query span to interact with the API.



