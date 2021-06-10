from lambda_app.reddit_data_model import User, Thread, Comment, DB
from flask import Flask, request
import random


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
DB.init_app(app)


@app.route('/')
def landing():
    user = User()
    user.id = random.randint(0, 999999999)
    user.name = 'paul'
    DB.session.add(user)
    DB.session.commit()
    users = User.query.all()
    return 'hello world, users registered:' + ', '.join([u.name for u in users])


if __name__ == '__main__':
    app.run()
