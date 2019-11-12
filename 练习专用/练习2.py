#网易云歌曲直链下载地址#http://music.163.com/song/media/outer/url?id={}.mp3

#此爬虫功能为自动爬取网易云华语男歌手的歌手ID并且写入cvs文件
#-*- coding:utf-8 -*-
import requests
import time
from bs4 import BeautifulSoup
import requests
import csv
import os
# 模拟浏览器
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
}
# 请求url
path = os.getcwd()+"/华语女歌手.csv"   #创建文件
csvfile = open(path, 'a+', encoding='utf-8-sig',newline='')   #创建cvs
writer = csv.writer(csvfile)
writer.writerow(('歌手名字','对应歌手的id'))   #cvs抬头写入的名称

def get_url(url):
    r = requests.get(url, headers=header)
    r.encoding = 'utf-8'
    soup = BeautifulSoup(r.text, "lxml")
    content = soup.find_all('ul', class_="m-cvrlst m-cvrlst-5 f-cb")
    for td in content:
        zzr = td.find_all('a')
        for a in zzr:
            gs_ids = a["href"]
            gs_names = a["title"]
            if ('个人主页' in gs_names) == False:
                gs_name = gs_names.split('的音乐')[0]
            if ('/user' in gs_ids) == False:
                if (' ' in gs_ids) == False:
                    gs_id = gs_ids.split('/artist?id=')[1]
                    print(gs_name, gs_id)
                    writer.writerow((gs_name, gs_id))  #将文本写入csv文件
if __name__ == "__main__":
    # dic = {'华语男歌手': "1001",
    #        '华语女歌手': "1002",
    #        '华语组合/乐队': "1003",
    #        '欧美男歌手': "2001",
    #        '欧美女歌手': "2002",
    #        '欧美组合/乐队': "2003",
    #        }
    dic = input('请需要下载的id：')
    urls = ["https://music.163.com/discover/artist/cat?id="+ str(dic) +"&initial={}".format
            (str(i)) for i in
            range(65, 91)
            ]
    for url in urls:
        get_url(url)
        time.sleep(1)
