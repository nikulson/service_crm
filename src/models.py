from src.lib import db
from datetime import datetime


class Technician(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)


class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)


# class Car(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     vin = db.Column(db.String(100), unique=True, nullable=False)
#     customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
#
#
# class CarPart(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), nullable=False)
#     make = db.Column(db.String(100))
#     model = db.Column(db.String(100))
#     series = db.Column(db.String(100))
#     count = db.Column(db.Integer, nullable=False)
#     price = db.Column(db.Float, nullable=False)
#
#
# class Problem(db.Model):
#     STATUS_CHOICES = [('in_progress', 'In Progress'), ('completed', 'Completed')]
#
#     id = db.Column(db.Integer, primary_key=True)
#     description = db.Column(db.String(100), nullable=False)
#     technician_id = db.Column(db.Integer, db.ForeignKey('technician.id'), nullable=False)
#     car_id = db.Column(db.Integer, db.ForeignKey('car.id'), nullable=False)
#     status = db.Column(db.String(20), nullable=False, default='in_progress', server_default='in_progress',
#                        index=True, choices=STATUS_CHOICES)
#     created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
#     completed_at = db.Column(db.DateTime)
#     parts = db.relationship('ProblemPart', backref='problem', lazy=True)
#     total_price = db.Column(db.Float, nullable=False, default=0)
#
#     def calculate_price(self):
#         total_price = 0
#         for problem_part in self.parts:
#             car_part = CarPart.query.get(problem_part.car_part_id)
#             if car_part is not None:
#                 total_price += problem_part.count * car_part.price
#         self.total_price = total_price
#
#
# class ProblemPart(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     problem_id = db.Column(db.Integer, db.ForeignKey('problem.id'), nullable=False)
#     car_part_id = db.Column(db.Integer, db.ForeignKey('car_part.id'), nullable=False)
#     count = db.Column(db.Integer, nullable=False)


