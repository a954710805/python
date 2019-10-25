import requests
import time
from bs4 import BeautifulSoup

# 模拟浏览器
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
}


# 请求url
def get_url(url):
    r = requests.get(url, headers=header)
    r.encoding = 'utf-8'
    soup = BeautifulSoup(r.text, "lxml")
    content = soup.find_all('div', class_="box list channel list-text-my")
    for td in content:
        zzr = td.find_all('li')
        for td in zzr:
            a = td.text
            b = a.split('《')[1]
            name = b.split('》')[0]
            ys_url = urlss + name + '.mp3'
            print(name)
            music = requests.get(ys_url).content
            with open('./%s.mp3' % name, 'wb') as file:
                file.write(music)
if __name__ == "__main__":
    print("一键下载有声小说(诱惑短篇小说)\n下载的小说位置为当前文件夹")
    urlss = 'https://mmssxs1.com/短篇有声小说/201904/'
    # https://m.ximalaya.com/m-revision/common/album/queryAlbumTrackRecordsByPage?albumId=19383749&page=1&pageSize=10
    urls = ["https://www.696ut.com/xiaoshuo/list-%E5%AE%B6%E5%BA%AD%E4%B9%B1%E4%BC%A6-{}.html".format
            (str(i)) for i in
            range(1, 200)
            ]
    for url in urls:
        get_url(url)
    time.sleep(1)
