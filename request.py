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


user = User(1, 'viskarik', 'viskarik_2', '122', 'user2@ya.ru', 'password')

'''
# create_user
data = {'user_name': user.name, 'user_second_name': user.second_name, 'description': user.description,
        'email': user.email, 'password': user.password}
json_data = json.dumps(data)
response = requests.post('http://localhost:5000/create_user', data=json_data, headers={'Content-Type': 'application/json'})
'''

# '''
# user_list
response = requests.get('http://localhost:5000/user_list')
print(response.text)
# '''

'''
# update user
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
