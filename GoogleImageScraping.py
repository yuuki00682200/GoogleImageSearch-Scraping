#必要なモジュールをインポートする
import requests
import random
import shutil
import bs4
import ssl

#sslの設定
ssl._create_default_https_context = ssl._create_unverified_context

#メイン関数
#image関数 Google画像検索にアクセスする
def image(data):
    Res = requests.get("https://www.google.com/search?hl=jp&q=" + data + "&btnG=Google+Search&tbs=0&safe=off&tbm=isch")
    Html = Res.text
    Soup = bs4.BeautifulSoup(Html, 'xml')
    links = Soup.find_all("img")
    link = random.choice(links).get("src")
    return link

#download_image関数 画像のダウンロード
def download_img(url, file_name):
    r = requests.get(url, stream=True)
    if r.status_code == 200: 
        with open (file_name+ ".png" , 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)

def code():
    code = ""
    for i in range(10):
        code += str(random.choice("getImage"))
    return code

while True: 
    num = input("検索回数: ")
    data = input("検索ワード: ")
    for _ in range(int(num)):
        link = image(data)
        download_img(link, code())
    print("ダウンロード完了")

#一度プログラムを実行したら再度実行するか終了するかy / nで選択する
    while True:
        yn = input("続けますか？ y/n: ")
        if yn == "y":
            break
        elif yn == "n":
            exit()
        else:
            print("yかnを入力してください")
