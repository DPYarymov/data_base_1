from flask import Flask
from flask import jsonify

# Создаем экземпляр Flask приложения
app = Flask(__name__)


class User():
    def __init__(self, name, second_name):
        self.name = name
        self.second_name = second_name

    def __str__(self):
        return f'{self.name} {self.second_name}'


# Эндпоинт для корневого URL
@app.route('/', methods=['POST'])
def home():
    user = User("pivasik", "pivasik_2")

    return jsonify([{'user_name': user.name, 'user_second_name': user.second_name}]), 200
                    # {'user_name': user.name, 'user_second_name': user.second_name}]), 200


# @app.route('/user_list')
# def home():
#     user = User("pivasik", "pivasik_2")
#
#
#
#     return  jsonify([{'user_name': user.name, 'user_second_name': user.second_name }, {'user_name': user.name, 'user_second_name': user.second_name }])


# Эндпоинт с персональным приветствием
@app.route('/hello/<name>')
def hello(name):
    return f"Привет, {name}!"


# @app.route('/add_user')
# def add_user():
#     print(request)
#     return f"Привет, {name}!"

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
