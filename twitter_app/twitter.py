from flask import Flask, request
from twitter_app.twitter_data_model import User, Tweet, DB
from twitter_app.twitter_database_functions import upsert_user
import spacy
from twitter_app.predict import get_most_likely_author


def create_app():

    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///twitter_db.sqlite3'
    DB.init_app(app)

    nlp = spacy.load('my_model')

    @app.route('/')
    def landing():
        return 'Welcome to my app'

    @app.route('/add_author')
    def add_author():
        twitter_handle = request.args['twitter_handle']
        new_user = upsert_user(twitter_handle, nlp)
        return '{}\'s tweets added to the database: {}'.format(new_user.name , ', '.join([t.text for t in new_user.tweets]))

    @app.route('/predict_author')
    def predict_author():
        tweet_to_classify = request.args['tweet_to_classify']
        users = [user.name for user in User.query.all()]
        most_likely_author = get_most_likely_author(users, tweet_to_classify, nlp)
        return most_likely_author

    return app
