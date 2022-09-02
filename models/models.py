from app import db
from flask_login import UserMixin


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    agency = db.Column(db.Integer)
    login = db.Column(db.String(100), unique=True)
    name = db.Column(db.String(1000))
    password = db.Column(db.String(100))
    admin = db.Column(db.Boolean, default=False)
    registers = db.relationship('Register', backref='user', lazy=True)


class Register(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    contact = db.Column(db.String(50), nullable=False)
    channel = db.Column(db.String(50), nullable=False)
    attendance = db.Column(db.String(50), nullable=False)
    associate = db.Column(db.String(50), nullable=False)
    demand = db.Column(db.String(50), nullable=False)
    product_offer = db.Column(db.String(3), nullable=False)
    product = db.Column(db.String(50))
    effective = db.Column(db.String(3))
    time_spent = db.Column(db.String(50), nullable=False)
    time_hour = db.Column(db.String(50), nullable=False)
    manager_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return '<Register %r>' % self.id
