#-*- coding:utf-8 -*-
import requests
import re
import urllib.parse
from bs4 import BeautifulSoup
import time
url='https://www.986tu.com/xiazai/list-%E6%AC%A7%E7%BE%8E%E7%94%B5%E5%BD%B1.html'
header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    }
urls='https://www.986tu.com'
def get_first_url():
    list_href = []
    reaponse = requests.get("https://www.986tu.com/yousheng/list-%E8%AF%B1%E6%83%91%E7%9F%AD%E7%AF%87%E5%B0%8F%E8%AF%B4.html", headers=header)
    soup = BeautifulSoup(reaponse.text, "lxml")
    content = soup.find_all('div', id="tpl-img-content")
    for td in content:
        zzr = td.find_all('a')
        for a in zzr:
            zzr=a["href"]
            list_href.append(urls+zzr)
            out_url = list(set(list_href))
    for reg in out_url:
        print(reg)

get_first_url()