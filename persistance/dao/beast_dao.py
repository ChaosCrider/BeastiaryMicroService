from models.beast import Beast

class BeastDAO:
    db = None
    app = None

    def __init__(self, db, app):
        self.db=db
        self.app=app

    def get_beasts(self):
        try:
            return Beast.query.all()
        except Exception as e:
            print(f"An error occurred in get_beasts: {e}")
            return None

    def get_beast_by_id(self, id):
        try:
            return Beast.query.filter_by(id=id).first_or_404()
        except Exception as e:
            print(f"An error occurred in get_beast_by_id: {e}")
            return None

    def get_beast_by_source(self, source):
        try:
            return Beast.query.filter_by(source=source).all()
        except Exception as e:
            print(f"An error occurred in get_beast_by_source: {e}")
            return None

    '''
    def add_beast(self, beast):
        try:
            with self.app.app_context():
                self.db.session.add(beast)
                self.db.session.commit()
            return beast
        except Exception as e:
            print(f"An error occurred in add_beast: {e}")
            return None

    '''
    def add_beast(self, beast_data):
        try:
            with self.app.app_context():
                if isinstance(beast_data, dict):
                    beast = Beast(**beast_data)
                else:
                    beast = beast_data
                self.db.session.add(beast_data)
                self.db.session.commit()
            return beast_data
        except Exception as e:
            print(f"An error occurred in add_beast: {e}")
            self.db.session.rollback()
            return None



    def remove_beast(self, beast):
        try:
            with self.app.app_context():
                self.db.session.delete(beast)
                self.db.session.commit()
            return beast
        except Exception as e:
            print(f"An error occurred in remove_beast: {e}")
            return None

    def update_beast(self, beast_id, beast):
        try:
            beast_update = Beast.query.filter_by(id=beast_id)
            beast_update.name = beast.name
            beast_update.source = beast.source
            beast_update.description = beast.description
            beast_update.stat_block = beast.stat_block
            with self.app.app_context():
                self.db.session.commit()
            return beast
        except Exception as e:
            print(f"An error occurred in update_beast: {e}")
            return None