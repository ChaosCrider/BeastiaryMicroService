from flask import jsonify
from conn_config import db, app
import persistance.dao.beast_dao as beast_dao
import utils.utils as utils

dao = beast_dao.BeastDAO(db, app)


@app.route('/Beast')
def index():
    beasts = dao.get_beasts()
    return jsonify(utils.convert_list_to_dict(beasts))


@app.route('/Beast/<id>')
def get_beast_by_id(beast_id):
    return jsonify(dao.get_beast_by_id(beast_id).to_dict())


@app.route('/Beast/Source/<source>')
def get_beast_by_source(source):
    beasts = dao.get_beast_by_source(source)
    return jsonify(utils.convert_list_to_dict(beasts))


@app.route('/Beast/Add', methods=['POST'])
def add_beast(beast):
    dao.add_beast(beast)


@app.route('/Beast/Del/', methods=['POST'])
def delete_beast(beast):
    dao.remove_beast(beast)
    return jsonify(beast)

@app.route('/Beast/Update/',methods=['POST'])
def update_beast(beast):
    dao.update_beast(beast)
    return jsonify(beast)