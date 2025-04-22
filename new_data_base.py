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
    conn = psycopg2.connect(**db_params)
    conn.autocommit = True

    cursor = conn.cursor()

    create_db_query = "CREATE DATABASE data_base_1;"

    try:
        cursor.execute(create_db_query)
        print("База данных 'data_base_1' успешно создана.")
    except errors.DuplicateDatabase as e:
        print(f"База данных 'data_base_1' уже существует. Пропускаем создание.")


except psycopg2.Error as e:
    print(f"Ошибка при работе с PostgreSQL: {e}")

finally:
    if conn:
        cursor.close() # Закрываем курсор
        conn.close()   # Закрываем соединение




