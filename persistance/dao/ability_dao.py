from models.ability import Ability

class AbilityDAO:
    db = None
    app = None

    def __init__(self, db, app):
        self.db = db
        self.app = app

    def get_abilities(self):
        try:
            return Ability.query.all()
        except Exception as e:
            print(f"An error occurred in get_abilities: {e}")
            return None

    def get_ability_by_id(self, id):
        try:
            return Ability.query.filter_by(id=id).first_or_404()
        except Exception as e:
            print(f"An error occurred in get_ability_by_id: {e}")
            return None

    def add_ability(self, ability):
        try:
            with self.app.app_context():
                self.db.session.add(ability)
                self.db.session.commit()
        except Exception as e:
            print(f"An error occurred in add_ability: {e}")

    def remove_ability(self, ability):
        try:
            with self.app.app_context():
                self.db.session.delete(ability)
                self.db.session.commit()
        except Exception as e:
            print(f"An error occurred in remove_ability: {e}")

    def update_ability(self, ability):
        try:
            ability_update = Ability.query.filter_by(id=ability.id)
            ability_update.name = ability.name
            ability_update.short_description = ability.short_description
            ability_update.mechanics = ability.mechanics
            with self.app.app_context():
                self.db.session.commit()
        except Exception as e:
            print(f"An error occurred in update_ability: {e}")
