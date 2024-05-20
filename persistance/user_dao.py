
from models.user import User

db = None
app = None


def __init__(self, db, app):
    self.db = db
    self.app = app

    def get_users():
        users = User.query.all()
        return users

    def get_user_by_id(id):
        user = User.query.filter_by(id=id).first_or_404()
        return user

    def get_user_by_token(token):
        user = User.query.filter_by(token=token).first_or_404()
        return user

    def get_user_by_plan_id(id):
        users = User.query.filter_by(plan_id=id)
        return users

    def consume_one(user):
        user_update = User.query.filter_by(id=user.id)
        user_update.consumption += 1
        with app.app_context():
            db.session.commit()

    def reset_all_consumption():
        users_update = User.query.all()
        for user in users_update:
            user.consumption = 0
        with app.app_context():
            db.session.commit()

    def add_user(user):
        with app.app_context():
            db.session.add(user)
            db.session.commit()

    def remove_user(user):
        with app.app_context():
            db.session.delete(user)
            db.session.commit()

    def update_user(user):
        with app.app_context(user):
            user_update = User.query.filter_by(id == user.id)
            user_update.name = user.name
            user_update.password = user.password
            user_update.token = user.token
            user_update.plan_id = user.plan_id
            db.session.commit()
