from flask import jsonify, request
from config import db, app
import utils.utils as utils
import persistance.dao.ability_dao as ability_dao
from models.ability import Ability

dao = ability_dao.AbilityDAO(db, app)

#get all
@app.route('/Ability')
def get_all_abilities():
    print('Get Avility triggered')
    abilities = dao.get_abilities()
    return jsonify(utils.convert_list_to_dict(abilities))

# get by id
@app.route('/Ability/<id>')
def get_ability_by_id(id):
    ability = dao.get_ability_by_id(id)
    return jsonify(ability.to_dict())

#add
@app.route('/Ability/Add', methods=['POST'])
def add_ability():
    ability_data= request.get_json()
    if not ability_data:
        return jsonify({"error": "Invalid JSON data"}), 400

    try:
        ability = Ability(**ability_data)
        dao.add_ability(ability)
        return jsonify(ability_data), 201
    except Exception as e:
        return  jsonify({"error":str(e)}), 500

#delete
@app.route('/Ability/Del/<id>', methods=['DELETE'])
def delete_ability(id):
    ability = dao.get_ability_by_id(id)
    dao.remove_ability(ability)
    return jsonify(ability), 201

#update
@app.route('/Ability/Update/<id>', methods=['POST','PUT'])
def update_ability(id):
    ability_json = request.get_json()
    if not ability_json:
        return jsonify({"error":"Invalid Json data"}), 400

    try:
        ability = Ability(**ability_json)
        dao.update_ability(ability)
        return jsonify(ability_json)
    except Exception as e:
        return jsonify({"error": str(e)}), 500