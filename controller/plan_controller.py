from flask import request as flask_request, jsonify
import requests as py_requests
from config import db, app, host, port
from models.plan import Plan
import utils.utils as utils



#get all
@app.route('/Plan')
def get_plans():
    try: #next convert dao into controller
        url = f'{host}{port}/Data/Plan'
        headers = {'Content-Type': 'application/json'}
        response = py_requests.get(url) #, json=json_data, headers=headers
        response.raise_for_status()  # Raise an exception for HTTP errors
        plans = response.text
        return plans
    except py_requests.exceptions.HTTPError as http_err:
        return (f"HTTP error occurred: {http_err}")
    except Exception as err:
        return (f"An error occurred: {err}")

#get by id
@app.route('/Plan/<id>')
def get_plan_by_id(id):
    try:
        url = f'{host}{port}/Data/Plan/{id}'
        response = py_requests.get(url)
        response.raise_for_status()
        plan = response.text
        return plan
    except py_requests.exceptions.HTTPError as http_err:
        return (f"HTTP error occurred: {http_err}")
    except Exception as err:
        return (f"An error occurred: {err}")

#get_under_price
@app.route('/Plan/Price/<price>')
def get_plan_under_price(price):
    try:
        url = f'{host}{port}/Data/Plan/Price/{price}'
        response = py_requests.get(url) #, json=json_data, headers=headers
        response.raise_for_status()  # Raise an exception for HTTP errors
        plans = response.text
        return plans
    except py_requests.exceptions.HTTPError as http_err:
        return (f"HTTP error occurred: {http_err}")
    except Exception as err:
        return (f"An error occurred: {err}")

#add
@app.route('/Plan/Add', methods=['POST'])
def add_plan():
    try:
        url = f'{host}{port}/Data/Plan/Add'
        json = flask_request.get_json()
        if not json:
            return jsonify({"error": "Invalid JSON data"}), 400
        headers = {'Content-Type': 'application/json'}
        response = py_requests.post(url, json=json, headers = headers)
        plan = response.text
        return plan, 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

#remove
@app.route('/Plan/Del/<id>', methods=['DELETE'])
def remove_plan(id):
    try:
        url = f'{host}{port}/Data/Plan/Del{id}'
        response = py_requests.get(url)
        response.raise_for_status()
        plan = response.text
        return plan
    except py_requests.exceptions.HTTPError as http_err:
        return (f"HTTP error occurred: {http_err}")
    except Exception as err:
        return (f"An error occurred: {err}")

#update
@app.route('/Plan/Update/<id>', methods=['POST','PUT'])
def update_plan(id):
    try:
        url = f'{host}{port}/Data/Plan/Update/{id}'
        json = flask_request.get_json()
        if not json:
            return jsonify({"error": "Invalid JSON data"}), 400
        headers = {'Content-Type': 'application/json'}
        response = py_requests.put(url, json=json, headers = headers)
        plan = response.text
        return plan, 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500