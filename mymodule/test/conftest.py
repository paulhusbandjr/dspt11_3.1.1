import pytest
from mymodule.reddit import User, Topic, Comment


@pytest.fixture()
def test_user():
    test_user = User(name='test_user', reputation=5000, is_moderator=False)
    return test_user


@pytest.fixture()
def test_topic(test_user):
    test_topic = Topic(title='test_title', body='test_body', user='test_user')
    return test_topic


@pytest.fixture()
def test_comment(test_user):
    test_comment = Comment(topic='test_title', body='test_body', user='test_user')
    return test_comment

