from flask_sqlalchemy import SQLAlchemy
from traitlets import default

db = SQLAlchemy()


def connect_db(app):
    db.app = app
    db.init_app(app)
    app.app_context().push()


class Pet(db.Model):
    """ Model for pet adoptions """

    __tablename__ = "pets"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(), nullable=False)
    species = db.Column(db.String(), nullable=False)
    photo_url = db.Column(db.String(
    ), default='https://th.bing.com/th/id/OIP.UYefmuqvYGCqQqZN9xaW8QHaGp?w=190&h=180&c=7&r=0&o=5&dpr=2&pid=1.7')
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, nullable=False, default=True)
