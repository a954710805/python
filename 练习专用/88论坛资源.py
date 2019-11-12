import time
from bs4 import BeautifulSoup
import requests
import csv
import os
# 模拟浏览器
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
}
path = os.getcwd()+"/2.csv"   #创建文件
csvfile = open(path, 'a+', encoding='utf-8-sig',newline='')   #创建cvs
writer = csv.writer(csvfile)
writer.writerow(('电影下载链接','电影名称'))   #cvs抬头写入的名称
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
              if ('http://www.88yunpan.com/forum.php' in move_url) == False:
                  r = requests.get(move_url, headers=header)
                  r.encoding = 'utf-8'
                  soup = BeautifulSoup(r.text, "lxml")
                  content = soup.find_all('td', class_="t_f")
                  for td in content:
                      zzr = td.find_all('a')
                      for td in zzr:
                          move_url = td["href"]
                          if ('http' in move_url) == False:
                              if ('plugin.php?id' in move_url) == False:
                                mz = td.text
                                print(move_url,mz)
                                writer.writerow((move_url, mz))
if __name__ == "__main__":
    # http://www.xixi16.com/forum.php?mod=forumdisplay&fid=59&typeid=146&typeid=146&filter=typeid&page=1
    urls = ["http://www.88yunpan.com/forum-36-{}.html".format
            (str(i)) for i in
            range(1, 322)
            ]
    for url in urls:
        get_url(url)
        time.sleep(1)