from flask import jsonify
import requests
import json
from accounts.model import User

# user_id: Mapped[int] = mapped_column(primary_key=True, index=True)
#     user_uuid: Mapped[str] = mapped_column(db.UUID(as_uuid=True), default=uuid.uuid4)
#     first_name: Mapped[str] = mapped_column(String(50))
#     last_name: Mapped[str] = mapped_column(String(50))
#     description: Mapped[str] = mapped_column(String(150))
#     email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
#     password: Mapped[str] = mapped_column(String(165), nullable=False)
#     date_of_create: Mapped[datetime] = mapped_column(default=datetime.now, nullable=False)
#     is_activ: Mapped[bool] = mapped_column(default=True, nullable=False)
#     role: Mapped[str] = mapped_column(String(10), default="user", nullable=False)


'''
# create_user
user = User('drink01', 'bear01', '111', 'drink09@ya.ru', '012345678')
data = {'first_name': user.first_name, 'last_name': user.last_name, 'description': user.description,
        'email': user.email, 'password': user.password}
json_data = json.dumps(data)
response = requests.post('http://localhost:5000/create_user', data=json_data,
                         headers={'Content-Type': 'application/json'})
print(response.text)
'''

'''
# user_list
response = requests.get('http://localhost:5000/user_list')
print(response.text)
'''

# '''
# update user
user = User('cola', 'cocacola', '111', 'drink09@ya.ru', '012345678')
data = {'user_uuid': "26538697-eb67-4412-b467-b9eb90cde5c3", 'first_name': user.first_name,
        'last_name': user.last_name, 'description': user.description, 'email': user.email, 'password': user.password,
        'role': 'admin'}
json_data = json.dumps(data)
response = requests.put('http://localhost:5000/update_user', data=json_data,
                        headers={'Content-Type': 'application/json'})
print(response.text)
# '''

'''
# delete user
data = {'user_uuid': "67714d59-e98b-46b9-b528-3d01dfd7b4b7"}
json_data = json.dumps(data)
response = requests.post('http://localhost:5000/delete_user', data=json_data,
                         headers={'Content-Type': 'application/json'})
print(response.text)
print(response)
'''
