# Retweet bot for Twitter, using Python and Tweepy.
# Search query via hashtag or keyword.
# Author: Tyler L. Jones || CyberVox
# Date: Saturday, May 20th - 2017.
# License: MIT License.

import tweepy
from time import sleep
# Import in your Twitter application keys, tokens, and secrets.
# Make sure your keys.py file lives in the same directory as this .py file.
from keys import *
from tweet_analysis import isEnglish, isBot, isPolitical
from keywords import twitter_seach_keywords

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Where q='#example', change #example to whatever hashtag or keyword you want to search.
# Where items(5), change 5 to the amount of retweets you want to tweet.
# Make sure you read Twitter's rules on automation - don't spam!
for search_keyword in twitter_seach_keywords:
    for tweet in tweepy.Cursor(api.search, q=search_keyword, include_entities=True).items(5):
        url = "https://twitter.com/"+tweet.user.screen_name+"/status/"+str(tweet.id)
        isBotVal = isBot(tweet.user.id)
        isEnglishVal = isEnglish(tweet)
        isPoliticalVal = isPolitical(tweet)
        # add reaching more mechanism
        if (not isBotVal) and isEnglishVal and (not isPoliticalVal):
            try:
                print('\nRetweet Bot found tweet by @' +
                      tweet.user.screen_name + '. ' + 'Attempting to retweet.')

                api.update_status("#coronavirus #pandemic #CoronavirusStories #COVID-19 "+url)
                print('Retweet published successfully of:'+url)

                # Where sleep(10), sleep is measured in seconds.
                # Change 10 to amount of seconds you want to have in-between retweets.
                # Read Twitter's rules on automation. Don't spam!
                sleep(10)

            # Some basic error handling. Will print out why retweet failed, into your terminal.
            except tweepy.TweepError as error:
                print('\nError. Retweet not successful. Reason: ')
                print(error.reason)

            except StopIteration:
                break
