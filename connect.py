# db_connection.py

import psycopg2

def create_connection():
    """
    Establishes a connection to the PostgreSQL database.
    You need to update the following parameters:
    - dbname: The name of your database
    - user: Your PostgreSQL username
    - password: Your PostgreSQL password
    - host: The host of your PostgreSQL server (default is 'localhost')
    - port: The port your PostgreSQL server is listening on (default is '5432')
    """
    conn = psycopg2.connect(
        dbname="ADBMS_WEB",
        user="postgres",
        password="postgres",
        host="localhost",
        port="5432"
    )
    return conn
