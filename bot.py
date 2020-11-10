import json, tweepy, os, time

def api_authorize():
    # authorize consumer key/secret
    auth = tweepy.OAuthHandler(os.environ['consumer_key'], os.environ['consumer_secret'])
    # set access to access key/secret
    auth.set_access_token(os.environ['key'], os.environ['secret'])
    # calling the api
    return tweepy.API(auth)

def send_tweet(): 
    api = api_authorize()
    
    hashtag = '#junjiito #drawing'
    tweets_count = 5
    
    tweets = tweepy.Cursor(api.search, hashtag).items(tweets_count) #since_id=read_last_seen(FILE_NAME)
    
    for tweet in tweets:
        try:
            api.retweet(tweet.id)
            # store_last_seen(FILE_NAME,  tweet.id)
            time.sleep(2)
        except tweepy.TweepError as e:
            print(e.reason)
            time.sleep(2)

def lambda_handler(event, context):
    send_tweet()
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
