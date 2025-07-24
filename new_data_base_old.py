import psycopg2
from psycopg2 import errors

db_params = {
    "host": "localhost",
    "database": "postgres",
    "user": "postgres",
    "password": "123",
    "port": 5432
}

conn = None
cursor = None

try:
    # создаем БД
    conn = psycopg2.connect(**db_params)
    conn.autocommit = True

    cursor = conn.cursor()

    create_db_query = "CREATE DATABASE data_base_1;"

    try:
        cursor.execute(create_db_query)
        print("База данных 'data_base_1' успешно создана.")
    except errors.DuplicateDatabase as e:
        print(f"База данных 'data_base_1' уже существует. Пропускаем создание.")

    db_connect_params = db_params.copy()
    db_connect_params["database"] = "data_base_1"

    if conn:  # Закрываем старое соединение, если оно было открыто
        cursor.close()
        conn.close()

    conn = psycopg2.connect(**db_connect_params)
    conn.autocommit = True
    cursor = conn.cursor()

    # Создание таблицы users
    create_table_query = """
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        uuid DEC(36),
        first_name VARCHAR(50) NOT NULL,
        last_name VARCHAR(50) NOT NULL,
        description VARCHAR(150),
        email VARCHAR(50) NOT NULL,
        password VARCHAR(165) NOT NULL,
        date_of_create TIMESTAMP NULL,
        is_activ BOOLEAN     
    );
    """
    cursor.execute(create_table_query)
    print("Таблица 'users' успешно создана (или уже существует).")


except psycopg2.Error as e:
    print(f"Ошибка при работе с PostgresSQL: {e}")

finally:
    if conn:
        cursor.close()
        conn.close()
