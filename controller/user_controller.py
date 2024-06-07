from flask import jsonify, request as flask_request
import requests as py_requests
from config import db, app, host, port
import utils.utils as utils
from models.user import User



#get all
@app.route('/User')
def get_all_user():
    """
    Gets all Users
    ---
    tags:
      - "User Operations"
    responses:
      '200':
        description: "A list of users"
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
                  password:
                    type: string
                  consumption:
                    type: string
                  plan_id:
                    type: string
      '400':
        description: "Bad Request"
      '404':
        description: "Not Found"
      '500':
        description: "Internal Server Error"
    """
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
    """
    Gets a user by matching id
    ---
    tags:
      - "User Operations"
    parameters:
      - in: "path"
        name: "id"
        description: "the id of the user to be returned"
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
                    type:string
                  name:
                    type:string
                  password:
                    type: string
                  consumption:
                    type: string
                  plan_id:
                    type: string
      '400':
        description: "Bad Request"
      '404':
        description: "Not Found"
      '500':
        description: "Internal Server Error"
    """
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
    """
    Posts a user to be added to the persistence
    ---
    tags:
      - "User Operations"
    post:
      produces:
        - "application/json"
      consumes:
        - "application/json"
      parameters:
        - in: "body"
          name: "body"
          description: "the identification token"
          required: true
          schema:
            type: object
            properties:
              token:
                type: string
                example: "bdeb"
      responses:
        '200':
          description: a user
          content:
            application/json:
              schema:
              type: object
              properties:
                  id:
                    type:string
                  name:
                    type:string
                  password:
                    type: string
                  consumption:
                    type: string
                  plan_id:
                    type: string
        400:
          description: Bad request
        404:
          description: Not found
        500:
          description: Internal server error
    """
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


# consume 1
@app.route('/User/Consume/<id>')
def consumeb_one(id):
    """
    Gets a user's consumption up by one
    ---
    tags:
      - "User Operations"
    parameters:
      - in: "path"
        name: "id"
        description: "the id of the user to be returned"
        type: "string"
    responses:
      '200':
        description:
        content:
          "application/json":
            schema:
              type: int
      '400':
        description: "Bad Request"
      '404':
        description: "Not Found"
      '500':
        description: "Internal Server Error"
    """
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
    """
    Consumes data for a user by user ID
    ---
    tags:
      - "User Operations"
    get:
      summary: "Consume data for a user by ID"
      consumes:
        - "application/json"
      produces:
        - "application/json"
      parameters:
        - in: "path"
          name: "id"
          type: "string"
          required: true
          description: "The ID of the user to consume data for"
      responses:
        '200':
          description: "Data consumed successfully"
          schema:
            type: "string"
            example: "Data consumption successful"
        '400':
          description: "Bad request"
          schema:
            type: "object"
            properties:
              message:
                type: "string"
        '500':
          description: "Internal Server Error"
          schema:
            type: "object"
            properties:
              message:
                type: "string"
    """
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
    """
    Gets a reset of all consumption going.
    ---
    tags:
      - "User Operations"
    responses:
      '200':
        description: "an amount of updated accounts."
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
    try:
        url = f'{host}{port}/Data/User/Consume/Reset'
        print(url)
        response = py_requests.get(url)
        response.raise_for_status()
        print(response)
        rows = response.text
        print(rows)
        return rows
    except py_requests.exceptions.HTTPError as http_err:
        return (f"HTTP error occurred: {http_err}")
    except Exception as err:
        return (f"An error occurred: {err}")

@app.route('/User/Add', methods=['POST'])
def add_user():
    """
    Posts a user to be added to the persistence
    ---
    tags:
      - "User Operations"
    post:
      produces:
        - "application/json"
      consumes:
        - "application/json"
      parameters:
        - in: "body"
          name: "body"
          description: "User Data to be added"
          required: true
          schema:
            type: object
            properties:
              name:
                type: string
                example: "Conrad"
              password:
                type: "250"
                example: "not1234"
              plan_id:
                type: string
                example: "1"
      responses:
        '201':
          description: An abilities
          content:
            application/json:
              schema:
              type: object
              properties:
                  id:
                    type:string
                  name:
                    type:string
                  password:
                    type: string
                  consumption:
                    type: string
                  plan_id:
                    type: string
        400:
          description: Bad request
        404:
          description: Not found
        500:
          description: Internal server error
    """
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
    """
    Deletes a user from the persistence
    ---
    tags:
      - "User Operations"
    delete:
      parameter:
        - in: "path"
          name: "id"
          type: "String"
          description: "The id of the user to be removed"
      responses:
        '200':
          description: An abilities
          content:
            application/json:
              schema:
              type: object
              properties:
                  id:
                    type:string
                  name:
                    type:string
                  password:
                    type: string
                  consumption:
                    type: string
                  plan_id:
                    type: string
        400:
          description: Bad request
        404:
          description: Not found
        500:
          description: Internal server error
    """
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
@app.route('/User/Update/<id>', methods=['PUT'])
def update_user(id):
    """
    Puts an update on an existing ability.
    ---
    tags:
      - "User Operations"
    put:
      consumes:
        - "application/json"
      produces:
        - "application/json"
      parameters:
        - in: "body"
          name: "body"
          description: "User Data to be updated"
          required: true
          schema:
            type: "Object"
            properties:
              name:
                type: string
                example: "premium user"
              monthly_allowance:
                type: string
                example: "20000"
              price:
                type: string
                example: "1.00"
        - in: "path"
          name: "id"
          type: "string"
          description: "the id of the user to be updated"
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
                    type:string
                  name:
                    type:string
                  password:
                    type: string
                  consumption:
                    type: string
                  plan_id:
                    type: string
        400:
          description: Bad request
        404:
          description: Not found
        500:
          description: Internal server error
    """
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

@app.route('/User/login', methods=['POST'])
def login():
    """
    Posts a request for a user's token
    ---
    tags:
      - "User Operations"
    post:
      summary: "Returns the user's token"
      consumes:
        - "application/json"
      produces:
        - "application/json"
      parameters:
        - in: "body"
          name: "body"
          description: "User login data"
          required: true
          schema:
            type: "object"
            properties:
              username:
                type: "string"
                example: "admin"
              password:
                type: "string"
                example: "coffeecrisp1"
      responses:
        '200':
          description: "Successfully returned the token"
          schema:
            type: "object"
            properties:
              token:
                type: "string"
                example: "some-jwt-token"
        '400':
          description: "Invalid JSON data"
          schema:
            type: "object"
            properties:
              error:
                type: "string"
                example: "Invalid JSON data"
        '500':
          description: "Internal Server Error"
          schema:
            type: "object"
            properties:
              error:
                type: "string"
                example: "Internal Server Error"
    """
    try:
        url = f'{host}{port}/Data/User/login'
        json = flask_request.get_json()
        if not json:
            return jsonify({"error": "Invalid JSON data"}), 400
        headers = {'Content-Type': 'application/json'}
        response = py_requests.post(url, json=json, headers = headers)
        token = response.text
        return token, 200
    except py_requests.exceptions.HTTPError as http_err:
        return jsonify({"error": f"HTTP error occurred: {http_err}"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500
