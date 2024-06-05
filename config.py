from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

user = 'root'
host = 'localhost'
database = 'beastiary'
charset = 'utf8'

app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{user}@{host}/{database}?charset={charset}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# target end point for controller
host = 'http://localhost:'
port = 5601


db = SQLAlchemy(app)

# creates and initializes the database
with app.app_context():
    db.create_all()


