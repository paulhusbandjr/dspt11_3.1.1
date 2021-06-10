from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()


class User(DB.Model):

    id = DB.Column(DB.BigInteger, primary_key=True, unique=True)
    name = DB.Column(DB.String, nullable=False)


class Thread(DB.Model):

    id = DB.Column(DB.BigInteger, primary_key=True, nullable=False)
    body = DB.Column(DB.VARCHAR(1000), nullable=False)
    author_id = DB.Column(DB.BigInteger, DB.ForeignKey('user.id'))
    author = DB.relationship('User', backref=DB.backref('comment_author', lazy=True))


class Comment(DB.Model):
    id = DB.Column(DB.BigInteger, primary_key=True)
    body = DB.Column(DB.VARCHAR(1000), nullable=False)
    thread_id = DB.Column(DB.BigInteger, DB.ForeignKey('thread.id'), nullable=False)
    thread = DB.relationship('Thread', backref=DB.backref('comment_thread', lazy=True))
