import _mod_main
from _mod_main import db, app

import utils.database_reset as db_restart
db_restart.reset_db(db, app)

if __name__ == '__main__':
    _mod_main.app.run(debug=True)