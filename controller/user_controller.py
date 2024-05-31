from flask import jsonify
from conn_config import db, app
import persistance.dao.user_dao as dao
import utils.utils as utils

dao = dao.UserDAO(db, app)

@app.route('/User')
def get_all_user():
    return jsonify(utils.convert_list_to_dict(dao.get_users()))

@app.route('/User/<id>')
def get_user_by_id(id):
    return jsonify(dao.get_user_by_id(id).to_dict())

@app.route('/User/token/', method=['POST'])
def get_user_by_token(token):
    return jsonify(dao.get_user_by_token(token).to_dict())

@app.route('/User/Plan/<id>')
def get_users_by_plan_id(id):
    return jsonify(utils.convert_list_to_dict(dao.get_user_by_plan_id(id)))

@app.route('/User/Consume/<id>')
def consumeb_one(id):
    user = dao.get_user_by_id(id)
    dao.consume_one(user)
    return dao.get_consomption(user)

@app.route('/User/Consume/User/<id>')
def get_consomption_by_user_id(id):
    return dao.get_consomption(dao.get_user_by_id(id))

@app.route('/User/Consume/Reset')
def reset_all_consomption():
    dao.reset_all_consomption()
    # have something returned, maybe int of reset users.

@app.route('/User/Add', method=['POST'])
def add_user(user):
    dao.add_user(user)
    return jsonify(user.to_dict())

@app.route('/User/Del', method=['DELETE'])
def delete_user(user):
    dao.remove_user(user)
    return jsonify(user.to_dict())

@app.route('/User/Update', method=['PORT','PUT'])
def update_user(user):
    dao.update_user(user)
    return jsonify(dao.get_user_by_id(user.id).to_dict())

