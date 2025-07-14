from accounts.urls import users
from nit import create_app


app = create_app()


app.register_blueprint(users)

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)



