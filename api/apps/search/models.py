from store.gino import db
from sqlalchemy import DateTime


class Post(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer())
    text = db.Column(db.String())
    created_date = db.Column(DateTime)
    rubrics = db.Column(db.String())
