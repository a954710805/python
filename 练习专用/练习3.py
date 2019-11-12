#网易云歌曲直链下载地址#http://music.163.com/song/media/outer/url?id={}.mp3
#-*- coding:utf-8 -*-
import requests

from bs4 import BeautifulSoup
# 模拟浏览器
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
}
# 请求url
url='https://music.163.com/artist?id=6472'
# urls='https://mmssxs1.com/有声连载/'
r = requests.get(url, headers=header)
r.encoding='utf-8'
soup = BeautifulSoup(r.text, "lxml")
print(soup)
