from flask import jsonify, request as flask_request
import requests as py_requests
from config import db, app, host, port
import utils.utils as utils
from models.ability import Ability


#get all
@app.route('/Ability')
def get_all_abilities():
    """
    Gets all abilities
    ---
    tags:
      - "Ability Operations"
    responses:
      '200':
        description: A list of abilities
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
                properties:
                  id:
                    type: string
                  Name:
                    type: string
                  Mechanics:
                    type: string
                  Short Description:
                    type: string
      400:
        description: Bad request
      404:
        description: Not found
      500:
        description: Internal server error
    """
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
    """
    Gets an ability for the matching ID
    ---
    tags:
      - "Ability Operations"
    parameters:
      - in: "path"
        name: "id"
        type: "String"
        description: "the ID of the desired ability"
    responses:
      '200':
        description: An abilities
        content:
          application/json:
            schema:
              type: object
              properties:
                id:
                  type: string
                Name:
                  type: string
                Mechanics:
                  type: string
                Short Description:
                  type: string
      400:
        description: Bad request
      404:
        description: Not found
      500:
        description: Internal server error
    """
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
    """
    Posts an ability to be added to the persistence
    ---
    tags:
      - "Ability Operations"
    post:
      produces:
        - "application/json"
      consumes:
        - "application/json"
      parameters:
        - in: "body"
          name: "body"
          description: "Ability Data to be added"
          required: true
          schema:
            type: object
            properties:
              id:
                type: string
              Name:
                type: string
              Mechanics:
                type: string
              Short Description:
                type: string
      responses:
        '201':
          description: An abilities
          content:
            application/json:
              schema:
              type: object
              properties:
                id:
                  type: string
                Name:
                  type: string
                Mechanics:
                  type: string
                Short Description:
                  type: string
        400:
          description: Bad request
        404:
          description: Not found
        500:
          description: Internal server error
    """
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
    """
    Deletes an ability from the persistence
    ---
    tags:
      - "Ability Operations"
    delete:
      parameter:
        - in: "path"
          name: "id"
          type: "String"
          description: "The id of the ability to be removed"
      responses:
        '200':
          description: An abilities
          content:
            application/json:
              schema:
              type: object
              properties:
                id:
                  type: string
                Name:
                  type: string
                Mechanics:
                  type: string
                Short Description:
                  type: string
        400:
          description: Bad request
        404:
          description: Not found
        500:
          description: Internal server error
    """
    try:
        url = f'{host}{port}/Data/Ability/Del/{id}'
        response = py_requests.get(url)
        response.raise_for_status()
        ability = response.text
        return ability, 200
    except py_requests.exceptions.HTTPError as http_err:
        return (f"HTTP error occurred: {http_err}")
    except Exception as err:
        return (f"An error occurred: {err}")

#update
@app.route('/Ability/Update/<id>', methods=['PUT'])

def update_ability(id):
    """
    Puts an update on an existing ability.
    ---
    tags:
      - "Ability Operations"
    put:
      consumes:
        - "application/json"
      produces:
        - "application/json"
      parameters:
        - in: "body"
          name: "body"
          description: "Ability Data to be updated"
          required: true
          schema:
            type: "Object"
            properties:
              name:
                type: string
                exemple: "Power Attack"
              mechanics:
                type: string
                exemple: "-2 to hit, +4 to hit"
              short_description:
                exemple: "A powerful attack trading precision for lethality"
                type: string
        - in: "path"
          name: "id"
          type: "string"
          description: "the id of the ability to be updated"
          required: true
      responses:
        '200':
          description: An abilities
          content:
            application/json:
              schema:
              type: object
              properties:
                id:
                  type: string
                Name:
                  type: string
                Mechanics:
                  type: string
                Short Description:
                  type: string
        400:
          description: Bad request
        404:
          description: Not found
        500:
          description: Internal server error
    """
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