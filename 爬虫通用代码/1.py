#-*- coding:utf-8 -*-
import requests
import collections
import re
import urllib.parse
from bs4 import BeautifulSoup
import time
# 模拟浏览器
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
}
# 请求url
url='https://www.696ut.com/yousheng/list-%E8%80%81%E5%B8%88%E4%B8%8E%E5%AD%A6%E7%94%9F.html'
urls='https://mmssxs1.com/有声连载/'
r = requests.get(url, headers=header)
r.encoding='utf-8'
soup = BeautifulSoup(r.text, "lxml")
# print(soup)
content = soup.find_all('div', class_="box list channel list-text-my")
# print(content)
for td in content:
    zzr = td.find_all('li')
    for td in zzr:
        a= td.text
        # print(a)
        name= a.split('10')[1]
        name=b.split('(')[0]
        ys_url=urls+name+'.mp3'
        print(name)
        music = requests.get(ys_url).content
        with open('./%s.mp3'%name,'wb') as file:
            file.write(music)

