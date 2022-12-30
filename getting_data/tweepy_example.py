import tweepy
import json

consumer_key = 'secret'
consumer_secret = 'secret'
access_token = 'secret'
access_token_secret = 'secret'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()

for tweet in public_tweets:
    print(tweet.text)

my_follower_ids = api.get_follower_ids()

followers_tree = {'followers': []}
for id in my_follower_ids:
    # get the followers of your followers
    try:
        follower_ids = api.get_follower_ids(user_id=id)
    except tweepy.errors.Unauthorized:
        print("Unauthorized to access user %d's followers"
              % (id))

    followers_tree['followers'].append(
        {'id': id, 'follower_ids': follower_ids})


# stream example
class MyStream(tweepy.Stream):
    """ Customized tweet stream """

    def on_data(self, tweet):
        """Do something with the tweet data..."""
        print(tweet)

    def on_error(self, status):
        return True  # keep stream open


stream = MyStream(consumer_key, consumer_secret,
                  access_token, access_token_secret)
# Start the stream with track list of keywords
stream.filter(track=['python', 'javascript', 'dataviz'])
