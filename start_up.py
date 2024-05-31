import conn_config
from conn_config import db, app
import controller._mod_beast_controller
import utils.database_reset as db_restart


db_restart.reset_db(db, app)


if __name__ == '__main__':
    conn_config.app.run(debug=True, port='5600')