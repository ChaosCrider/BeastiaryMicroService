from flask import jsonify, request as flask_request
import requests as py_requests
from config import db, app, host, port
import utils.utils as utils
from models.user import User

#get all
@app.route('/User')
def get_all_user():
    try: #next convert dao into controller
        url = f'{host}{port}/Data/User'
        headers = {'Content-Type': 'application/json'}
        response = py_requests.get(url) #, json=json_data, headers=headers
        response.raise_for_status()  # Raise an exception for HTTP errors
        users = response.text
        return users
    except py_requests.exceptions.HTTPError as http_err:
        return (f"HTTP error occurred: {http_err}")
    except Exception as err:
        return (f"An error occurred: {err}")
    

#get by  id
@app.route('/User/<id>')
def get_user_by_id(id):
    try:
        url = f'{host}{port}/Data/User/{id}'
        response = py_requests.get(url)
        response.raise_for_status()
        user = response.text
        return user
    except py_requests.exceptions.HTTPError as http_err:
        return (f"HTTP error occurred: {http_err}")
    except Exception as err:
        return (f"An error occurred: {err}")

#get by token
@app.route('/User/Token/', methods=['POST'])
def get_user_by_token():
    try:
        json = flask_request.get_json()
        url = f'{host}{port}/Data/User/Token'
        headers = {'Content-Type': 'application/json'}
        response = py_requests.post(url, json=json, headers = headers)
        response.raise_for_status()
        consume = response.text
        return consume
    except py_requests.exceptions.HTTPError as http_err:
        return (f"HTTP error occurred: {http_err}")
    except Exception as err:
        return (f"An error occurred: {err}")

#get by plan id
@app.route('/User/Plan/<id>')
def get_users_by_plan_id(id):
    try:
        url = f'{host}{port}/Data/User/Plan/{id}'
        response = py_requests.get(url)
        response.raise_for_status()
        users = response.text
        return users
    except py_requests.exceptions.HTTPError as http_err:
        return (f"HTTP error occurred: {http_err}")
    except Exception as err:
        return (f"An error occurred: {err}")

# consume 1
@app.route('/User/Consume/<id>')
def consumeb_one(id):
    try:
        url = f'{host}{port}/Data/User/Consume/{id}'
        response = py_requests.get(url)
        response.raise_for_status()
        consume = response.text
        return consume
    except py_requests.exceptions.HTTPError as http_err:
        return (f"HTTP error occurred: {http_err}")
    except Exception as err:
        return (f"An error occurred: {err}")

# get consomption by user id
@app.route('/User/Consume/User/<id>')
def get_consomption_by_user_id(id):
    try:
        url = f'{host}{port}/Data/User/Consume/User/{id}'
        response = py_requests.get(url)
        response.raise_for_status()
        consume = response.text
        return consume
    except py_requests.exceptions.HTTPError as http_err:
        return (f"HTTP error occurred: {http_err}")
    except Exception as err:
        return (f"An error occurred: {err}")

# reset consomption
@app.route('/User/Consume/Reset')
def reset_all_consomption():
    try:
        url = f'{host}{port}/Data/User/Consume/Reset'
        response = py_requests.get(url)
        response.raise_for_status()
        consume = response.text
        return consume
    except py_requests.exceptions.HTTPError as http_err:
        return (f"HTTP error occurred: {http_err}")
    except Exception as err:
        return (f"An error occurred: {err}")

@app.route('/User/Add', methods=['POST'])
def add_user():
    try:
        url = f'{host}{port}/Data/User/Add'
        json = flask_request.get_json()
        if not json:
            return jsonify({"error": "Invalid JSON data"}), 400
        headers = {'Content-Type': 'application/json'}
        response = py_requests.post(url, json=json, headers = headers)
        user = response.text
        return user, 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# delete
@app.route('/User/Del/<id>', methods=['DELETE'])
def delete_user(id):
    try:
        url = f'{host}{port}/Data/User/Del{id}'
        response = py_requests.get(url)
        response.raise_for_status()
        user = response.text
        return user
    except py_requests.exceptions.HTTPError as http_err:
        return (f"HTTP error occurred: {http_err}")
    except Exception as err:
        return (f"An error occurred: {err}")

# update
@app.route('/User/Update/<id>', methods=['POST','PUT'])
def update_user(id):
    try:
        url = f'{host}{port}/Data/User/Update/{id}'
        json = flask_request.get_json()
        if not json:
            return jsonify({"error": "Invalid JSON data"}), 400
        headers = {'Content-Type': 'application/json'}
        response = py_requests.put(url, json=json, headers = headers)
        user = response.text
        return user, 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
