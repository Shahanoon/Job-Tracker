import psycopg2

def get_connection():
    conn = psycopg2.connect(
        host="localhost",
        database="jobtracker",
        user="postgres",
        password=""
    )
    return conn