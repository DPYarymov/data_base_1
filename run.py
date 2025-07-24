from accounts.urls import users
from app import create_app
import loging

app = create_app()


app.register_blueprint(users)

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
