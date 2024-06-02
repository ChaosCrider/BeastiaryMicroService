from flask import jsonify
from config import db, app
import persistance.dao.beast_dao as beast_dao
import utils.utils as utils

GET = []
POST = []
UPD = []

# @app.route('/Beast')
GET.append('http://localhost:5600/Beast')

# @app.route('/Beast/<id>')
GET.append('http://localhost:5600/Beast/4')

# @app.route('/Beast/Source/<source>')
GET.append('http://localhost:5600/Beast/Source/b')

# @app.route('/Beast/Add', methods=['POST'])
POST.append('http://localhost:5600/Beast/Add')

# @app.route('/Beast/Update/',methods=['PUT'])
UPD.append('http://localhost:5600/Beast/Update/6')

# @app.route('/Beast/Del/<id>', methods=['DElETE'])
