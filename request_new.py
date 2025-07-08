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


# '''
# create_user
user = User(None, None, 'alko101', 'alko_102', '111', 'alko101@ya.ru', '102345678', None, None, None)
data = {'first_name': user.first_name, 'last_name': user.last_name, 'description': user.description,
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
response = requests.put('http://localhost:5000/update_user', data=json_data, headers={'Content-Type': 'application/json'})
'''

'''
# delete user
data = {'id': 3}
json_data = json.dumps(data)
response = requests.post('http://localhost:5000/delete_user', data=json_data, headers={'Content-Type': 'application/json'})
'''

print(response.text)
