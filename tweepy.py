#pip install tweepy
import tweepy

consumer_key = ""
consumer_secret = ""

access_token = ""
access_token_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#All request windows are 15 minutes in length.
#API Version 1.1 Rate limits
#https://developer.twitter.com/en/docs/twitter-api/v1/rate-limits
api.wait_on_rate_limit = True

#http://docs.tweepy.org/en/latest/api.html?highlight=friendship#friendship-methods

#follow 400 users per day
#api.create_friendship(id/screen_name/user_id)

#output each follow to a spreadsheet
#note time followed
#like most recent tweet
#wait 24 hrs
#view status of friendship....

#unfollow if they have not followed back in 24 hours
#api.destroy_friendship(id/screen_name/user_id)
#review how many are following back?
