GET = []
POST = []
UPD = []




# @app.route('/Plan')
GET.append('http://localhost:5600/Plan')


# @app.route('/Plan/<id>')
GET.append('http://localhost:5600/Plan/2')


# @app.route('/Plan/Price/<price>')
GET.append('http://localhost:5600/Plan/Price/100')

# @app.route('/Plan/Add', methods=['POST'])
POST.append('http://localhost:5600/Plan/Add')


# @app.route('/Plan/Update/<id>', methods=['POST','PUT'])
UPD.append('http://localhost:5600/Plan/Update/2')


# @app.route('/Plan/Del/<id>', methods=['DELETE'])
