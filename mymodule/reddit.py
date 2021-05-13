class Post:
    def __init__(self, up_votes, down_votes, user, body):
        self.up_votes = up_votes
        self.down_votes = down_votes
        self.user = user
        self.body = body


class User:
    def __init__(self, name, reputation, is_moderator):
        self.reputation = reputation
        self.name = name
        self.is_moderator = is_moderator
        self.topics = []
        self.comments = []

    def post_topic(self, title, body):
        topic = Topic(title=title, body=body, user=self)
        self.topics.append(topic)
        return topic

    def post_comment(self, topic, body):
        comment = Comment(topic=topic, body=body, user=self)
        self.comments.append(comment)
        return comment

    def up_vote(self, post: Post):
        post.up_votes += 1


class Topic(Post):
    def __init__(self, title, user, body, up_votes=0, down_votes=0):
        self.title = title
        self.comments = []
        self.comments.append(Comment(body='This is my topic', user=user, topic=self))
        super(Topic, self).__init__(up_votes=up_votes, down_votes=down_votes, user=user, body=body)


class Comment(Post):
    def __init__(self, topic, body, user, up_votes=0, down_votes=0):
        self.topic = topic
        super(Comment, self).__init__(up_votes=up_votes, down_votes=down_votes, user=user, body=body)

