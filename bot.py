import tweepy, os, random, requests
from time import sleep
from secrets import *

def api_authorize():
    # authorize consumer key/secret
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    # set access to access key/secret
    auth.set_access_token(key, secret)
    # calling the api
    return tweepy.API(auth)

def tweet():
    api = api_authorize()
    # mylist = os.listdir('img')
    mylist = ['ancestors.png','cat-1.jpg','cat-diary-1.jpg','chill.jpg','glyceride.jpg','gyo-1.jpg',
            'remina-1.jpeg', 'tomie-1.jpg', 'tomie-2.jpg','tomie-3.jpeg','tomie-4.jpg', 'uzumaki-1.jpg',
            'uzumaki-2.jpg','uzumaki-3.jpg','uzumaki-4.jpg','uzumaki-5.jpg']
    random_num = random.randrange(0, len(mylist)-1)
    filename = 'temp.jpg'

    url = f'https://raw.githubusercontent.com/mikedinhnguyen/twitter_bot/master/img/{mylist[random_num]}'
    request = requests.get(url, stream=True)

    x = mylist[random_num].split(".")
    message = f'{x[0]}'
    if request.status_code == 200:
        with open(filename, 'wb') as image:
            for chunk in request:
                image.write(chunk)

        api.update_with_media(filename, status=message)
        os.remove(filename)
    else:
        print("Unable to download image")

def main():
    tweet()

if __name__ == "__main__":
    main()

# upload image
# mylist = os.listdir('img')
# random_num = random.randrange(0, len(mylist)-1)
# filename = f"img/{mylist[random_num]}"
# api.update_with_media(filename)

# liking 20 most recent posts
# statuses = api.user_timeline('username_here')
# for status in statuses:
#     api.create_favorite(status.id)