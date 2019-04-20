import tweepy
from auth_handler import *
import sys

class CustomStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        print(status.text)

def filterTracks(args):
    auth = authenticate()
    stream = tweepy.Stream(auth, CustomStreamListener())
    stream.filter(track=args)
    
if __name__ == "__main__":
    if len(sys.argv) > 1:
        filterTracks(sys.argv[1:])
