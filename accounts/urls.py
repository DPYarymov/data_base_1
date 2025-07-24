from flask import Blueprint

from accounts.controllers import (create_user_controller, user_list_controller, delete_user_controller,
                                  update_user_controller)

users = Blueprint('users', __name__)


@users.route('/create_user', methods=['POST'])
def add_user():
    return create_user_controller()


@users.route('/user_list', methods=['GET'])
def user_list():
    return user_list_controller()


@users.route('/update_user', methods=['PUT'])
def update_user():
    return update_user_controller()


@users.route('/delete_user', methods=['POST'])
def del_user():
    return delete_user_controller()
