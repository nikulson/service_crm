from flask import Response, request
import json

from src import app
from src.lib import db
from src.models import Customer, Technician


@app.route('/technician', methods=['GET', 'POST'])
def technicians():
    if request.method == 'GET':
        technicians = Technician.query.all()
        data = [{'id': t.id, 'name': t.name} for t in technicians]
        return Response(json.dumps(data), mimetype='application/json')
    elif request.method == 'POST':
        data = request.get_json()
        technician = Technician(name=data['name'])
        db.session.add(technician)
        db.session.commit()
        return Response(json.dumps({'id': technician.id}), status=201, mimetype='application/json')


@app.route('/customer', methods=['GET', 'POST'])
def customers():
    if request.method == 'GET':
        customers = Customer.query.all()
        data = [{'id': c.id, 'name': c.name, 'email': c.email} for c in customers]
        return Response(json.dumps(data), mimetype='application/json')
    elif request.method == 'POST':
        data = request.get_json()
        customer = Customer(name=data['name'], email=data['email'])
        db.session.add(customer)
        db.session.commit()
        return Response(json.dumps({'id': customer.id}), status=201, mimetype='application/json')
