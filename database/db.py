import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ Создать соединение с SQLite базой данных, указанной в db_file """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn

def execute_sql(conn, sql):
    """ Выполнить SQL-запрос """
    try:
        c = conn.cursor()
        c.execute(sql)
    except Error as e:
        print(e)

def create_tables():
    """ Создать таблицы в базе данных """
    database = "calorie_tracker.db"

    sql_create_users_table = """
    CREATE TABLE IF NOT EXISTS users (
        id integer PRIMARY KEY,
        username text NOT NULL,
        chat_id text NOT NULL
    );
    """

    sql_create_entries_table = """
    CREATE TABLE IF NOT EXISTS entries (
        id integer PRIMARY KEY,
        user_id integer NOT NULL,
        date text NOT NULL,
        calories int,
        description text,
        FOREIGN KEY (user_id) REFERENCES users (id)
    );
    """

    # Создать соединение с базой данных
    conn = create_connection(database)

    # Создать таблицы
    if conn is not None:
        execute_sql(conn, sql_create_users_table)
        execute_sql(conn, sql_create_entries_table)
        conn.close()
    else:
        print("Ошибка! Не удалось создать соединение с базой данных.")
