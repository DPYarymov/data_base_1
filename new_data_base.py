import psycopg2


db_params = {
    "host": "localhost",
    "database": "postgres",
    "user": "postgres",
    "password": "123",
    "port": 5432
}
print(db_params)
try:
    conn = psycopg2.connect(**db_params)
    conn.autocommit = True  # Включаем авто-коммит

    # Создаем курсор
    cursor = conn.cursor()

    # SQL-запрос для создания новой базы данных
    create_db_query = "CREATE DATABASE data_base_1           ;"

    # Выполняем запрос
    cursor.execute(create_db_query)

    print("База данных 'data_base_1' успешно создана.")

except psycopg2.Error as e:
    print(f"Ошибка при работе с PostgreSQL: {e}")

# finally:
#     if conn:
#         cursor.close() # Закрываем курсор
#         conn.close()   # Закрываем соединение