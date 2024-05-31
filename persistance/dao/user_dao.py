from models.user import User

class UserDAO:
    db = None
    app = None


    def __init__(self, db, app):
        self.db = db
        self.app = app

    def get_users(self):
        users = User.query.all()
        return users

    def get_user_by_id(self,id):
        user = User.query.filter_by(id=id).first_or_404()
        return user

    def get_user_by_token(self,token):
        user = User.query.filter_by(token=token).first_or_404()
        return user

    def get_user_by_plan_id(self,id):
        users = User.query.filter_by(plan_id=id)
        return users

    def consume_one(self,user):
        user_update = User.query.filter_by(id=user.id)
        user_update.consumption += 1
        with self.app.app_context():
            self.db.session.commit()

    def reset_all_consumption(self):
        users_update = User.query.all()
        for user in users_update:
            user.consumption = 0
        with self.app.app_context():
            self.db.session.commit()

    def add_user(self,user):
        with self.app.app_context():
            self.db.session.add(user)
            self.db.session.commit()

    def remove_user(self,user):
        with self.app.app_context():
            self.db.session.delete(user)
            self.db.session.commit()

    def update_user(self,user):
        with self.app.app_context(user):
            user_update = User.query.filter_by(id == user.id)
            user_update.name = user.name
            user_update.password = user.password
            user_update.token = user.token
            user_update.plan_id = user.plan_id
            self.db.session.commit()
