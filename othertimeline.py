#encoding:utf-8
import tweepy

#親ディレクトリにあるアカウント情報へのパス
import sys,os


#account情報をaccount.pyからロード
from account import account #load account
def AWS_handler(event, context):
    pardir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.append(pardir)
    auth=account.Initialize()
    api = tweepy.API(auth)
    twitter_id=account.id()

    othertimelines=api.user_timeline("togetter_jp")
    for tweet in othertimelines:
        print(tweet.text)
    return "othertimeline.py works"
