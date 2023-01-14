from flask import Response, request

from src import app
from src.lib import db
from src.models import Customer


@app.route('/customer', methods=['POST', 'GET'])
def problem():
    if request.method == 'POST':
        # customer = Customer()
        db.create_all()
        return Response("{'a':'b'}", status=201, mimetype='application/json')

    if request.method == 'GET':
        return Response("{'a':'b'}", status=200, mimetype='application/json')
