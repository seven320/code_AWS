#encoding:utf-8
import tweepy
#親ディレクトリにあるアカウント情報へのパス
import sys,os
#account情報をaccount.pyからロード
from account import account #load account

def AWS_handler(event, context):
    pardir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.append(pardir)

    #account情報ロード
    auth=account.Initialize()
    api = tweepy.API(auth)
    twitter_id=account.id()

    public_tweets = api.home_timeline()

    for tweet in public_tweets:
        print(tweet.text)
