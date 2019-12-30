from sqlalchemy_utils import database_exists, create_database, drop_database
from hw18.view import app, db

if database_exists(db.engine.url):
    drop_database(db.engine.url)

if not database_exists(db.engine.url):
    create_database(db.engine.url)

db.init_app(app)
db.create_all()

if __name__ == "__main__":
    app.run()
