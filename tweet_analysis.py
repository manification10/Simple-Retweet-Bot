from keys import *
import botometer
import numpy as np
from keywords import political_words


# setup
rapidapi_key = botometer_rapid_api_key  # now it's called rapidapi key
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
    display_scores = result["display_scores"]
    display_scores_mean = np.array(list(display_scores.values())).mean()
    if display_scores_mean >= 4.0:
        print("Propbably a bot.")
        return True
    return False


def isEnglish(tweet):
    if tweet.lang == 'en':
        return True
    return False


def checkUserVerified(tweet):
    return tweet.user.verified

def isPolitical(tweet):
    text = tweet.text
    if any(val in text for val in political_words):
        print("Political text")
        return True
    return False
