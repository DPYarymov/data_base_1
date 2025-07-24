import bcrypt
from flask import request, jsonify
from accounts.model import User
from app import db
from datetime import datetime, UTC


def hashing_password(password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password


def create_user_controller():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No JSON data provided"}), 400
    except Exception as e:
        return jsonify({"error": f"Invalid JSON format: {str(e)} "}), 400
    try:
        pwd = str(data.get('password'))
        password = hashing_password(pwd)
        user = User(
            first_name=data.get('first_name'),
            last_name=data.get('last_name'),
            description=data.get('description'),
            email=data.get('email'),
            password=password,
        )

        query = db.select(User).where(User.email == user.email, User.is_active == True)
        results = db.session.execute(query)
        if results.one_or_none() is None:
            db.session.add(user)
            db.session.commit()
            return jsonify(user.to_dict()), 201
        else:
            return jsonify(f"User with email '{user.email}' already exists"), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": f"Database error: {str(e)} "}), 500


def user_list_controller():
    try:
        query = db.select(User)
        results = db.session.execute(query)
        users = results.scalars().all()
        response = []
        for user in users:
            response.append(user.to_dict())
        return jsonify(response), 200

    except Exception as e:
        return jsonify({"error": f"Database error: {str(e)} "}), 500


def update_user_controller():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No JSON data provided"}), 400
    except Exception as e:
        return jsonify({"error": f"Invalid JSON format: {str(e)} "}), 400

    uuid = data.get('uuid')
    pwd = str(data.get('password'))
    password = hashing_password(pwd)

    try:
        query = db.select(User).where(User.uuid == uuid, User.is_active == True)
        results = db.session.execute(query)
        user = results.scalar_one_or_none()
        if user is None:
            return jsonify(f"User with uuid {uuid} does not exist"), 404
        else:
            user.first_name = data.get('first_name'),
            user.last_name = data.get('last_name'),
            user.description = data.get('description'),
            user.email = data.get('email'),
            user.password = password,
            user.role = data.get('role'),

            db.session.commit()
            return jsonify(f"User with uuid {uuid} has been updated"), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": f"Database error: {str(e)} "}), 500


def delete_user_controller():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No JSON data provided"}), 400
    except Exception as e:
        return jsonify({"error": f"Invalid JSON format: {str(e)} "}), 400

    uuid = data.get('uuid')

    try:
        query = db.select(User).where(User.uuid == uuid, User.is_active == True)
        results = db.session.execute(query)
        user = results.scalar_one_or_none()
        print(user)
        if user is None:
            return jsonify(f"User with uuid {uuid} does not exist"), 404

        else:
            # db.session.delete(user)
            user.is_active = False
            db.session.commit()
            return jsonify(f"User with uuid {uuid} has been deleted"), 204

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": f"Database error: {str(e)} "}), 500
