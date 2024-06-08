from flask import request as flask_request, jsonify, json
import utils.utils as utils
from models.user import User
from config import db, app
from controller.auth.Authentication import encode, decode, hash_string


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
        token = flask_request.get_json()
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
            return jsonify(user_update.consumption)
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
            print('1')
            users_update = User.query.all()
            print(users_update)
            for user in users_update:
                user.consumption = 0
            db.session.commit()
            print(len(users_update))
            return jsonify(len(users_update))
        except Exception as e:
            print(f"An error occurred in reset_all_consumption: {e}")
            return -1

@app.route('/Data/User/Add', methods=['POST'])
def add_user():
    try:
        with app.app_context():
            user = None
            user_data = flask_request.get_json()
            print(user_data)
            if isinstance(user_data, dict):
                user = User(**user_data)
                print('User created')
            else:
                user = user_data
                print('user data not a dict')
            user.password = hash_string(user.password)
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


@app.route('/Data/User/login', methods=['POST'])
def login():
    credentials = flask_request.get_json()
    if credentials:
        try:
            if not isinstance(credentials, dict):
                credentials = json.loads(credentials)
            username = credentials.get('username', '')
            raw_password = credentials.get('password', '')
            hashed_password = hash_string(raw_password)
            try:
                user = User.query.filter_by(name=username, password=hashed_password).first()
                print(f" user token: [{user.token}]")
                if not user.token or user.token == '':
                    user.token = encode({"name":user.name, "password":user.password, "id": user.id})
                    db.session.commit()
                token = user.token
                return jsonify(token)
            except Exception as e:
                print('user.token could not be retreived')
                return e
        except Exception as e:
            return e
    else:
        return 'credentials not found'
