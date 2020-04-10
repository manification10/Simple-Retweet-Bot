from keys import *
import botometer
import numpy as np



# setup
rapidapi_key = botometer_rapid_api_key # now it's called rapidapi key
twitter_app_auth = {
    'consumer_key': consumer_key,
    'consumer_secret': consumer_secret,
    'access_token': access_token,
    'access_token_secret': access_token_secret,
  }
bom = botometer.Botometer(wait_on_ratelimit=True,
                          rapidapi_key=rapidapi_key,
                          **twitter_app_auth)


def isBot(userid):
    result = bom.check_account(userid)
    display_scores = result["display_scores"])
    display_scores_mean = np.array(list(display_scores.values())).mean()
    if display_scores_mean >= 4.0:
        return True
    return False

def checkUserVerified(tweet):
    return tweet.user.verified

isBot('TidePod89577871')
