from auth_handler import *
import tweepy
def create_api():
    return tweepy.API(authenticate())

def get_home_timeline_tweets(api):
    tweets = api.home_timeline()
    for tweet in tweets:
        print(tweet.text)

def get_user_details(api, user_name):
    user = api.get_user(user_name)
    details = {}
    details["screen_name"] = user.screen_name
    details["followers_count"] = user.followers_count
    return details

if __name__ == "__main__":
    api = create_api()
    get_home_timeline_tweets(api)
    print(get_user_details(api, "LeeGunner82"))
