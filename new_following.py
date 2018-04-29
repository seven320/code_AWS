#encoding:utf-8
#フォローしている人のフォロワーから誰かを探してフォローする

import random
import certifi
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

    count=10#データ取得人数

    # random
    num=random.randint(0,count-1)


    #フォロー先ロード
    following_ids=api.friends_ids(twitter_id,count=10)
    following_date=api.lookup_users(user_ids=following_ids)
    for u in following_date:
        print(u.screen_name)
    print(num)
    #フォロー先のフォロワーを取得
    # followers=t.followers.list(screen_name=following_twitter_id[num],count=count)
    followers=api.followers_ids(id=following_ids[num],count=count)
    followers2=api.lookup_users(user_ids=followers)
    #random
    # print(followers)
    for u in followers2:
        print(u.screen_name)
        # print(u.id)
        # print(u.follow_request_sent)
        # print(u._json["following"])
    #ランダムもう一回
    num1=random.randint(0,count-1)
    print(num1)

    following_id=[]
    following_id.append(followers[num1])
    # print(following_id)
    following_date=api.lookup_users(user_ids=following_id)
    for u in following_date:
        # #follow-part
        if u.follow_request_sent or u._json["following"]:
            print("I already follow "+str(u.screen_name))
        elif u.screen_name==twitter_id:
            print("You can't follow yourself!!")
        else:
            api.create_friendship(u.screen_name)
            print("success!! you followed "+str(u.screen_name)+"!!")
