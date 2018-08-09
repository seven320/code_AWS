import urllib.parse
import boto3
from datetime import datetime
import random
import subprocess

print('Loading function')      # ②Functionのロードをログに出力

s3 = boto3.resource('s3')      # ③S3オブジェクトを取得

# ④Lambdaのメイン関数
def lambda_handler(event, context):

    bucket = event['Records'][0]['s3']['bucket']['name']    # ⑤バケット名を取得
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')  # ⑥オブジェクトのキー情報を取得

    # ⑦ローカルのファイル保存先を設定
    file_path = '/tmp/' + key + '_' + datetime.now().strftime('%Y-%m-%d-%H-%M-%S-') + str(random.randint(0,999999))

    try:
        bucket = s3.Bucket(bucket)   # ⑧バケットにアクセス
        bucket.download_file(key, file_path)  # ⑨バケットからファイルをダウンロード
        # ⑩ファイルがダウンロードされているかlsコマンドで確認
        print(subprocess.run(["ls", "-l", "/tmp"], stdout=subprocess.PIPE))
        return
    except Exception as e:
        print(e)
