from .db import db
from sqlalchemy import inspect


class BaseMixin(db.Model):
    __abstract__ = True

    def __int__(self, **kwargs):
        self.__dict__.update(kwargs)

    def to_dict(self):
        return {c.key: getattr(self, c.key)
                for c in inspect(self).mapper.column_attrs}


class Employee(BaseMixin):
    __tablename__ = 'employees'

    id = db.Column(db.Integer, primary_key=True)
    surname = db.Column(db.String(30), nullable=False)
    name = db.Column(db.String(30), nullable=False)
    patronymic = db.Column(db.String(30), nullable=False)
    address = db.Column(db.String(100), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)


class Position(BaseMixin):
    __tablename__ = 'positions'

    id = db.Column(db.Integer, primary_key=True)
    position = db.Column(db.String(50), nullable=False)


class Division(BaseMixin):
    __tablename__ = 'divisions'

    id = db.Column(db.Integer, primary_key=True)
    division = db.Column(db.String, nullable=False)


class Job(BaseMixin):
    __tablename__ = 'job'

    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employees.id'), nullable=True)
    position_id = db.Column(db.Integer, db.ForeignKey('positions.id'), nullable=True)
    division_id = db.Column(db.Integer, db.ForeignKey('divisions.id'), nullable=True)
    date_of_employment = db.Column(db.Date, nullable=True)
    date_of_dismissal = db.Column(db.Date, nullable=False)
