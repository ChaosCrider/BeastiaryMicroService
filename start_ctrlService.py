import config as config
from config import db, app
from controller import beast_controller, ability_controller, plan_controller, user_controller

print('CICD is the worse thin kto setup, it never tells you what goes wrong , Hwo am i supposed to getanything done with this uncooperative deisgn...')

import utils.database_reset as db_restart

db_restart.reset_db(db, app)


if __name__ == '__main__':
    config.app.run(debug=True, port='5600')
