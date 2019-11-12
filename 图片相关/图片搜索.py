import time
from bs4 import BeautifulSoup
import requests
import os
# 模拟浏览器
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
}
def get_url(url):
    r = requests.get(url, headers=header)
    r.encoding = 'utf-8'
    soup = BeautifulSoup(r.text, "lxml")
    content = soup.find_all('div', class_="listbox")
    for td in content:
        zzr = td.find_all('a')
        for td in zzr:
            a = td["href"]
            ggg = td["title"]
            iurl = "http:" + a
            r = requests.get(iurl, headers=header)
            r.encoding = 'utf-8'
            soup = BeautifulSoup(r.text, "lxml")
            content = soup.find_all('div', class_="img-box")
            for td in content:
                zzr = td.find_all('img')
                for td in zzr:
                    a = td["src"]
                    if ('http:' in a ) == False:
                        if ('//www' in a) == False:
                            imageurl = "http:" + a
                            names = imageurl.split('/')[4]
                            names = names.split('.jpg')[0]
                            name = ggg + names
                            print(name)
                            # 文件位置
                            my_dir = "F:\\图片\\" + ggg                           # 判断目录是否存在
                            if not os.path.exists(my_dir):                                # 创建文件夹
                                os.makedirs(my_dir)
                            response = requests.get(imageurl)
                            down = response.content
                            with open(my_dir+".\%s.jpg"%names,'wb') as file:
                               file.write(down)
if __name__ == "__main__":
    print("图片保存的位置为F:\\图片\\")
    content =   input('请输入需要下载图片图片名称：')
    # https://m.ximalaya.com/m-revision/common/album/queryAlbumTrackRecordsByPage?albumId=19383749&page=1&pageSize=10
    urls = ["http://www.zdqx.com/index.php?m=search&c=index&a=init&typeid=3&q=" + str(
        content) + "&page={}".format
    (str(i)) for i in
        range(1,20)
            ]
    for url in urls:
        get_url(url)
    time.sleep(1)
