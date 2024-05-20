from models.beast import Beast


db = None
app = None

def __init__(self, db, app):
    self.db = db
    self.app = app

    def get_beasts():
        return Beast.query.all()

    def get_beast_by_id(id):
        return Beast.query.filter_by(id=id)

    def get_beast_by_source(source):
        return Beast.query.filter_by(source = source)

    def add_beast(beast):
        with app.app_context():
            db.session.add(beast)
            db.session.commit()

    def remove_beast(beast):
        with app.app_context():
            db.session.delete(beast)
            db.session.commit()

    def update_beast(beast):
        beast_update = Beast.query.filter_by(id = beast.id)
        beast_update.name = beast.name
        beast_update.source = beast.source
        beast_update.description = beast.description
        beast_update.stat_block = beast.stat_block
        with app.app_context():
            db.session.commit()