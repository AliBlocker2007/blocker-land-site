from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime


db = SQLAlchemy()


class User(UserMixin, db.Model):
id = db.Column(db.Integer, primary_key=True)
username = db.Column(db.String(80), unique=True, nullable=False)
email = db.Column(db.String(120), unique=True, nullable=False)
password = db.Column(db.String(200), nullable=False) # store hashed password in real app
is_admin = db.Column(db.Boolean, default=False)
bookings = db.relationship('Booking', backref='user', lazy=True)


class Booking(db.Model):
id = db.Column(db.Integer, primary_key=True)
user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
date = db.Column(db.Date, nullable=False)
time = db.Column(db.String(20), nullable=False)
created_at = db.Column(db.DateTime, default=datetime.utcnow)
status = db.Column(db.String(20), default='booked') # booked, cancelled


__table_args__ = (
db.UniqueConstraint('date', 'time', name='uix_date_time'),
)
