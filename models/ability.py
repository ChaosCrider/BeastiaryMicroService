from config import db

class Ability(db.Model):
    __tablename__ = "abilities"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    short_description = db.Column(db.String(200), nullable=False)
    mechanics = db.Column(db.String(600), nullable=False)  # Intended for JSON formatting

    def __str__(self):
        return f"{self.name} : {self.short_description}"


    def __init__(self, name, short_description, mechanics):
        self.name = name
        self.short_description = short_description
        self.mechanics = mechanics


    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'short_description': self.short_description,
            'mechanics': self.mechanics
        }