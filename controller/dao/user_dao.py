from flask import request as flask_request, jsonify
import utils.utils as utils
from models.user import User
from config import db, app

# to add:
# get token by username/password,
# set token,
# check consume vs plan



@app.route('/Data/User')
def get_users():
    try:
        users = User.query.all()
        return jsonify(utils.convert_list_to_dict(users))
    except Exception as e:
        print(f"An error occurred in get_users: {e}")
        return None

@app.route('/Data/User/<id>')
def get_user_by_id(id):
    try:
        user = User.query.filter_by(id=id).first_or_404()
        return user.to_dict()
    except Exception as e:
        print(f"An error occurred in get_user_by_id: {e}")
        return None

@app.route('/Data/User/Token', methods=['POST'])
def get_user_by_token():
    try:
        json = flask_request.get_json()
        token = json.get('token', '')
        user = User.query.filter_by(token=token).first_or_404()
        return user.to_dict()
    except Exception as e:
        print(f"An error occurred in get_user_by_token: {e}")
        return e

@app.route('/Data/User/Plan/<user_id>')
def get_user_by_plan_id(user_id):
    try:
        users = User.query.filter_by(plan_id=user_id).all()
        return jsonify(utils.convert_list_to_dict(users))
    except Exception as e:
        print(f"An error occurred in get_user_by_plan_id: {e}")
        return None

@app.route('/Data/User/Consume/<user_id>')
def consume_one(user_id):
    try:
        with app.app_context():
            user_update = User.query.filter_by(id=user_id).first_or_404()
            user_update.consumption += 1
            db.session.commit()
            return user_update.consumption
    except Exception as e:
        print(f"An error occurred in consume_one: {e}")
        return None

@app.route('/Data/User/Consume/User/<user_id>')
def get_consumption(user_id):
    try:
        u = User.query.filter_by(id=user_id).first_or_404()
        return u.consumption
    except Exception as e:
        print(f"An error occurred in get_consumption: {e}")
        return -1

@app.route('/Data/User/Consume/Reset')
def reset_all_consumption():
    with app.app_context():
        try:
            users_update = User.query.all()
            for user in users_update:
                user.consumption = 0
            db.session.commit()
            return len(users_update)
        except Exception as e:
            print(f"An error occurred in reset_all_consumption: {e}")
            return -1

@app.route('/Data/User/Add', methods=['POST'])
def add_user():
    try:
        with app.app_context():
            user = None
            user_data = flask_request.get_json()
            if isinstance(user_data, dict):
                user = User(**user_data)
                print('User created')
            else:
                user = user_data
                print('user data not a dict')
            db.session.add(user)
            db.session.commit()
            return user.to_dict()
    except Exception as e:
        print(f"An error occurred in add_user: {e}")
        return str(e)

@app.route('/Data/User/Del/<user_id>', methods=['DELETE'])
def remove_user(user_id):
    try:
        with app.app_context():
            user = User.query.filter_by(id=user_id).first()
            db.session.delete(user)
            db.session.commit()
        return user.to_dict()
    except Exception as e:
        print(f"An error occurred in remove_user: {e}")
        return None

@app.route('/Data/User/Update/<user_id>')
def update_user(user_id):
    try:
        with app.app_context():
            user_json = flask_request.get_json()
            user = User.query.filter_by(id=user_id).first_or_404()
            user.name = user_json.get('name', user.name)
            user.password = user_json.get('password', user.password)
            user.token = user_json.get('token', user.token)
            user.plan_id = user_json.get('plan_id', user.plan_id)
            user.consumption = user_json.get('consumption', user.consumption)
            db.session.commit()
            return user.to_dict()
    except Exception as e:
        print(f"An error occurred in update_user: {e}")
        return None
