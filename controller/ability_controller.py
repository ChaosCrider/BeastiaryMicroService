from flask import jsonify, request as flask_request
import requests as py_requests
from config import db, app, host, port
import utils.utils as utils
from models.ability import Ability


#get all
@app.route('/Ability')
def get_all_abilities():
    try: #next convert dao into controller
        url = f'{host}{port}/Data/Ability'
        headers = {'Content-Type': 'application/json'}
        response = py_requests.get(url) #, json=json_data, headers=headers
        response.raise_for_status()  # Raise an exception for HTTP errors
        ability = response.text
        return ability
    except py_requests.exceptions.HTTPError as http_err:
        return (f"HTTP error occurred: {http_err}")
    except Exception as err:
        return (f"An error occurred: {err}")


# get by id
@app.route('/Ability/<id>')
def get_ability_by_id(id):
    try:
        url = f'{host}{port}/Data/Ability/{id}'
        response = py_requests.get(url)
        response.raise_for_status()
        ability = response.text
        return ability
    except py_requests.exceptions.HTTPError as http_err:
        return (f"HTTP error occurred: {http_err}")
    except Exception as err:
        return (f"An error occurred: {err}")


#add
@app.route('/Ability/Add', methods=['POST'])
def add_ability():
    try:
        url = f'{host}{port}/Data/Ability/Add'
        json = flask_request.get_json()
        if not json:
            return jsonify({"error": "Invalid JSON data"}), 400
        headers = {'Content-Type': 'application/json'}
        response = py_requests.post(url, json=json, headers = headers)
        ability = response.text
        return ability, 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

#delete
@app.route('/Ability/Del/<id>', methods=['DELETE'])
def delete_ability(id):
    try:
        url = f'{host}{port}/Data/Ability/Del/{id}'
        response = py_requests.get(url)
        response.raise_for_status()
        ability = response.text
        return ability
    except py_requests.exceptions.HTTPError as http_err:
        return (f"HTTP error occurred: {http_err}")
    except Exception as err:
        return (f"An error occurred: {err}")

#update
@app.route('/Ability/Update/<id>', methods=['POST','PUT'])
def update_ability(id):
    try:
        url = f'{host}{port}/Data/Ability/Update/{id}'
        json = flask_request.get_json()
        if not json:
            return jsonify({"error": "Invalid JSON data"}), 400
        headers = {'Content-Type': 'application/json'}
        response = py_requests.put(url, json=json, headers = headers)
        ability = response.text
        return ability, 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500