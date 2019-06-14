from datetime import datetime
from app import db

def create_tables():
    metadata = db.MetaData()
    users_table = db.Table('user', metadata,
        db.Column('id', db.Integer, primary_key=True),
        db.Column('login', db.String, unique=True),
        db.Column('hash_password', db.String)
    )

    posts_table = db.Table('post', metadata,
        db.Column('id', db.Integer, primary_key=True),
        db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
        db.Column('title', db.String),
        db.Column('body', db.String),
        db.Column('publication_date', db.DateTime)
    )

    posts_table = db.Table('comment', metadata,
        db.Column('id', db.Integer, primary_key=True),
        db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
        db.Column('post_id', db.Integer, db.ForeignKey('post.id')),
        db.Column('body', db.String),
        db.Column('publication_date', db.DateTime),
    )

    posts_table = db.Table('subscriber', metadata,
        db.Column('id', db.Integer, primary_key=True),
        db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
        db.Column('subscriber_id', db.Integer, db.ForeignKey('user.id'))
    )

    metadata.create_all(db.engine)

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String, unique=True)
    hash_password = db.Column(db.String)

    def __init__(self, login, hash_password):
        self.login = login
        self.hash_password = hash_password

    def to_dict(self):
        dict = {
            'id' : self.id,
            'login' : self.login,
            'hash_password' : self.hash_password
        }
        return dict

    def __repr__(self):
        return '<User {}, {}>'.format(self.login, self.hash_password)

class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    title = db.Column(db.String)
    body = db.Column(db.String)
    publication_date = db.Column(db.DateTime)

    def __init__(self, user_id, title, body, publication_date):
        self.user_id = user_id
        self.title = title
        self.body = body
        self.publication_date = publication_date

    def to_dict(self):
        dict = {
            'id' : self.id,
            'user_id' : self.user_id,
            'title' : self.title,
            'body' : self.body,
            'publication_date' : str(self.publication_date)
        }
        return dict

    def __repr__(self):
        return '<Post {}, {}, {}, {}>'.format(self.user_id, self.title, self.body, self.publication_date)

class Comment(db.Model):
    __tablename__ = 'comment'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))
    body = db.Column(db.String)
    publication_date = db.Column(db.DateTime)

    def __init__(self, user_id, post_id, body, publication_date):
        self.user_id = user_id
        self.post_id = post_id
        self.body = body
        self.publication_date = publication_date

    def to_dict(self):
        dict = {
            'id' : self.id,
            'user_id' : self.user_id,
            'post_id' : self.post_id,
            'body' : self.body,
            'publication_date' : str(self.publication_date)
        }
        return dict

    def __repr__(self):
        return '<Comment {}>'.format(self.user_id, self.post_id, self.body, self.publication_date)

class Subscriber(db.Model):
    __tablename__ = 'subscriber'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    subscriber_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, user_id, subscriber_id):
        self.user_id = user_id
        self.subscriber_id = subscriber_id

    def to_dict(self):
        dict = {
            'id' : self.id,
            'user_id' : self.user_id,
            'subscriber_id' : self.subscriber_id
        }
        return dict

    def __repr__(self):
        return '<User {} has a subscriber {}>'.format(self.user_id, self.subscriber_id)
