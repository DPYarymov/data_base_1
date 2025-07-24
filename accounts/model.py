from datetime import datetime, UTC
import uuid as u
from sqlalchemy import Integer, String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.types import UUID
import enum
from flask_validator import ValidateEmail


class RoleEnum(str, enum.Enum):
    USER = "user"
    ADMIN = "admin"


class Base(DeclarativeBase):
    __abstract__ = True

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    date_of_create: Mapped[datetime] = mapped_column(default=datetime.now(UTC))
    date_of_updated: Mapped[datetime] = mapped_column(default=datetime.now(UTC), onupdate=datetime.now(UTC))


class User(Base):
    __tablename__ = 'users'

    uuid: Mapped[UUID] = mapped_column(UUID(as_uuid=True), default=u.uuid4)
    first_name: Mapped[str] = mapped_column(String(50))
    last_name: Mapped[str] = mapped_column(String(50))
    description: Mapped[str] = mapped_column(String(200), nullable=True)
    email: Mapped[str] = mapped_column(String(120), nullable=False)
    password: Mapped[str] = mapped_column(String(165), nullable=False)
    is_active: Mapped[bool] = mapped_column(default=True, nullable=False)
    role: Mapped[RoleEnum] = mapped_column(default=RoleEnum.USER)

    def __init__(self, first_name, last_name, description, email, password, is_active: Mapped[bool] = True):
        self.first_name = first_name
        self.last_name = last_name
        self.description = description
        self.email = email
        self.password = password
        self.is_active = is_active

    @classmethod
    def __declare_last__(cls):
        ValidateEmail(User.email, True, True, throw_exception=True,
                      message="The email is not valid. Please check it")

    def __repr__(self):
        return f' {self.uuid} {self.first_name} {self.last_name} {self.email}'

    def to_dict(self):
        return {
            'uuid': self.uuid,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'description': self.description,
            'email': self.email,
            'date_of_create': self.date_of_create,
            'date_of_updated': self.date_of_updated,
            'role': self.role,
        }
