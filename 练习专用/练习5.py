# http://www.xixi16.com/forum.php?mod=forumdisplay&fid=59&typeid=146&typeid=146&filter=typeid&page=1
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
path = os.getcwd()+"\电影.csv"   #创建文件
csvfile = open(path, 'a+', encoding='utf-8-sig',newline='')   #创建cvs
writer = csv.writer(csvfile)
writer.writerow(('歌手名字','对应歌手的id'))   #cvs抬头写入的名称

def get_url(url):
    r = requests.get(url, headers=header)
    r.encoding = 'utf-8'
    soup = BeautifulSoup(r.text, "lxml")
    content = soup.find_all('th', class_="new")
    for td in content:
         zzr = td.find_all('a')
         for td in zzr:
          move_url = td["href"]
          if ('javascript' in move_url) == False:
              if ('http://www.xixi16.com/forum.php?mod=forumdisplay' in move_url) == False:
                      r=requests.get(move_url,headers=header)
                      r.encoding = 'utf-8'
                      soup = BeautifulSoup(r.text, "lxml")
                      content = soup.find_all('div', class_="t_fsz")
                      for td in content:
                          zzr = td.find_all('a')
                          for td in zzr:
                              move_url = td["href"]
                              mz=td.text
                              if ('http' in move_url) == False:
                                  print(move_url,mz)
                                  writer.writerow((move_url, mz))
if __name__ == "__main__":
    # http://www.xixi16.com/forum.php?mod=forumdisplay&fid=59&typeid=146&typeid=146&filter=typeid&page=1
    urls = ["http://www.xixi16.com/forum.php?mod=forumdisplay&fid=59&typeid=146&typeid=146&filter=typeid&page={}".format
            (str(i)) for i in
            range(1, 22)
            ]
    for url in urls:
        get_url(url)
        time.sleep(1)