from datetime import datetime
import uuid
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.types import UUID


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'

    user_id: Mapped[int] = mapped_column(primary_key=True, index=True)
    user_uuid: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), default=uuid.uuid4)
    # user_uuid: Mapped[str] = mapped_column(db.UUID(as_uuid=True), default=uuid.uuid4)
    # user_uuid: Mapped[str] = mapped_column(String(150), unique=True, nullable=False)
    first_name: Mapped[str] = mapped_column(String(50))
    last_name: Mapped[str] = mapped_column(String(50))
    description: Mapped[str] = mapped_column(String(200), nullable=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(165), nullable=False)
    date_of_create: Mapped[datetime] = mapped_column(default=datetime.now, nullable=False)
    is_activ: Mapped[bool] = mapped_column(default=True, nullable=False)
    role: Mapped[str] = mapped_column(String(10), default="user", nullable=False)

    def __init__(self, first_name, last_name, description, email, password, is_activ: Mapped[bool] = True,
                 role: Mapped[str] = 'user'):
        # super().__init__()
        # self.user_id = user_id
        # self.user_uuid = user_uuid
        self.first_name = first_name
        self.last_name = last_name
        self.description = description
        self.email = email
        self.password = password
        # self.date_of_create = date_of_create
        self.is_activ = is_activ
        self.role = role

    def __repr__(self):
        return f' {self.user_uuid} {self.first_name} {self.last_name} {self.email} {self.date_of_create}'

    def to_dict(self):
        return {
            'user_uuid': self.user_uuid,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'description': self.description,
            'email': self.email,
            'date_of_create': self.date_of_create,
            'role': self.role,
        }
