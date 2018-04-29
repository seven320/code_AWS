#encoding:utf-8
import tweepy

#親ディレクトリにあるアカウント情報へのパス
import sys,os
import manuscript

#account情報をaccount.pyからロード
from account import account #load account

def AWS_handler(event, context):
    pardir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.append(pardir)

    auth=account.Initialize()
    api = tweepy.API(auth)
    twitter_id=account.id()

    # ツイートのみ
    # api.update_status(status="test by tweepy")#status

    #原稿のロードのためにclass継承　from manuscript.py
    tweet=manuscript.Manuscript()

    # 指定された写真の範囲からランダムに選ぶ
    import random
    min=1
    max=tweet.max_num()#写真と記事の割り振り番号の最大値
    num=random.randint(min,max)
    num_padded='{0:03d}'.format(num)#ゼロパディング:0で３桁左詰する。 example 1→001

    # # #一番から順にツイートする機能
    # # tweetnum=outputtext.Tweet_num()
    # # num=tweetnum.load()#今ツイートする番号を取得
    # # tweetnum.write(num+1)#次のツイート番号を返却
    # # num_padded='{0:03d}'.format(num)


    # 画像付きツイート
    pic="/Users/kenkato/Pictures/forbot/"+str(num_padded)+".jpg" #画像を投稿するなら画像のパス
    status=tweet.manus(num-1)+"\ninstagram.com/ken_4y4"#ツイート内容
    api.update_with_media(filename=pic,status=status)
    print("tweet No:"+str(num))
