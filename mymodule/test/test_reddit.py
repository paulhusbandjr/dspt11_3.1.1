from mymodule.reddit import User, Topic


def test_create_user():
    name = 'tests user'
    reputation = 499
    is_moderator = True
    test_user = User(name=name, reputation=reputation, is_moderator=is_moderator)
    assert(type(test_user) == User and
           test_user.name == name and
           test_user.reputation == reputation and
           test_user.is_moderator == is_moderator)


def test_user_upvote_topic(test_user, test_topic):
    up_votes = test_topic.up_votes
    test_user.up_vote(test_topic)
    assert(test_topic.up_votes == up_votes + 1)


def test_user_upvote_comment(test_user, test_comment):
    up_votes = test_comment.up_votes
    test_user.up_vote(test_comment)
    assert(test_comment.up_votes)


def test_create_topic():
    title = 'test_title'
    body = 'test_body'
    user = 'test_user'
    test_topic = Topic(title=title, body=body, user=user)
    assert(type(test_topic) == Topic and
           test_topic.title == title and
           test_topic.body == body and
           test_topic.user == user and
           test_topic.comments[0].body == 'This is my topic'
           )

