from flask import request as flask_request, jsonify
import requests as py_requests
from config import db, app, host, port
from models.plan import Plan
import utils.utils as utils



#get all
@app.route('/Plan')
def get_plans():
    """
    Gets all Plans
    ---
    tags:
      - "Plan Operations"
    responses:
      '200':
        description: "A list of plans"
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
                properties:
                  id:
                    type:string
                  name:
                    type:string
                  monthly_allowance:
                    type: string
                  price:
                    type: string
      '400':
        description: "Bad Request"
      '404':
        description: "Not Found"
      '500':
        description: "Internal Server Error"
    """
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
    """
    Gets a plan by matching id
    ---
    tags:
      - "Plan Operations"
    parameters:
      - in: "path"
        name: "id"
        description: "the id of the plan to be returned"
        type: "string"
    responses:
      '200':
        description:
        content:
          "application/json":
            schema:
              type: object
              properties:
                id:
                  type: string
                name:
                  type: string
                monthly_allowance:
                  type: string
                price:
                  type: string
      '400':
        description: "Bad Request"
      '404':
        description: "Not Found"
      '500':
        description: "Internal Server Error"
    """
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
    """
    Gets all plan under a certain price
    ---
    tags:
      - "Plan Operations"
    parameters:
      - in: "path"
        name: "price"
        description: "the maximum price to look for"
        type: "string"
    responses:
      '200':
        description:
        content:
          "application/json":
            schema:
              type: object
              properties:
                id:
                  type: string
                name:
                  type: string
                monthly_allowance:
                  type: string
                price:
                  type: string
      '400':
        description: "Bad Request"
      '404':
        description: "Not Found"
      '500':
        description: "Internal Server Error"
    """
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
    """
    Posts a plan to be added to the persistence
    ---
    tags:
      - "Plan Operations"
    post:
      produces:
        - "application/json"
      consumes:
        - "application/json"
      parameters:
        - in: "body"
          name: "body"
          description: "Plan Data to be added"
          required: true
          schema:
            type: object
            properties:
              id:
                type: string
              Name:
                type: string
              monthly_allowance:
                type: string
              price:
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
                monthly_allowance:
                  type: string
                price:
                  type: string
        400:
          description: Bad request
        404:
          description: Not found
        500:
          description: Internal server error
    """
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
    """
    Deletes a plan from the persistence
    ---
    tags:
      - "Plan Operations"
    delete:
      parameter:
        - in: "path"
          name: "id"
          type: "String"
          description: "The id of the plan to be removed"
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
                monthly_allowance:
                  type: string
                price:
                  type: string
        400:
          description: Bad request
        404:
          description: Not found
        500:
          description: Internal server error
    """
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
@app.route('/Plan/Update/<id>', methods=['PUT'])
def update_plan(id):
    """
    Puts an update on an existing ability.
    ---
    tags:
      - "Plan Operations"
    put:
      consumes:
        - "application/json"
      produces:
        - "application/json"
      parameters:
        - in: "body"
          name: "body"
          description: "Plan Data to be updated"
          required: true
          schema:
            type: "Object"
            properties:
              name:
                type: string
                exemple: "premium plan"
              monthly_allowance:
                type: string
                exemple: "20000"
              price:
                exemple: "1.00"
                type: string
        - in: "path"
          name: "id"
          type: "string"
          description: "the id of the plan to be updated"
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
                monthly_allowance:
                  type: string
                price:
                  type: string
        400:
          description: Bad request
        404:
          description: Not found
        500:
          description: Internal server error
    """
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