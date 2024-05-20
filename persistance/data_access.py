from _mod_main import db, app

# Ensure the engine is correctly set from Flask-SQLAlchemy's db
engine = db.engine


def drop_all():
    with app.app_context():
        db.drop_all()

def create_all():
    with app.app_context():
        db.create_all()



'''

#setup for mowes - phpmyadmin
engine = create_engine("sqlite+pysqlite:///root@127.0.0.1/beastiary", echo=True)
print(engine)
print("data_access engine boot attempt")

#other connection string attemps
#"sqlite+pysqlite:///:memory:", echo=True
#"mysql+mysqldb://root@127.0.0.1/beastiary"
#"mssql+pyodbc:///?odbc_connect=Driver%3D%7BSQL+Server%7D%3BServer%3D%28LocalDB%29%5CMSSQLlocalDB%3BDatabase%3DRevisionIntra%3BTrusted_Connection%3Dyes%3BEncrypt%3Dyes"


metadata = MetaData()
metadata.bind = engine

class Base(DeclarativeBase):
    pass


def create_all(engine):
    Base.metadata.create_all(engine)


def drop_all(engine):
    Base.metadata.drop_all(engine)
   
'''