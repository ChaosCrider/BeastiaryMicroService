from models.ability import Ability
from models.beast import Beast
from models.plan import Plan
from models.user import User
from controller.auth.Authentication import hash_string


def reset_db(db, app):
    # Drop all tables
    with app.app_context():
        db.drop_all()
    # Recreate all tables
    with app.app_context():
        db.create_all()

    # Add Beasts
    beasts = [
        Beast("AAA", "A", "AAA", "AAA"),
        Beast("BBB", "A", "BBB", "BBB"),
        Beast("CCC", "B", "CCC", "CCC"),
        Beast("DDD", "B", "DDD", "DDD"),
        Beast("EEE", "B", "EEE", "EEE"),
    ]

    with app.app_context():
        for beast in beasts:
            db.session.add(beast)
        db.session.commit()

    # Add Abilities
    abilities = [
        Ability("111", "111", "111"),
        Ability("222", "222", "222"),
        Ability("333", "333", "333"),
        Ability("444", "444", "444"),
        Ability("555", "5", "555"),
    ]

    with app.app_context():
        for ability in abilities:
            db.session.add(ability)
        db.session.commit()

    # Add Plans
    plans = [
        Plan("admin", 0, 65535),
        Plan("freemium", 0, 300),
        Plan("basic", 1, 1200),
        Plan("premium", 2.99, 5000)
    ]
    with app.app_context():
        for plan in plans:
            db.session.add(plan)
        db.session.commit()

    # Add Users
    users = [
        User("guest", hash_string("bubblegum0"), 2),
        User("admin", hash_string("coffeecrisp1"), 1),
        User("test", hash_string("gummyworm2"), 3),
    ]
    users[0].token='bdeb'
    users[1].token='1256'

    with app.app_context():
        for user in users:
            db.session.add(user)
        db.session.commit()
