
import tweepy
from src import Secret, System

class Twitter:
    def __init__(self):
        s = System.System("credentials")
        c = Secret.Crypt()
        consumer_key = c.decrypt(s.ENV["consumer_key"])
        consumer_secret = c.decrypt(s.ENV["consumer_secret"])
        access_token = c.decrypt(s.ENV["access_token"])
        access_token_secret = c.decrypt(s.ENV["access_token_secret"])
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth,wait_on_rate_limit=True)

    def getHashTag(self, hashTag):
        tweetList = []
        for tweet in tweepy.Cursor(self.api.search,q=hashTag).items(100):
            tweetList.append({"hashtag": hashTag, 
                "user": tweet.user.screen_name, 
                "followers": tweet.user.followers_count,
                "date": str(tweet.created_at),
                "language": tweet.lang,
                "country": tweet.user.location})
        return tweetList


