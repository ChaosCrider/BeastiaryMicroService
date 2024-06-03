from flask import jsonify, request
from config import db, app
import persistance.dao.user_dao as user_dao
import utils.utils as utils
from models.user import User

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
@app.route('/User/token/', methods=['POST'])
def get_user_by_token():
    token_data = request.get_json()
    token = None
    if not token_data:
        return jsonify({"error": "Invalid token"}), 400
    else:
        token = token_data.name
        print(str(token))
    try:
        user = dao.get_user_by_token(token)
        return jsonify(user), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

#get by plan id
@app.route('/User/Plan/<id>')
def get_users_by_plan_id(id):
    return jsonify(utils.convert_list_to_dict(dao.get_user_by_plan_id(id)))

# consume 1
@app.route('/User/Consume/<id>')
def consumeb_one(id):
    try:
        user = dao.get_user_by_id(id)
        if not user:
            return jsonify({"error":"no user with matching ID found"}), 404
        consumption = dao.consume_one(user)
        return jsonify({"consumption": consumption}), 200
    except Exception as e:
        return jsonify({"error":str(e)}), 500

# get consomption by user id
@app.route('/User/Consume/User/<id>')
def get_consomption_by_user_id(id):
    consumption = dao.get_consumption(id)
    return jsonify(consumption), 200

# reset consomption
@app.route('/User/Consume/Reset')
def reset_all_consomption():
    affected_rows = dao.reset_all_consumption()
    return {"affected_rows": affected_rows}, 200
    # have something returned, maybe int of reset users.

@app.route('/User/Add', methods=['POST'])
def add_user():
    user_json = request.get_json()
    if not user_json:
        return jsonify({"error":"Invalid Json data"}), 400
    try:
        user = User(**user_json)
        u = dao.add_user(user)
        return user.to_dict(), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# delete
@app.route('/User/Del/<id>', methods=['DELETE'])
def delete_user(id):
    user = dao.get_user_by_id(id)
    dao.remove_user(user)
    return jsonify(user.to_dict())

# update
@app.route('/User/Update/<id>', methods=['POST','PUT'])
def update_user(id):
    user_json = request.get_json()
    if not user_json:
        return jsonify({"error": "Invalid Json data"}), 400

    try:
        user = User(**user_json)
        dao.update_user(id, user)
        return user.to_dict(), 201
    except Exception as e:
        return jsonify({"error":str(e)}), 500

