from flask import Flask
from flask import request
import psycopg2
from psycopg2 import errors

db_params = {
    "host": "localhost",
    "database": "data_base_1",
    "user": "postgres",
    "password": "123",
    "port": 5432
}

# Создаем экземпляр Flask приложения
app = Flask(__name__)


# Эндпоинт для корневого URL
@app.route('/create_user', methods=['POST'])
def add_user():
    data = request.get_json()
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
        cursor.execute('''SELECT EXISTS (SELECT 1 FROM table_1 WHERE email = %s);''', (email,))
        sql = cursor.fetchone()[0]
        if sql is False:
            cursor.execute(
                '''INSERT INTO table_1 
                 (first_name, last_name, description, email, password)
                 VALUES
                 (%s, %s, %s, %s, %s)''',
                (first_name, last_name, description, email, password))
            conn.commit()
            return f"User has been successfully added"

        else:
            return f"User with email '{email}' already exists"

    except psycopg2.Error as e:
        print(f"Ошибка при работе с PostgresSQL: {e}")

    finally:
        if conn:
            cursor.close()
            conn.close()


@app.route('/user_list', methods=['GET'])
def list_of_user():
    conn = None
    cursor = None
    try:
        conn = psycopg2.connect(**db_params)
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM table_1;''')
        data = cursor.fetchall()
        return data

    except psycopg2.Error as e:
        print(f"Ошибка при работе с PostgresSQL: {e}")

    finally:
        if conn:
            cursor.close()
            conn.close()


@app.route('/update_user', methods=['POST'])
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
        cursor.execute('''SELECT EXISTS (SELECT 1 FROM table_1 WHERE id = %s);''', (id,))
        sql = cursor.fetchone()[0]
        if sql:
            cursor.execute('''UPDATE table_1 SET first_name=%s, \
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
        cursor.execute('''SELECT EXISTS (SELECT 1 FROM table_1 WHERE id = %s);''', (id,))
        sql = cursor.fetchone()[0]
        if sql:
            cursor.execute('''DELETE FROM table_1 WHERE id=%s;''', (id,))
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

    # r = request.json
    #
    # print(r)
    # return r


# @app.route('/user_list')
# def home():
#     user = User("pivasik", "pivasik_2")
#
#     return  jsonify([{'user_name': user.name, 'user_second_name': user.second_name }, {'user_name': user.name, 'user_second_name': user.second_name }])


# @app.route('/add_user', methods=['POST'])
# def add_user():
#     print(request)
#     return f"Привет, {name}!"

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
