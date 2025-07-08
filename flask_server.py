from flask import Flask
from flask import request
import psycopg2
import bcrypt
from psycopg2 import errors
from request import User

db_params = {
    "host": "localhost",
    "database": "data_base_1",
    "user": "postgres",
    "password": "123",
    "port": 5432
}

app = Flask(__name__)

conn = None


@app.before_first_request
def initialize_database_connection():
    global conn
    try:
        conn = psycopg2.connect(database="flask_db",
                                user="postgres",
                                password="root",
                                host="localhost", port="5432")
    except psycopg2.Error as e:
        print(f"Ошибка подключения к базе данных: {e}")
        raise


@app.teardown_appcontext
def close_database_connection(exception=None):
    global conn
    if conn is not None:
        conn.close()
        print("Соединение с базой данных закрыто.")


def hashing_password(password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password


def check_password(password, hashed_password):
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)


def get_user_data_from_request():
    try:
        data = request.get_json()
        first_name = data.get('user_name')
        last_name = data.get('user_second_name')
        description = data.get('description')
        email = data.get('email')
        password = data.get('password')
        hash_password = hashing_password(password)
        return first_name, last_name, description, email, hash_password
    except Exception as e:
        print(f"Ошибка при обработке request: {e}")


def user_exists(email):
    try:
        cursor.execute('''SELECT EXISTS (SELECT 1 FROM users WHERE email = %s);''', (email,))
        exists = cursor.fetchone()[0]
        return exists
    except psycopg2.Error as e:
        print(f"Ошибка при работе с PostgresSQL: {e}")


def insert_user(first_name, last_name, description, email, hash_password):
    try:
        cursor.execute(
            '''INSERT INTO users
             (first_name, last_name, description, email, password)
             VALUES
             (%s, %s, %s, %s, %s)''',
            (first_name, last_name, description, email, hash_password))
        conn.commit()
        return f"User has been successfully added"
    except psycopg2.Error as e:
        print(f"Ошибка при работе с PostgresSQL: {e}")


# @app.route('/create_user', methods=['POST'])
# def add_user():
#     first_name, last_name, description, email, hash_password = get_user_data_from_request()
#     sql = user_exists(email)
#     if sql is False:
#         insert_user()
#     else:
#         return f"User with email '{email}' already exists"
#
#
# def add_user():
#     data = request.get_json()
#     first_name = data.get('user_name')
#     last_name = data.get('user_second_name')
#     description = data.get('description')
#     email = data.get('email')
#     password = data.get('password')
#
#     # user = User()
#     # user.add_db(conn)
#
#     hash_password = hashing_password(password)
#
#     conn = None
#     cursor = None
#     try:
#         conn = psycopg2.connect(**db_params)
#         cursor = conn.cursor()
#         cursor.execute('''SELECT EXISTS (SELECT 1 FROM users WHERE email = %s);''', (email,))
#         sql = cursor.fetchone()[0]
#         if sql is False:
#             cursor.execute(
#                 '''INSERT INTO users
#                  (first_name, last_name, description, email, password)
#                  VALUES
#                  (%s, %s, %s, %s, %s)''',
#                 (first_name, last_name, description, email, hash_password))
#             conn.commit()
#             return f"User has been successfully added"
#
#         else:
#             return f"User with email '{email}' already exists"
#
#     except psycopg2.Error as e:
#         print(f"Ошибка при работе с PostgresSQL: {e}")
#
#     finally:
#         if conn:
#             cursor.close()
#             conn.close()


@app.route('/user_list', methods=['GET'])
def list_of_user():
    conn = None
    cursor = None
    try:
        conn = psycopg2.connect(**db_params)
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM users''')
        data = cursor.fetchall()
        return data

    except psycopg2.Error as e:
        print(f"Ошибка при работе с PostgresSQL: {e}")

    finally:
        if conn:
            cursor.close()
            conn.close()


@app.route('/update_user', methods=['PUT'])
def update_user():
    data = request.get_json()
    id = data.get('id')
    first_name = data.get('user_name')
    last_name = data.get('user_second_name')
    description = data.get('description')
    email = data.get('email')
    password = data.get('password')

    conn = None
    cursor = None
    try:
        conn = psycopg2.connect(**db_params)
        cursor = conn.cursor()
        cursor.execute('''SELECT EXISTS (SELECT 1 FROM users WHERE id = %s);''', (id,))
        sql = cursor.fetchone()[0]
        if sql:
            cursor.execute('''UPDATE users SET first_name=%s, \
            last_name=%s, description=%s, email=%s, password=%s
            WHERE id = %s;''', (first_name, last_name, description, email, password, id))

            conn.commit()
            return f"User with id '{id}' has been successfully update"

        else:
            return f"User with id '{id}' does not exist"

    except psycopg2.Error as e:
        print(f"Ошибка при работе с PostgresSQL: {e}")

    finally:
        if conn:
            cursor.close()
            conn.close()


@app.route('/delete_user', methods=['POST'])
def del_user():
    data = request.get_json()
    id = data.get('id')

    conn = None
    cursor = None
    try:
        conn = psycopg2.connect(**db_params)
        cursor = conn.cursor()
        cursor.execute('''SELECT EXISTS (SELECT 1 FROM users WHERE id = %s);''', (id,))
        sql = cursor.fetchone()[0]
        if sql:
            cursor.execute('''DELETE FROM users WHERE id=%s;''', (id,))
            conn.commit()
            return f"User with id '{id}' has been deleted"

        else:
            return f"User with id '{id}' does not exist"
    except psycopg2.Error as e:
        print(f"Ошибка при работе с PostgresSQL: {e}")

    finally:
        if conn:
            cursor.close()
            conn.close()


if __name__ == '__main__':

    app.run(debug=True, host='127.0.0.1', port=5000)

    # conn = None
    # cursor = None
    # try:
    #     conn = psycopg2.connect(**db_params)
    #     cursor = conn.cursor()
    #
    # except psycopg2.Error as e:
    #     print(f"Ошибка при работе с PostgresSQL: {e}")
    # finally:
    #     if conn:
    #         if cursor:
    #             cursor.close()
    #         conn.close()
