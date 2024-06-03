from models.plan import Plan

class PlanDAO:
    db = None
    app = None

    def __init__(self, db, app):
        self.db = db
        self.app = app

    def get_plans(self):
        try:
            return Plan.query.all()
        except Exception as e:
            print(f"An error occurred in get_plans: {e}")
            return None

    def get_plan_by_id(self, id):
        try:
            return Plan.query.filter_by(id=id).first_or_404()
        except Exception as e:
            print(f"An error occurred in get_plan_by_id: {e}")
            return None

    def get_plan_under_price(self, price):
        try:
            return Plan.query.filter(Plan.price < price).all()
        except Exception as e:
            print(f"An error occurred in get_plan_under_price: {e}")
            return None

    def add_plan(self, plan):
        try:
            with self.app.app_context():
                self.db.session.add(plan)
                self.db.session.commit()
            return plan
        except Exception as e:
            print(f"An error occurred in add_plan: {e}")
            return None

    def remove_plan(self, plan):
        try:
            with self.app.app_context():
                self.db.session.delete(plan)
                self.db.session.commit()
            return plan
        except Exception as e:
            print(f"An error occurred in remove_plan: {e}")
            return None

    def update_plan(self, plan):
        try:
            plan_update = Plan.query.filter_by(id=plan.id).first_or_404()
            plan_update.name = plan.name
            plan_update.price = plan.price
            plan_update.monthly_allowance = plan.monthly_allowance
            with self.app.app_context():
                self.db.session.commit()
            return plan
        except Exception as e:
            print(f"An error occurred in update_plan: {e}")
            return None
