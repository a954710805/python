import requests
import json
import re
all = input("音乐名:")  # 控制台输入搜索关键词
rn = "1"  # 请求数目
url = 'http://search.kuwo.cn/r.s?all=%s&ft=music&client=kt&cluster=0&pn=0&rn=%s&rformat=json&callback=searchMusicResult&encoding=utf8&r=1572669234660' % (all, rn)
res = requests.get(url)
print(res)