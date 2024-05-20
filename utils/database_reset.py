from models.ability import Ability
from models.beast import Beast
from models.plan import Plan
from models.user import User


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
        Plan("aaa", "1", "10"),
        Plan("bbb", "4", "50"),
        Plan("ccc", "175", "250"),
    ]
    with app.app_context():
        for plan in plans:
            db.session.add(plan)
        db.session.commit()

    # Add Users
    users = [
        User("bubblegum", "bubblegum0", 1),
        User("coffeecrisp", "coffeecrisp1", 2),
        User("gummyworm", "gummyworm2", 3),
    ]

    with app.app_context():
        for user in users:
            db.session.add(user)
        db.session.commit()
