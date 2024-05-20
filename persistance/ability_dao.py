from models.ability import Ability

db = None
app = None


def __init__(self, db, app):
    self.db = db
    self.app = app

    def get_abilities():
        return Ability.query.all()

    def get_ability_by_id(id):
        return Ability.query.filter_by(id=id)

    def add_ability(ability):
        with app.app_context():
            db.session.add(ability)
            db.session.commmit()

    def remove_ability(ability):
        with app.app_context():
            db.session.delete(ability)
            db.session.commmit()

    def update_ability(ability):
        ability_update = Ability.query.filter_by(id = ability.id)
        ability_update.name = ability.name
        ability_update.short_description = ability.short_description
        ability_update.mechanics = ability.mechanics
        with app.app_context():
            db.session.commmit()