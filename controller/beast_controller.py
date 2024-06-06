from flask import request as flask_request, jsonify
import requests as py_requests
from config import db, app, host, port


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
        response = py_requests.get(url)
        response.raise_for_status()
        beast = response.text
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
                type: string
                example: "Wolf"
              source:
                type: string
                example: "D&D"
              description:
                type: string
                example: "A wild canidae of medium size"
              stat_block:
                type: string
                example: "hp: 22, AC:15, ini: +2 ..."
      responses:
        '201':
          description: "Beast data added successfully"
          schema:
            type: "object"
            properties:
              message:
                type: "string"
              data:
                type: "object"
                properties:
                  id:
                    type: integer
                    example: 1
                  name:
                    type: string
                    example: "AAA"
                  source:
                    type: string
                    example: "A"
                  description:
                    type: string
                    example: "AAA"
                  stat_block:
                    type: string
                    example: "AAA"
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
        url = f'{host}{port}/Data/Beast/Del{id}'
        response = py_requests.get(url)
        response.raise_for_status()
        beast = response.text
        return beast
    except py_requests.exceptions.HTTPError as http_err:
        return (f"HTTP error occurred: {http_err}")
    except Exception as err:
        return (f"An error occurred: {err}")

@app.route('/Beast/Update/<id>',methods=['PUT'])
def update_beast(id):
    """
    Puts an update to a beast from the database
    ---
    tags:
      - "Beast Operations"
    put:
      summary: "Add a new beast data"
      consumes:
        - "application/json"
      produces:
        - "application/json"
      parameters:
        - in: "path"
          name: "ID"
          type: "string"
          require: true
          description: "the id of the beast to update"
        - in: "body"
          name: "body"
          description: "Beast data to be added"
          required: true
          schema:
            type: "object"
            properties:
              name:
                type: string
                example: "Wolf"
              source:
                type: string
                example: "D&D"
              description:
                type: string
                example: "A wild canidae of medium size"
              stat_block:
                type: string
                example: "hp: 22, AC:15, ini: +2 ..."
      responses:
        '201':
          description: "Beast data added successfully"
          schema:
            type: "object"
            properties:
              message:
                type: "string"
              data:
                type: "object"
                properties:
                  id:
                    type: integer
                    example: 1
                  name:
                    type: string
                    example: "AAA"
                  source:
                    type: string
                    example: "A"
                  description:
                    type: string
                    example: "AAA"
                  stat_block:
                    type: string
                    example: "AAA"
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