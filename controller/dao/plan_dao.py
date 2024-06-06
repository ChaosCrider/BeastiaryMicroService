from flask import request as flask_request, jsonify
import utils.utils as utils
from config import db, app
from models.plan import Plan

@app.route('/Data/Plan')
def get_plans():
    try:
        plans = Plan.query.all()
        return jsonify(utils.convert_list_to_dict(plans))
    except Exception as e:
        print(f"An error occurred in get_plans: {e}")
        return e

@app.route('/Data/Plan/<plan_id>')
def get_plan_by_id(plan_id):
    try:
        plan = Plan.query.filter_by(id=plan_id).first_or_404()
        return plan.to_dict()
    except Exception as e:
        print(f"An error occurred in get_plan_by_id: {e}")
        return e

@app.route('/Data/Plan/Price/<price>')
def get_plan_under_price(price):
    try:
        plans = Plan.query.filter(Plan.price < price).all()
        return jsonify(utils.convert_list_to_dict(plans))
    except Exception as e:
        print(f"An error occurred in get_plan_under_price: {e}")
        return e

@app.route('/Data/Plan/Add', methods=['POST'])
def add_plan():
    try:
        plan_json = flask_request.get_json()
        if not plan_json:
            return jsonify({'error': 'No input data provided'}), 400
        plan = Plan(**plan_json)

        db.session.add(plan)
        db.session.commit()
        return plan.to_dict()
    except Exception as e:
        print(f"An error occurred in add_plan: {e}")
        return e

@app.route('/Data/Plan/Del/<plan_id>', methods=['DELETE'])
def remove_plan(plan_id):
    try:
        with app.app_context():
            plan = Plan.query.filter_by(id=plan_id).first_or_404()
            db.session.delete(plan)
            db.session.commit()
        return plan.to_ditc()
    except Exception as e:
        print(f"An error occurred in remove_plan: {e}")
        return e

@app.route('/Data/Plan/Update/<plan_id>', methods=['PUT'])
def update_plan(plan_id):
    try:
        plan_json = flask_request.get_json()
        if not plan_json:
            return jsonify({'error': 'No input data provided'}), 400

        plan = Plan.query.filter_by(id=plan_id).first()
        if not plan:
            return jsonify({'error': 'Plan not found'}), 404
        
        plan.name = plan_json.get('name', plan.name)
        plan.price = plan_json.get('price', plan.price)
        plan.monthly_allowance = plan_json.get('monthly_allowance', plan.monthly_allowance)
        db.session.commit()

        updated_plan = Plan.query.filter_by(id=plan_id).first()
        return updated_plan.to_dict(), 200
    except Exception as e:
        print(f"An error occurred in update_plan: {e}")
        return e
