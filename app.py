from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config

# from accounts import urls


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = config

db = SQLAlchemy(app)

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)



