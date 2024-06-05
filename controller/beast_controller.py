from flask import request as flask_request, jsonify
import requests as py_requests
from config import db, app, host, port
import controller.dao as beast_dao
import utils.utils as utils
from models.beast import Beast

# dao = beast_dao

@app.route('/Beast')
def index():
    try: #next convert dao into controller
        url = f'{host}{port}/Data/Beast'
        headers = {'Content-Type': 'application/json'}
        response = py_requests.get(url) #, json=json_data, headers=headers
        response.raise_for_status()  # Raise an exception for HTTP errors
        beasts = response.text
        return beasts
    except py_requests.exceptions.HTTPError as http_err:
        return (f"HTTP error occurred: {http_err}")
    except Exception as err:
        return (f"An error occurred: {err}")


@app.route('/Beast/<id>')
def get_beast_by_id(id):
    try:
        url = f'{host}{port}/Data/Beast/{id}'
        response = py_requests.get(url)
        response.raise_for_status()
        beast = response.text
        return beast
    except py_requests.exceptions.HTTPError as http_err:
        return (f"HTTP error occurred: {http_err}")
    except Exception as err:
        return (f"An error occurred: {err}")





@app.route('/Beast/Source/<source>')
def get_beast_by_source(source):
    try:
        url = f'{host}{port}/Data/Beast/Source/{source}'
        response = py_requests.get(url) #, json=json_data, headers=headers
        response.raise_for_status()  # Raise an exception for HTTP errors
        beasts = response.text
        return beasts
    except py_requests.exceptions.HTTPError as http_err:
        return (f"HTTP error occurred: {http_err}")
    except Exception as err:
        return (f"An error occurred: {err}")

    # beasts = dao.get_beast_by_source(source)
    # return jsonify(utils.convert_list_to_dict(beasts))



@app.route('/Beast/Add', methods=['POST'])
def add_beast():
    # Extract JSON data from the request

    try:
        url = f'{host}{port}/Data/Beast/Add'
        json = flask_request.get_json()
        if not json:
            return jsonify({"error": "Invalid JSON data"}), 400
        headers = {'Content-Type': 'application/json'}
        response = py_requests.post(url, json=json, headers = headers)
        beast = response.text
        return beast, 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500



@app.route('/Beast/Del/<id>', methods=['DElETE'])
def delete_beast(id):
    try:
        url = f'{host}{port}/Data/Beast/Del{id}'
        response = py_requests.get(url)
        response.raise_for_status()
        beast = response.text
        return beast
    except py_requests.exceptions.HTTPError as http_err:
        return (f"HTTP error occurred: {http_err}")
    except Exception as err:
        return (f"An error occurred: {err}")

@app.route('/Beast/Update/<id>',methods=['POST','PUT'])
#modify to match teh post approach
def update_beast(id):
    try:
        url = f'{host}{port}/Data/Beast/Update/{id}'
        json = flask_request.get_json()
        if not json:
            return jsonify({"error": "Invalid JSON data"}), 400
        headers = {'Content-Type': 'application/json'}
        response = py_requests.put(url, json=json, headers = headers)
        beast = response.text
        return beast, 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500