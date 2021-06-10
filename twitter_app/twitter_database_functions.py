from .twitter_data_model import DB, Tweet, User
import numpy as np
from functools import partial

# function to input a user and tweets
def upsert_user(twitter_handle, nlp, twitter_api):
    try:
        twitter_user = twitter_api.get_user(twitter_handle)
        if User.query.get(twitter_user.id):
            db_user = User.query.get(twitter_user.id)
        else:
            db_user = User(id=twitter_user.id, name=twitter_handle)
            DB.session.add(db_user)

        user_tweet_ids = [tweet.id for tweet in Tweet.query.filter(Tweet.user_id == db_user.id).all()]
        user_tweets_func = partial(twitter_user.timeline, count=200, exclude_replies=True, include_rts=False,
                                   tweet_mode="extended")
        if len(user_tweet_ids) > 0:
            last_tweet_stored_id = np.max()
            user_tweets = user_tweets_func(since_id=last_tweet_stored_id)
        else:
            user_tweets = user_tweets_func()

        for tweet in user_tweets:
            vectorized_tweet = nlp(tweet.full_text).vector
            db_tweet = Tweet(id=tweet.id, text=tweet.full_text, vect=vectorized_tweet)
            db_user.tweets.append(db_tweet)
            DB.session.add(db_tweet)

    except Exception as e:
        raise e
    else:
        DB.session.commit()
    return db_user
