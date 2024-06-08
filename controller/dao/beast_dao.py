from flask import request as flask_request, jsonify
import utils.utils as utils
from models.beast import Beast
from config import db, app


@app.route('/Data/Beast')
def get_beasts():
    try:
        beasts = Beast.query.all()
        print('beasts: ', beasts)
        return jsonify(utils.convert_list_to_dict(beasts))
    except Exception as e:
        print(f"An error occurred in get_beasts: {e}")
        return jsonify(e)


@app.route('/Data/Beast/<id>')
def get_beast_by_id(id):
    try:
        beast = Beast.query.filter_by(id=id).first_or_404()
        return beast.to_dict()
    except Exception as e:
        print(f"An error occurred in get_beast_by_id: {e}")
        return e

@app.route('/Data/Beast/Source/<source>')
def get_beast_by_source(source):
    try:
        beasts = Beast.query.filter_by(source=source).all()
        return jsonify(utils.convert_list_to_dict(beasts))
    except Exception as e:
        print(f"An error occurred in get_beast_by_source: {e}")
        return None

@app.route('/Data/Beast/Add', methods=['POST'])
def add_beast():
    try:
        with app.app_context():
            beast = None
            beast_data = flask_request.get_json()
            if isinstance(beast_data, dict):
                beast = Beast(**beast_data)
            else:
                beast = beast_data
            db.session.add(beast)
            db.session.commit()
            return beast.to_dict()
    except Exception as e:
        print(f"An error occurred in add_beast: {e}")
        db.session.rollback()
        return e


@app.route('/Data/Beast/Del/<beast_id>', methods=['DELETE'])
def remove_beast(beast_id):
    print('del beast dao reached')
    try:
        with app.app_context():
            print(1)
            beast = Beast.query.filter_by(id = beast_id).first_or_404()
            print(2)
            db.session.delete(beast)
            print(3)
            db.session.commit()
            print(4)
        return beast.to_dict()
    except Exception as e:
        print(f"An error occurred in remove_beast: {e}")
        return None


@app.route('/Data/Beast/Update/<beast_id>', methods=['PUT'])
def update_beast(beast_id):
    try:
        beast_json = flask_request.get_json()
        if not beast_json:
            return jsonify({'error': 'No input data provided'}), 400

        beast = Beast.query.filter_by(id=beast_id).first()
        if not beast:
            return jsonify({'error': 'Beast not found'}), 404

        beast.name = beast_json.get('name', beast.name)
        beast.source = beast_json.get('source', beast.source)
        beast.description = beast_json.get('description', beast.description)
        beast.stat_block = beast_json.get('stat_block', beast.stat_block)
        db.session.commit()

        updated_beast = Beast.query.filter_by(id=beast_id).first()
        return jsonify(updated_beast.to_dict()), 200
    except Exception as e:
        print(f"An error occurred in update_beast: {e}")
        return jsonify({'error': 'An error occurred'}), 500