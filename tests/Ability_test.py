GET = []
POST = []
UPD = []

# @app.route('/Ability')
GET.append('http://localhost:5600/Ability')

# @app.route('/Ability/<id>')
GET.append('http://localhost:5600/Ability/2')

# @app.route('/Ability/Add', methods=['POST'])
POST.append('http://localhost:5600/Ability/Add')

# @app.route('/Ability/Update/',methods=['PUT'])
UPD.append('http://localhost:5600/Ability/Update/2')


# @app.route('/Ability/Del', method=['DELETE'])
