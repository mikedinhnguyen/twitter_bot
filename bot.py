import tweepy
import os
import random
from secrets import *

# authorize consumer key/secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# set access to access key/secret
auth.set_access_token(key, secret)
# calling the api
api = tweepy.API(auth)

# upload image
mylist = os.listdir('img')
random_num = random.randrange(0, len(mylist)-1)
filename = f"img/{mylist[random_num]}"
api.update_with_media(filename)

# update status
# api.update_status('tweet!')