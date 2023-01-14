from flask import Response, request
import json

from src import app
from src.lib import db
from src.models import Customer


@app.route('/customer', methods=['POST', 'GET'])
def problem():
    if request.method == 'POST':
        data = request.get_json()
        customer = Customer(name=data.get('name'), email=data.get('email'))
        db.session.add(customer)
        db.session.commit()
        return Response("", status=201)

    if request.method == 'GET':
        customers = Customer.query.all()
        response = [
            {
                'id': customer.id,
                'name': customer.name,
                'email': customer.email
            }
            for customer in customers
        ]
        return Response(
            json.dumps(response),
            status=200,
            mimetype='application/json'
        )
