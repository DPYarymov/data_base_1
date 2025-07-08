from app import app

from controllers import create_user_controller


@app.route('/create_user', methods=['POST'])
def add_user():
    return create_user_controller()

