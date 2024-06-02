from flask import request, jsonify
from config import db, app
import persistance.dao.beast_dao as beast_dao
import utils.utils as utils
from models.beast import Beast

dao = beast_dao.BeastDAO(db, app)


@app.route('/Beast')
def index():
    beasts = dao.get_beasts()
    return jsonify(utils.convert_list_to_dict(beasts))


@app.route('/Beast/<id>')
def get_beast_by_id(id):
    return jsonify(dao.get_beast_by_id(id).to_dict())


@app.route('/Beast/Source/<source>')
def get_beast_by_source(source):
    beasts = dao.get_beast_by_source(source)
    return jsonify(utils.convert_list_to_dict(beasts))


@app.route('/Beast/Add', methods=['POST'])
def add_beast():
    # Extract JSON data from the request
    beast_data = request.get_json()
    if not beast_data:
        return jsonify({"error": "Invalid JSON data"}), 400

    try:
        beast = Beast(**beast_data)
        dao.add_beast(beast)
        return jsonify(beast_data), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/Beast/Del/<id>', methods=['DElETE'])
def delete_beast(id):
    beast = dao.get_beast_by_id(id)
    dao.remove_beast(beast)
    return jsonify(beast)



@app.route('/Beast/Update/<id>',methods=['POST','PUT'])
#modify to match teh post approach
def update_beast(id):
    beast_data = request.get_json()
    if not beast_data:
        return jsonify({"error": "Invalid JSON data"}), 400
    try:
        beast = Beast(**beast_data)
        dao.update_beast(id, beast)
        target_beast = dao.get_beast_by_id(id)
        return target_beast.to_dict(), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

