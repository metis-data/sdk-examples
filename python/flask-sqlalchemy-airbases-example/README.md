
## Run from terminal
### Prerequisites

Kindly ensure you have the following installed:
- [ ] [Python 3.6](https://www.python.org/downloads/release/python-365/)
- [ ] [Pip](https://pip.pypa.io/en/stable/installing/)
- [ ] [Virtualenv](https://virtualenv.pypa.io/en/stable/installation/)
- [ ] [PostgreSQL](https://www.postgresql.org/)

### Setting up + Running

1. With Python 3.6 and Pip installed:
    ```
     virtualenv env && source env/bin/activate && pip install -r requirements.txt
    ```

2. Run the Flask API:
    ```
     ./env/bin/flask  run
    ```

3. Navigate to [http://127.0.0.1:5000/aircraft](http://127.0.0.1:5000/aircraft).

4. Open Metis app app and the query span.

## Run  using docker

1.   ``` 
      docker build -t flask-app .
     ```
    
2.  ```
     docker run -p 8080:5000 flask-app
    ```

3. Navigate to [http://localhost:8080/aircraft](http://localhost:5000/aircraft).

4. Open Metis app app and the query span.


