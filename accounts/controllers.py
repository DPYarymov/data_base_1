import psycopg2
import bcrypt
import uuid
from flask import request, jsonify
from app import db
from model import User
from psycopg2 import errors


def hashing_password(password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password


def create_user_controller():
    request_form = request.form.to_dict()
    password = hashing_password(request_form['password'])
    user = User(
        first_name=request_form.get('first_name'),
        last_name=request_form.get('last_name'),
        description=request_form.get('description'),
        email=request_form.get('email'),
        password=password,
    )

    db.session.add(user)
    db.session.commit()

    response = user, 200
    return jsonify(response)

# не проверяем, есть ли уже юзер в базе
# где создаем БД, и табл? (креайт олл)





