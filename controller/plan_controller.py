from flask import jsonify, request

import utils.utils as utils
import persistance.dao.plan_dao as plan_dao
from config import db, app
from models.plan import Plan

dao = plan_dao.PlanDAO (db, app)


#get all
@app.route('/Plan')
def get_plans():
    plans = dao.get_plans()
    return jsonify(utils.convert_list_to_dict(plans))

#get by id
@app.route('/Plan/<id>')
def get_plan_by_id(id):
    plan = dao.get_plan_by_id(id)
    return jsonify(plan.to_dict())

#get_under_price
@app.route('/Plan/Price/<price>')
def get_plan_under_price(price):
    plans = dao.get_plan_under_price(price)
    return jsonify(utils.convert_list_to_dict(plans))

#add
@app.route('/Plan/Add', methods=['POST'])
def add_plan():
    plan_json = request.get_json()
    if not plan_json:
        return jsonify({"error": "Invalid Json data"}), 400

    try:
        plan = Plan(**plan_json)
        dao.add_plan(plan)
        return jsonify(plan), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

#remove
@app.route('/Plan/Del/<id>', methods=['DELETE'])
def remove_plan(id):
    plan = dao.get_plan_by_id(id)
    dao.remove_plan(plan)
    return jsonify(plan)

#update
@app.route('/Plan/Update/<id>', methods=['POST','PUT'])
def update_plan(id):
    plan_json = request.get_json()
    if not plan_json:
        return jsonify({"error":"Invalid Json data"}), 400

    try:
        plan = dao.get_plan_by_id(id)
        dao.update_plan(id, plan)
        return jsonify(plan.to_dict()), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
