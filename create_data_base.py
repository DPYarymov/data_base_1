from app import db, app
from sqlalchemy import create_engine
from accounts.model import Base
from config import config

# from accounts.model import User

engine = create_engine(config, echo=True)


def create_db():
    Base.metadata.create_all(engine)


if __name__ == '__main__':
    create_db()
