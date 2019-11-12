import time
from bs4 import BeautifulSoup
import requests
import csv
import os
# 模拟浏览器
header = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'User-Agent':  'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
    'cookie' : '__cfduid=dec36529f6a72646c2f23eb0459f5aaef1572428194; _ga=GA1.2.273512530.1572428194; _gid=GA1.2.243098338.1572428194; Hm_lvt_7fdb595155952c7ea57e38e9bbafc6e8=1572428198,1572428249; Hm_lvt_1d5f02d5df48c64bf8536f393e6fc114=1572428198,1572428249; _gat_gtag_UA_126205200_1=1; _gat_gtag_UA_146776794_4=1; _gat_gtag_UA_146776794_2=1; Hm_lpvt_7fdb595155952c7ea57e38e9bbafc6e8=1572428608; Hm_lpvt_1d5f02d5df48c64bf8536f393e6fc114=1572428608; playss=7'
}
path = os.getcwd()+"/2.csv"   #创建文件
csvfile = open(path, 'a+', encoding='utf-8-sig',newline='')   #创建cvs
writer = csv.writer(csvfile)
writer.writerow(('电影下载链接','电影名称'))   #cvs抬头写入的名称
def get_url(url):
    r = requests.get(url ,headers=header)
    r.encoding = 'utf-8'
    soup = BeautifulSoup(r.text, "lxml")
    content = soup.find_all('div', id="tpl-img-content")
    for td in content:
        zzr = td.find_all('a')
        for td in zzr:
            move_urls = td["href"]
            name = td["title"]
            move_url='https://www.687yt.com'+move_urls
            print(move_url)
            r = requests.get(move_url, headers=header)
            r.encoding = 'utf-8'
            soup = BeautifulSoup(r.text, "lxml")
            content = soup.find_all('td', align="right")
            for td in content:
                zzr = td.find_all('a')
                for td in zzr:
                    move_url = td["href"]
                    if ('thunder:' in move_url) == False:
                        print(move_url,name)
                        writer.writerow((move_url, name))
if __name__ == "__main__":
    urls = ["https://www.966ut.com/xiazai/list-欧美电影-{}.html".format
            (str(i)) for i in
            range(1, 200)
            ]
    for url in urls:
        get_url(url)
    time.sleep(1)