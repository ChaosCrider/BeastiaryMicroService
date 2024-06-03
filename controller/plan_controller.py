from flask import jsonify

import utils.utils as utils
import persistance.dao.plan_dao as plan_dao
from conn_config import db, app


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
    plans = dao.get_plan_uder_price(price)
    return jsonify(utils.convert_list_to_dict(plans))

#add
@app.route('/Plan', method=['POST'])
def add_plan(plan):
    dao.add_plan(plan)
    return jsonify(plan.to_dict())

#remove
@app.route('/Plan/Del', method=['DELETE'])
def remove_plan(plan):
    dao.remove_plan(plan)
    return jsonify(plan.to_dict())

#update
@app.route('/Plan/Update', method=['POST','PUT'])
def update_plan(plan):
    dao.update_plan(plan)
    return jsonify(plan.to_dict())
