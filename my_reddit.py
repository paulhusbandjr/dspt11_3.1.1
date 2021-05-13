from mymodule.reddit import User, Comment


ryan = User(name="ryan", reputation=5000, is_moderator=False)
windsurfing_topic = ryan.post_topic(title="windsurfing is cool", body="who wants to go windsurfing?")
troll_comment = ryan.post_comment(topic=windsurfing_topic, body="windsurfing is lame")
nice_comment = Comment(topic=windsurfing_topic, body="windsurfing is the best", down_votes=50, user=ryan)

print(nice_comment.up_votes)

ryan.up_vote(nice_comment)
ryan.up_vote(windsurfing_topic)
susan = User(name="susan", reputation=5000, is_moderator=False)
go_windsurfing_comment = susan.post_comment(topic=windsurfing_topic, body="wanna go windsurfing?")
ryan.up_vote(go_windsurfing_comment)

print(nice_comment.up_votes)