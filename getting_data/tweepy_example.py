import tweepy

CONSUMER_KEY = 'secret'
CONSUMER_SECRET = 'secret'
ACCESS_TOKEN = 'secret'
ACCESS_TOKEN_SECRET = 'secret'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

public_tweets = api.home_timeline()

for tweet in public_tweets:
    print(tweet.text)

my_follower_ids = api.get_follower_ids()

followers_tree = {'followers': []}
for user_id in my_follower_ids:
    # get the followers of your followers
    try:
        follower_ids = api.get_follower_ids(user_id=user_id)
    except tweepy.errors.Unauthorized:
        print(f"Unauthorized to access user {user_id}'s followers")

    followers_tree['followers'].append(
        {'id': user_id, 'follower_ids': follower_ids})


# stream example
class MyStream(tweepy.Stream):
    """ Customized tweet stream """

    def on_data(self, raw_data):
        """Do something with the tweet data..."""
        print(raw_data)

    def on_error(self):
        return True  # keep stream open


stream = MyStream(CONSUMER_KEY, CONSUMER_SECRET,
                  ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
# Start the stream with track list of keywords
stream.filter(track=['python', 'javascript', 'dataviz'])
