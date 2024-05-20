from conn_config import db
class Plan(db.Model):
    __tablename__="plans"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    price = db.Column(db.Float, nullable=False)
    monthly_allowance = db.Column(db.Integer, nullable=False)

    users = db.relationship('User', backref='plan', lazy =True)

    def __str__(self):
        return f"Plan: {self.name}, Price: {self.price}, Monthly allowance: {self.monthly_allowance}"

    def __init__(self, name, price, monthly_allowance):
        self.name = name
        self.price = price
        self.monthly_allowance = monthly_allowance


