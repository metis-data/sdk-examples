[![HitCount](http://hits.dwyl.io/ro6ley/cars_in_a_flask.svg)](http://hits.dwyl.io/ro6ley/cars_in_a_flask)

# Cars in a Flask

This repository contains the code for this [blogpost](https://stackabuse.com/using-sqlalchemy-with-flask-and-postgresql/).


## Getting Started

### Prerequisites

Kindly ensure you have the following installed:
- [ ] [Python 3.6](https://www.python.org/downloads/release/python-365/)
- [ ] [Pip](https://pip.pypa.io/en/stable/installing/)
- [ ] [Virtualenv](https://virtualenv.pypa.io/en/stable/installation/)
- [ ] [PostgreSQL](https://www.postgresql.org/)

### Setting up + Running

1. Clone the repo:

    ```
    $ git clone https://github.com/ro6ley/cars_in_a_flask.git
    $ cd cars_in_a_flask
    ```

2. With Python 3.6 and Pip installed:

    ```
    $ virtualenv env 
    $ source env/bin/activate
    $ pip install -r requirements.txt
    ```

3. Export the required environment variables:

    ```
    $ export FLASK_APP=app.py
    ```

4. Execute the migrations to create the `cars` table:

    ```
    $ ./env/bin/flask  db migrate
    $ ./env/bin/flask  db upgrade
    ```

5. Run the Flask API:

    ```
    $ ./env/bin/flask  run
    ```

6. Navigate to `http://localhost:5000/cars` to view the cars data.

## Contribution

Please feel free to raise issues using this [template](./.github/ISSUE_TEMPLATE.md) and I'll get back to you.

You can also fork the repository, make changes and submit a Pull Request using this [template](./.github/PULL_REQUEST_TEMPLATE.md).
