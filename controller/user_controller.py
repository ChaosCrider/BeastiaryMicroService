from flask import jsonify
from conn_config import db, app
import persistance.dao.user_dao as user_dao

import utils.utils as utils

dao = user_dao.UserDAO(db, app)

#get all
@app.route('/User')
def get_all_user():
    return jsonify(utils.convert_list_to_dict(dao.get_users()))

#get by  id
@app.route('/User/<id>')
def get_user_by_id(id):
    return jsonify(dao.get_user_by_id(id).to_dict())

#get by token
@app.route('/User/token/', method=['POST'])
def get_user_by_token(token):
    return jsonify(dao.get_user_by_token(token).to_dict())

#get by plan id
@app.route('/User/Plan/<id>')
def get_users_by_plan_id(id):
    return jsonify(utils.convert_list_to_dict(dao.get_user_by_plan_id(id)))

# consume 1
@app.route('/User/Consume/<id>')
def consumeb_one(id):
    user = dao.get_user_by_id(id)
    dao.consume_one(user)
    return dao.get_consumption(user)

# get consomption by user id
@app.route('/User/Consume/User/<id>')
def get_consomption_by_user_id(id):
    return dao.get_consumption(dao.get_user_by_id(id))

# reset consomption
@app.route('/User/Consume/Reset')
def reset_all_consomption():
    dao.reset_all_consumption()
    # have something returned, maybe int of reset users.

@app.route('/User/Add', method=['POST'])
def add_user(user):
    dao.add_user(user)
    return jsonify(user.to_dict())

# delete
@app.route('/User/Del', method=['DELETE'])
def delete_user(user):
    dao.remove_user(user)
    return jsonify(user.to_dict())

# update
@app.route('/User/Update', method=['PORT','PUT'])
def update_user(user):
    dao.update_user(user)
    return jsonify(dao.get_user_by_id(user.id).to_dict())

