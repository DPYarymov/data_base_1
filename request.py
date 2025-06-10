from flask import jsonify
import requests
import json


class User():
    def __init__(self, id, name, second_name, description, email, password):
        self.id = id
        self.name = name
        self.second_name = second_name
        self.description = description
        self.email = email
        self.password = password

    def __str__(self):
        return f'{self.name} {self.second_name} {self.description} {self.email} {self.password}'


# '''
# create_user
user = User(1, 'alko', 'alko_2', '111', 'alko@ya.ru', '12345678')
data = {'user_name': user.name, 'user_second_name': user.second_name, 'description': user.description,
        'email': user.email, 'password': user.password}
json_data = json.dumps(data)
response = requests.post('http://localhost:5000/create_user', data=json_data,
                         headers={'Content-Type': 'application/json'})
# '''

'''
# user_list
user = User(1, 'viskarik', 'viskarik_2', '122', 'user2@ya.ru', 'password')
response = requests.get('http://localhost:5000/user_list')
print(response.text)
'''

'''
# update user
user = User(1, 'viskarik', 'viskarik_2', '122', 'user2@ya.ru', 'password')
data = {'id': user.id, 'user_name': user.name, 'user_second_name': user.second_name, 'description': user.description,
        'email': user.email, 'password': user.password}
json_data = json.dumps(data)
response = requests.post('http://localhost:5000/update_user', data=json_data, headers={'Content-Type': 'application/json'})
'''

'''
# delete user
data = {'id': 3}
json_data = json.dumps(data)
response = requests.post('http://localhost:5000/delete_user', data=json_data, headers={'Content-Type': 'application/json'})
'''

# print(response.text)
