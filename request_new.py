from flask import jsonify
import requests
import json
from accounts.model import User


# '''
# create_user
user = User('drink06', 'bear06', '111', 'drink07@ya.ru', '012345678')
# data = {'first_name': 'cola', 'last_name': 'cocacola', 'description': '123',
#         'email': 'drink07@ya.ru', 'password': '012345678'}

data = {'first_name': user.first_name, 'last_name': user.last_name, 'description': user.description,
        'email': user.email, 'password': user.password}
# print(user.email)
json_data = json.dumps(data)
response = requests.post('http://localhost:5000/create_user', data=json_data,
                         headers={'Content-Type': 'application/json'})
print(response.text)
print(response)
# '''

'''
# user_list
response = requests.get('http://localhost:5000/user_list')
print(response.text)
'''

'''
# update user
user = User('cola02', 'cocacola', '111', 'drink09@ya.ru', '012345678')
data = {'uuid': "26538697-eb67-4412-b467-b9eb90cde5c3", 'first_name': user.first_name,
        'last_name': user.last_name, 'description': user.description, 'email': user.email, 'password': user.password,
        'role': 'admin'}
json_data = json.dumps(data)
response = requests.put('http://localhost:5000/update_user', data=json_data,
                        headers={'Content-Type': 'application/json'})
print(response.text)
'''

'''
# delete user
data = {'uuid': "b8c20af5-0bc7-4c45-a833-cf3a6c91c764"}
json_data = json.dumps(data)
response = requests.post('http://localhost:5000/delete_user', data=json_data,
                         headers={'Content-Type': 'application/json'})
print(response.text)
print(response)
# '''
