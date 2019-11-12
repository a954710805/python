import time
from bs4 import BeautifulSoup
import requests
import csv
import os
# 模拟浏览器
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
}
# path = os.getcwd()+"/电影.csv"   #创建文件
# csvfile = open(path, 'a+', encoding='utf-8-sig',newline='')   #创建cvs
# writer = csv.writer(csvfile)
# writer.writerow(('电影下载链接','电影名称'))   #cvs抬头写入的名称
def page_url():
    r = requests.get(url, headers=header)
    r.encoding = 'gbk'
    soup = BeautifulSoup(r.text, "lxml")
    return soup
def get_url(url):
    soup=page_url()
    wjmc=soup.find_all('div', id="main")
    for td in wjmc:
        pm = td.find_all('h1')
        for td in pm:
         mulu = td.text
    content = soup.find_all('div', class_="list")
    for td in content:
        pm=td.find_all('a')
        for td in pm:
            image_url = td["href"]
            image_name=td.text
            if ('http' in image_url) == False:
                image_urls="http://www.netbian.com/"+image_url
                r = requests.get(image_urls, headers=header)
                r.encoding = 'gbk'
                soup = BeautifulSoup(r.text, "lxml")
                content = soup.find_all('div', class_="pic-down")
                for td in content:
                    pm = td.find_all('a')
                    for td in pm:
                        image_url = td["href"]
                        image_url = "http://www.netbian.com/" + image_url
                        r = requests.get(image_url, headers=header)
                        r.encoding = 'gbk'
                        soup = BeautifulSoup(r.text, "lxml")
                        content = soup.find_all('td', align="left")
                        for td in content:
                            pm = td.find_all('a')
                            for td in pm:
                                image_url = td["href"]
                                if ('javascript' in image_url) == False:
                                 print(image_url,image_name)
                                 my_dir = "E:\\图片\\" + mulu
                                # 判断目录是否存在
                                 if not os.path.exists(my_dir): # 创建文件夹
                                     os.makedirs(my_dir)
                                 response = requests.get(image_url)
                                 down = response.content
                                 with open(my_dir + "./%s.jpg"%image_name, 'wb') as file:
                                    file.write(down)


if __name__ == "__main__":
    # http://www.xixi16.com/forum.php?mod=forumdisplay&fid=59&typeid=146&typeid=146&filter=typeid&page=1
    print("下载目录为E:\\图片   直接输入下方分类的英文名称就可以了")
    print("日历:rili	    动漫:dongman	风景:fengjing	美女:meinv ")
    print("游戏:youxi	    影视:yingshi	动态:dongtai	唯美:weimei")
    print("设计:sheji	    可爱:keai	    汽车:qiche   	花卉:huahui")
    print("动物:dongwu	    节日:jieri	    人物:renwu	    美食:meishi")
    print("水果:shuiguo     建筑:jianzhu	体育:tiyu	    军事:junshi")
    print("非主流:feizhuliu                           	     其他:qita ")
    leixing = input('请输入需要下载的类型：')
    urls = ["http://www.netbian.com/"+str(leixing)+"/index_{}.htm".format
            (str(i)) for i in
            range(2, 300)
            ]
    for url in urls:
        get_url(url)
        time.sleep(1)

        # https: // api.zzzmh.cn / bz / getJson
