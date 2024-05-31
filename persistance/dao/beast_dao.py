from models.beast import Beast

class BeastDAO:
    db = None
    app = None

    def __init__(self, db, app):
        self.db = db
        self.app = app

    def get_beasts(self,):
        return Beast.query.all()

    def get_beast_by_id(self, id):
        return Beast.query.filter_by(id=id).first_or_404()

    def get_beast_by_source(self, source):
        return Beast.query.filter_by(source = source).all()

    def add_beast(self, beast):
        with self.app.app_context():
            self.db.session.add(beast)
            self.db.session.commit()

    def remove_beast(self, beast):
        with self.app.app_context():
            self.db.session.delete(beast)
            self.db.session.commit()

    def update_beast(self, id):
        beast_update = Beast.query.filter_by(id = beast.id)
        beast_update.name = beast.name
        beast_update.source = beast.source
        beast_update.description = beast.description
        beast_update.stat_block = beast.stat_block
        with self.app.app_context():
            self.db.session.commit()