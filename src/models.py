from src.lib import db
from datetime import datetime


# class Technician(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), unique=True)


class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    email = db.Column(db.String(100), unique=True)


# class Car(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     vin = db.Column(db.String(100), unique=True)
#     customer_id = db.Column(db.Integer, db.ForeignKey('Customer.id'))
#
#
# class Car_part(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), unique=True)
#     make = db.Column(db.String(100))
#     model = db.Column(db.String(100), unique=True)
#     serie = db.Column(db.String(100), unique=True)
#     count = db.Column(db.Integer, unique=True)
#
#
# class Problem(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     symptome = db.Column(db.String(100))
#     technician_id = db.Column(db.Integer, db.ForeignKey('technician.id'))
#     car_id = db.Column(db.Integer, db.ForeignKey('car.id'))
#     status = db.Column(db.String(100))
#     created_at = db.Column(db.DateTime, default=datetime.utcnow)
#
#     def __repr__(self):
#         return '<Problem %r> % self.id'
#
#
# class Problem_procurement(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     problem_id = db.Column(db.Integer, db.ForeignKey('problem.id'))
#     car_part_id = db.Column(db.Integer, db.ForeignKey('car_part.id'))
#     car_part_count = db.Column(db.Integer, unique=True)
