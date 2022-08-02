import psycopg2

host = 'ec2-107-22-122-106.compute-1.amazonaws.com'
database = 'd77p6occqh3l06'
user = 'lvvzdmtzkaejme'
password = '01a8ca75afdd409f83fbd5f72d7649c908536c478292727b537023eaad374eda'
port = 5432

cur = None

try:
    conn = psycopg2.connect(host=host,
                            database=database,
                            user=user,
                            password=password,
                            port=port)
    cur = conn.cursor()
    create_table = """CREATE TABLE IF NOT EXISTS users(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
    )
    """
    new_user = ("Camilo Acosta", "cacosta@yahoo.com", "c123456")
    insert_users = "INSERT INTO users(name, email, password) VALUES (%s, %s, %s)"

    cur.execute(insert_users, new_user)
    conn.commit()
except Exception as Error:
    print(Error)
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()
