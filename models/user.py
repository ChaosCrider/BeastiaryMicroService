from config import db

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    token = db.Column(db.String(90), nullable=True)
    consumption = db.Column(db.Integer, nullable=False)

    #Foreign keys
    plan_id = db.Column(db.Integer, db.ForeignKey('plans.id'), nullable=True)

    def __str__(self):
        return f"{self.name} - current plan: {self.plan}"

    def __init__(self, name, password, plan_id):
        self.name = name
        self.password = password
        self.plan_id = plan_id
        self.consumption = 0

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'password': self.password,
            'plan_id': self.plan_id,
            'consumption': self.consumption
        }
