from models.plan import Plan

class PlanDAO:
    db = None
    app = None

    def __init__(self, db, app):
        self.db = db
        self.app = app

    def get_plans(self,):
        return Plan.query.all()

    def get_plan_by_id(self, id):
        return Plan.query.filter_by(id = id).first_or_404()

    def get_plan_uder_price(self, price):
        return Plan.query.filter_by(price < price).get_or_404()

    def add_plan(self,plan):
        with self.app.app_context():
            self.db.session.add(plan)
            self.db.session.commit()

    def remove_plan(self,plan):
        with self.app.app_context():
            self.db.session.delete(plan)
            self.db.session.commit()

    def update_plan(self,plan):
        plan_update = Plan.query.filter_by(id = plan.id)
        plan_update.name = plan.name
        plan_update.price = plan
        plan_update.monthly_allowance = plan.monthly_allowance
        with self.app.app_context():
            self.db.session.commit()
