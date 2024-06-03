GET = []
POST = []
UPD = []

# @app.route('/User')
GET.append('http://localhost:5600/User')

# @app.route('/User/<id>')
GET.append('http://localhost:5600/User/2')

# @app.route('/User/token/', methods=['POST'])
# POST.append('http://localhost:5600/User/token/')

# @app.route('/User/Plan/<id>')
GET.append('http://localhost:5600/User/Plan/2')

# @app.route('/User/Consume/<id>') # perform the consume action on an account
GET.append('http://localhost:5600/User/Consume/2')

# @app.route('/User/Consume/User/<id>') # returns the consumption left for a user
GET.append('http://localhost:5600/User/Consume/User/2')

# @app.route('/User/Consume/Reset')
GET.append('http://localhost:5600/User/Consume/Reset')

# @app.route('/User/Add', methods=['POST'])
POST.append('http://localhost:5600/User/Add')

# @app.route('/User/Del/<id>', methods=['DELETE'])
# DEL.append('http://localhost:5600/User/Del/4')

# @app.route('/User/Update/<id>', methods=['POST','PUT'])
UPD.append('http://localhost:5600/User/Update/4')