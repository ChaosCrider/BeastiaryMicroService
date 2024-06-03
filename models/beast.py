from conn_config import db
import json


class Beast(db.Model):
    __tablename__ = "Beasts"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    source = db.Column(db.String(30), nullable=False)
    description = db.Column(db.String(120), nullable=False)
    stat_block = db.Column(db.String(30), nullable=True)

    def __str__(self):
        return f"{self.name} : {self.description}"

    def __init__(self, name, source, desctiption, stat_block):
        self.name = name
        self.source = source
        self.description = desctiption
        self.stat_block = stat_block

    #Converts the instance to a dictionary
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'source': self.source,
            'description': self.description,
            'stat_block': self.stat_block
        }
