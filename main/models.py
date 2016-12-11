from app import db


class User(db.Model):
    hash = db.Column(db.String, primary_key=True)
    name = db.Column(db.String)


class Site(db.Model):
    url = db.Column(db.String, primary_key=True)


class Event(db.Model):
    reputation = db.Column(db.Float)
    content = db.Column(db.Text, nullable=False)
