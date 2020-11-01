import tweepy, os, random, requests
from time import sleep
from secrets import *

FILE_NAME = 'last_seen.txt'

def read_last_seen(FILE_NAME):
    file_read = open(FILE_NAME, 'r')
    last_seen_id = int(file_read.read().strip())
    file_read.close()
    return last_seen_id

def store_last_seen(FILE_NAME, last_seen_id):
    file_write = open(FILE_NAME, 'w')
    file_write.write(str(last_seen_id))
    file_write.close()
    return

def api_authorize():
    # authorize consumer key/secret
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    # set access to access key/secret
    auth.set_access_token(key, secret)
    # calling the api
    return tweepy.API(auth)

def send_tweet(api, message, tweet_id): 
    # mylist = os.listdir('img')
    mylist = ['ancestors.png','cat-1.jpg','cat-diary-1.jpg','chill.jpg','glyceride.jpg','gyo-1.jpg',
            'remina-1.jpeg', 'tomie-1.jpg', 'tomie-2.jpg','tomie-3.jpeg','tomie-4.jpg', 'uzumaki-1.jpg',
            'uzumaki-2.jpg','uzumaki-3.jpg','uzumaki-4.jpg','uzumaki-5.jpg']
    random_num = random.randrange(0, len(mylist)-1)
    fileimg = 'temp.jpg'

    # fetch image from github
    url = f'https://raw.githubusercontent.com/mikedinhnguyen/twitter_bot/master/img/{mylist[random_num]}'
    request = requests.get(url, stream=True)

    x = mylist[random_num].split(".")
    message += f' {x[0]}'

    # upload media as tweet
    if request.status_code == 200:
        with open(fileimg, 'wb') as image:
            for chunk in request:
                image.write(chunk)
                
        api.update_with_media(filename=fileimg, status=message, in_reply_to_status_id=tweet_id)
        os.remove(fileimg)
    else:
        print("Unable to download image")

def reply():
    api = api_authorize()
    tweets = api.mentions_timeline(read_last_seen(FILE_NAME), tweet_mode='extended')
    for tweet in reversed(tweets):
        print(str(tweet.id) + ' - ' + tweet.full_text + ' - ' + tweet.user.screen_name)
        api.create_favorite(tweet.id)
        message = '@' + tweet.user.screen_name
        send_tweet(api, message, tweet.id)
        store_last_seen(FILE_NAME,  tweet.id)

def main():
    reply()

if __name__ == "__main__":
    main()

# upload image
# mylist = os.listdir('img')
# random_num = random.randrange(0, len(mylist)-1)
# image = f"img/{mylist[random_num]}"
# api.update_with_media(image)

# liking 20 most recent posts
# statuses = api.user_timeline('username_here')
# for status in statuses:
#     api.create_favorite(status.id)