from models.plan import Plan


db = None
app = None

def __init__(self, db, app):
    self.db = db
    self.app = app

    def get_plans():
        return Plan.query.all()

    def get_plan_by_id(id):
        return Plan.query.filter_by(id = id).first_or_404()

    def get_plan_uder_price(price):
        return Plan.query.filter_by(price < price).get_or_404()

    def add_plan(plan):
        with app.app_context():
            db.session.add(plan)
            db.session.commit()

    def remove_plan(plan):
        with app.app_context():
            db.session.delete(plan)
            db.session.commit()

    def update_plan(plan):
        plan_update = Plan.query.filter_by(id = plan.id)
        plan_update.name = plan.name
        plan_update.price = plan
        plan_update.monthly_allowance = plan.monthly_allowance
        with app.app_context():
            db.session.commit()
