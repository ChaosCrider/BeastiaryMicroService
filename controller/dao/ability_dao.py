from flask import request as flask_request, jsonify
import utils.utils as utils
from models.ability import Ability
from config import db, app

@app.route('/Data/Ability')
def get_abilities():
    try:
        abilities = Ability.query.all()
        return jsonify(utils.convert_list_to_dict(abilities))
    except Exception as e:
        print(f"An error occurred in get_beasts: {e}")
        return jsonify(e)

@app.route('/Data/Ability/<ability_id>')
def get_ability_by_id(ability_id):
    try:
        ability = Ability.query.filter_by(id=ability_id).first_or_404()
        return ability.to_dict()
    except Exception as e:
        print(f"An error occurred in get_beast_by_id: {e}")
        return e

@app.route('/Data/Ability/Add', methods=['POST'])
def add_ability():
    try:
        with app.app_context():
            ability = None
            beast_data = flask_request.get_json()
            print(beast_data)
            if isinstance(beast_data, dict):
                ability = Ability(**beast_data)
            else:
                ability = beast_data
            db.session.add(ability)
            db.session.commit()
            return ability.to_dict()
    except Exception as e:
        print(f"An error occurred in add_beast: {e}")
        db.session.rollback()
        return e

@app.route('/Data/Ability/Del')
def remove_ability(ability_id):
    try:
        with app.app_context():
            ability = Ability.query.filter_by(id = ability_id)
            db.session.delete(ability)
            db.session.commit()
            return ability
    except Exception as e:
        print(f"An error occurred in remove_beast: {e}")
        return None

@app.route('/Data/Ability/Update/<ability_id>', methods=['PUT'])
def update_ability(ability_id):
    try:
        ability_json = flask_request.get_json()
        print('ability_json: ', ability_json)
        if not ability_json:
            return jsonify({'error': 'No input data provided'}), 400

        ability = Ability.query.filter_by(id=ability_id).first()
        print('ability: ', ability)
        if not ability:
            return jsonify({'error': 'Beast not found'}), 404

        ability.name = ability_json.get('name', ability.name)
        ability.mechanics = ability_json.get('source', ability.mechanics)
        ability.short_description = ability_json.get('description', ability.short_description)
        db.session.commit()

        updated_ability = Ability.query.filter_by(id=ability_id).first()
        return jsonify(updated_ability.to_dict()), 200
    except Exception as e:
        print(f"An error occurred in update_beast: {e}")
        return jsonify({'error': 'An error occurred'}), 500