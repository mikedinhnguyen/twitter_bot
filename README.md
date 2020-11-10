# Small Businesses Twitter Bot  

I used Python library, Tweepy, to authenticate and fetch data to access account, @smallbiznessbot.

Code in bot.py is run through AWS Lambda function.

os.environ arrays are API keys and access token keys, ie, os.environ['consumer_key'], etc. (hidden for obvious reasons)  

I made an AWS EventBridge trigger to have the bot automatically retweet any hashtag in its code every x amount of hours. the default time I made it was 8 hours.
