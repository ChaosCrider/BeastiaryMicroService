from models.user import User

class UserDAO:
    db = None
    app = None

    def __init__(self, db, app):
        self.db = db
        self.app = app

    def get_users(self):
        try:
            users = User.query.all()
            return users
        except Exception as e:
            print(f"An error occurred in get_users: {e}")
            return None

    def get_user_by_id(self, id):
        try:
            user = User.query.filter_by(id=id).first_or_404()
            return user
        except Exception as e:
            print(f"An error occurred in get_user_by_id: {e}")
            return None

    def get_user_by_token(self, token):
        try:
            user = User.query.filter_by(token=token).first_or_404()
            return user
        except Exception as e:
            print(f"An error occurred in get_user_by_token: {e}")
            return None

    def get_user_by_plan_id(self, id):
        try:
            users = User.query.filter_by(plan_id=id).all()
            return users
        except Exception as e:
            print(f"An error occurred in get_user_by_plan_id: {e}")
            return None

    def consume_one(self, user):
        try:
            with self.app.app_context():
                user_update = User.query.filter_by(id=user.id).first_or_404()
                user_update.consumption += 1
                self.db.session.commit()
                return user_update.consumption
        except Exception as e:
            print(f"An error occurred in consume_one: {e}")
            return None

    def get_consumption(self, user_id):
        try:
            u = User.query.filter_by(id=user_id).first_or_404()
            return u.consumption
        except Exception as e:
            print(f"An error occurred in get_consumption: {e}")
            return -1

    def reset_all_consumption(self):
        with self.app.app_context():
            try:
                users_update = User.query.all()
                for user in users_update:
                    user.consumption = 0
                self.db.session.commit()
                return len(users_update)
            except Exception as e:
                print(f"An error occurred in reset_all_consumption: {e}")
                return -1

    def add_user(self, user):
        try:
            with self.app.app_context():
                self.db.session.add(user)
                self.db.session.commit()
                print('user after commit: ', user)
            return user
        except Exception as e:
            print(f"An error occurred in add_user: {e}")
            return str(e)

    def remove_user(self, user):
        try:
            with self.app.app_context():
                self.db.session.delete(user)
                self.db.session.commit()
            return user
        except Exception as e:
            print(f"An error occurred in remove_user: {e}")
            return None

    def update_user(self, id, user):
        try:
            with self.app.app_context():
                user_update = User.query.filter_by(id=id).first_or_404()
                user_update.name = user.name
                user_update.password = user.password
                user_update.token = user.token
                user_update.plan_id = user.plan_id
                self.db.session.commit()
            return user
        except Exception as e:
            print(f"An error occurred in update_user: {e}")
            return None
