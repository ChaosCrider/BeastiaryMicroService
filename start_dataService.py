import config as config
from config import db, app
from controller.dao import beast_dao, ability_dao, plan_dao, user_dao

import utils.database_reset as db_restart

# db_restart.reset_db(db, app)


if __name__ == '__main__':
    config.app.run(debug=True, port='5601')
