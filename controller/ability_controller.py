from flask import jsonify
from conn_config import db, app
import utils.utils as utils

import persistance.dao.ability_dao as ability_dao

dao = ability_dao.AbilityDAO(db, app)

#get all
@app.route('/Ability')
def get_all_abilities():
    abilities = dao.get_abilities()
    return jsonify(utils.convert_list_to_dict(abilities))

# get by id
@app.route('/Ability/<id>')
def get_ability_by_id(id):
    return jsonify(dao.get_ability_by_id(id).to_dict())

#add
@app.route('/Ability/Add', method=['POST'])
def add_ability(ability):
    dao.add_ability(ability)

#delete
@app.route('/Ability/Del', method=['DELETE'])
def delete_ability(ability):
    dao.remove_ability(ability)

#update
@app.route('/Ability/Update', method=['POST','PUT'])
def update_ability(ability):
    dao.update_ability(ability)