from flask import request as flask_request, jsonify, json
import requests as py_requests
from config import db, app, host, port
from models.user import User


@app.route('/Beast')
def index():
    """
    Gets all beasts
    ---
    tags:
      - "Beast Operations"
    responses:
      200:
        description: A list of beasts
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
                properties:
                  description:
                    type: string
                    example: "AAA"
                  id:
                    type: integer
                    example: 1
                  name:
                    type: string
                    example: "AAA"
                  source:
                    type: string
                    example: "A"
                  stat_block:
                    type: string
                    example: "AAA"
      400:
        description: Bad request
      404:
        description: Not found
      500:
        description: Internal server error
    """
    try:
        url = f'{host}{port}/Data/Beast'
        beasts = url_call(url)
        return beasts
    except py_requests.exceptions.HTTPError as http_err:
        return (f"HTTP error occurred: {http_err}")
    except Exception as err:
        return (f"An error occurred: {err}")


@app.route('/Beast/<id>')
def get_beast_by_id(id):
    """
    Gets a beast by providing the ID
    ---
    tags:
      - "Beast Operations"
    parameters:
      - in: "path"
        name: "ID"
        type: "String"
        description: "the ID of the desired ability"
    responses:
      200:
        description: A list of beasts
        content:
          application/json:
            schema:
            type: object
            properties:
              description:
                type: string
                example: "AAA"
              id:
                type: integer
                example: 1
              name:
                type: string
                example: "AAA"
              source:
                type: string
                example: "A"
              stat_block:
                type: string
                example: "AAA"
      400:
        description: Bad request
      404:
        description: Not found
      500:
        description: Internal server error
    """
    try:
        url = f'{host}{port}/Data/Beast/{id}'
        beast = url_call(url)
        return beast, 200
    except py_requests.exceptions.HTTPError as http_err:
        return (f"HTTP error occurred: {http_err}"), http_err.response.status_code
    except Exception as err:
        return (f"An error occurred: {err}"), 500





@app.route('/Beast/Source/<source>')
def get_beast_by_source(source):
    """
    Gets a list beasts of beast that are included in a specific source.
    ---
    tags:
      - "Beast Operations"
    parameters:
      - name: source
        in: path
        type: string
        required: true
        description: the source material for which all beast must be returned
    responses:
      200:
        description: A list of beasts
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
                properties:
                  description:
                    type: string
                    example: "AAA"
                  id:
                    type: integer
                    example: 1
                  name:
                    type: string
                    example: "AAA"
                  source:
                    type: string
                    example: "A"
                  stat_block:
                    type: string
                    example: "AAA"
      400:
        description: Bad request
      404:
        description: Not found
      500:
        description: Internal server error
    """
    try:
        url = f'{host}{port}/Data/Beast/Source/{source}'
        beasts = url_call(url)
        return beasts
    except py_requests.exceptions.HTTPError as http_err:
        return (f"HTTP error occurred: {http_err}")
    except Exception as err:
        return (f"An error occurred: {err}")

    # beasts = dao.get_beast_by_source(source)
    # return jsonify(utils.convert_list_to_dict(beasts))



@app.route('/Beast/Add', methods=['POST'])
def add_beast():
    """
    Posts a beast to the database
    ---
    tags:
      - "Beast Operations"
    post:
      summary: "Add a new beast data"
      consumes:
        - "application/json"
      produces:
        - "application/json"
      parameters:
        - in: "body"
          name: "body"
          description: "Beast data to be added"
          required: true
          schema:
            type: "object"
            properties:
              name:
                type: "string"
                example: "Wolf"
              source:
                type: "string"
                example: "D&D"
              description:
                type: "string"
                example: "A wild canidae of medium size"
              stat_block:
                type: "string"
                example: "hp: 22, AC:15, ini: +2 ..."
              token:
                type: "string"
                example: "1256"
      responses:
        '201':
          description: "Beast data added successfully"
          schema:
            type: "object"
            properties:
              id:
                type: "integer"
                example: 1
              name:
                type: "string"
                example: "Wolf"
              source:
                type: "string"
                example: "D&D"
              description:
                type: "string"
                example: "A wild canidae of medium size"
              stat_block:
                type: "string"
                example: "hp: 22, AC:15, ini: +2 ..."
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
    json_data = flask_request.get_json()
    token = json_data.get("token", None)
    if token:
        #get user by token
        url = f'{host}{port}/Data/User/Token'
        user_data = url_call_json(url, token)
        if not isinstance(user_data, dict):
            user_data = json.loads(user_data)

        #get user details
        user_id = user_data.get('id', 1)
        consumption = user_data.get('consumption', 65535)
        plan_id = user_data.get('plan_id', 1)

        #get plan's allowance
        url = f'{host}{port}/Data/Plan/{plan_id}'
        plan_data = url_call(url)
        if not isinstance(plan_data, dict):
            plan_data = json.loads(plan_data)
        allowance = plan_data.get('monthly_allowance', 0)

        if allowance > consumption:
            try: # consumes 1 for the user
                url = f'{host}{port}/Data/User/Consume/{user_id}'  # consume by id url
                url_call(url)
            except py_requests.exceptions.HTTPError as http_err:
                return (f"HTTP error occurred: {http_err}")
            except Exception as err:
                return (f"An error occurred: {err}")

            try: # adds the beasts and returns it
                url = f'{host}{port}/Data/Beast/Add'
                json_data = flask_request.get_json()
                beast = url_call_json(url, json_data)
                return beast, 201
            except Exception as e:
                return jsonify({"error": str(e)}), 500


@app.route('/Beast/Del/<id>', methods=['DElETE'])
def delete_beast(id):
    """
    Deletes a beast from the persistence based on a provided ID
    ---
    tags:
      - "Beast Operations"
    delete:
      summary: "Deletes a beast by ID"
      parameters:
        - in: "path"  # Removed extra space before the colon
          name: "id"
          description: "ID of the best to be removed"
          required: true  # Changed "true" to true
          type: "string"
      responses:
        '200':
          description: "Beast deleted successfully"  # Corrected typo in "successfully"
          schema:
            type: "string"  # Changed "String" to "string"
        '404':
          description: "Not found"
          schema:
            type: object
            properties:
              message:
                type: "string"
        '500':
          description: "Internal Server Error"
          schema:
            type: object
            properties:
              message:
                type: "string"
    """
    try:
        url = f'{host}{port}/Data/Beast/Del/{id}'
        beast = url_call(url, "delete")
        print(beast)
        return beast
    except py_requests.exceptions.HTTPError as http_err:
        return (f"HTTP error occurred: {http_err}")
    except Exception as err:
        return (f"An error occurred: {err}")

@app.route('/Beast/Update/<beast_id>',methods=['PUT'])
def update_beast(beast_id):
    """
    Puts an update to a beast in the database
    ---
    tags:
      - "Beast Operations"
    put:
      summary: "Update existing beast data"
      consumes:
        - "application/json"
      produces:
        - "application/json"
      parameters:
        - in: "path"
          name: "beast_id"
          type: "string"
          required: true
          description: "The ID of the beast to update"
          example: "5"
        - in: "body"
          name: "body"
          description: "Beast data to be updated"
          required: true
          schema:
            type: "object"
            properties:
              name:
                type: "string"
                example: "Wolf"
              source:
                type: "string"
                example: "D&D"
              description:
                type: "string"
                example: "A wild canidae of medium size"
              stat_block:
                type: "string"
                example: "hp: 22, AC:15, ini: +2 ..."
              token:
                type: "string"
                example: "1256"
      responses:
        '201':
          description: "Beast data updated successfully"
          schema:
            type: "object"
            properties:
              id:
                type: "integer"
                example: 1
              name:
                type: "string"
                example: "Wolf"
              source:
                type: "string"
                example: "D&D"
              description:
                type: "string"
                example: "A wild canidae of medium size"
              stat_block:
                type: "string"
                example: "hp: 22, AC:15, ini: +2 ..."
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
    print('update endpoint reached')
    json_data = flask_request.get_json()
    token = json_data.get("token", None)
    print(token)
    if token:

        #get user by token
        url = f'{host}{port}/Data/User/Token'
        user_data = url_call_json(url, token)
        if not isinstance(user_data, dict):
            user_data = json.loads(user_data)

        #get user details
        user_id = user_data.get('id', 1)
        consumption = user_data.get('consumption', 65535)
        plan_id = user_data.get('plan_id', 1)

        print(f'user {user_id}, cons{consumption}, plan {plan_id}')
        #get plan's allowance
        url = f'{host}{port}/Data/Plan/{plan_id}'
        plan_data = url_call(url)
        if not isinstance(plan_data, dict):
            plan_data = json.loads(plan_data)
        allowance = plan_data.get('monthly_allowance', 0)

        if allowance > consumption:
            try: # consumes 1 for the user
                url = f'{host}{port}/Data/User/Consume/{user_id}'  # consume by id url
                url_call(url)
            except py_requests.exceptions.HTTPError as http_err:
                return (f"HTTP error occurred: {http_err}")
            except Exception as err:
                return (f"An error occurred: {err}")

            try:
                print(1)
                url = f'{host}{port}/Data/Beast/Update/{beast_id}'
                print('2, ', url)
                json_data = flask_request.get_json()
                print('3 ,', json_data)
                beast = url_call_json(url, json_data, "put")
                print(beast)
                return beast, 201
            except Exception as e:
                return jsonify({"error": str(e)}), 500




def url_call_json(url, json, method=None):
    if not json:
        return jsonify({"error": "Invalid JSON data"}), 400
    headers = {'Content-Type': 'application/json'}
    if method == "put":
        response = py_requests.put(url, json=json, headers = headers)
    else:
        response = py_requests.post(url, json=json, headers = headers)
    response.raise_for_status()
    return response.text


def url_call(url, method=None):
    if method == "delete":
        response = py_requests.delete(url)
    else:
        response = py_requests.get(url)
    response.raise_for_status()
    return response.text
