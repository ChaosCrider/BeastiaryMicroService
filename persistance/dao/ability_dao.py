from models.ability import Ability

class AbilityDAO:
    db = None
    app = None


    def __init__(self, db, app):
        self.db = db
        self.app = app

    def get_abilities(self):
        return Ability.query.all()

    def get_ability_by_id(self, id):
        return Ability.query.filter_by(id=id)

    def add_ability(self, ability):
        with self.app.app_context():
            self.db.session.add(ability)
            self.db.session.commmit()

    def remove_ability(self, ability):
        with self.app.app_context():
            self.db.session.delete(ability)
            self.db.session.commmit()

    def update_ability(self, ability):
        ability_update = Ability.query.filter_by(id = ability.id)
        ability_update.name = ability.name
        ability_update.short_description = ability.short_description
        ability_update.mechanics = ability.mechanics
        with self.app.app_context():
            self.db.session.commmit()