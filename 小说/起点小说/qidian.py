import requests
from bs4 import BeautifulSoup
from requests.exceptions import *
import random
import json
def random_user_agent():
    list = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/44.0.2403.155 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2226.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.4; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36']
    seed = random.randint(0, len(list) - 1)
    return list[seed]

def neirong():
    search = input("请输入小说的URL:")
    url = search
    headers = {'User-Agent': random_user_agent(),
               'Referer': 'https://book.qidian.com/info/1014104227',
               'Cookie': '_csrfToken=BXnzDKmnJamNAgLu4O3GknYVL2YuNX5EE86tTBAm; newstatisticUUID=1564467217_1193332262; qdrs=0%7C3%7C0%7C0%7C1; showSectionCommentGuide=1; qdgd=1; lrbc=1013637116%7C436231358%7C0%2C1003541158%7C309402995%7C0; rcr=1013637116%2C1003541158; bc=1003541158%2C1013637116; e1=%7B%22pid%22%3A%22qd_P_limitfree%22%2C%22eid%22%3A%22qd_E01%22%2C%22l1%22%3A4%7D; e2=%7B%22pid%22%3A%22qd_P_free%22%2C%22eid%22%3A%22qd_A18%22%2C%22l1%22%3A3%7D'
               }
    try:
        res = requests.get(url=url, params=headers)
        if res.status_code == 200:
            res = requests.get(url)  # 进行get请求
            res = json.loads(res.content)
            xsList = []
            list = res['data']['vs']
            # print(list)
            for item in list:
                a = item['cs']
                for item in a:
                    # 'https://read.qidian.com/chapter/wKJTbRGljRcuwUjttRcGug2/eyG-ndViRwHgn4SMoDUcDQ2'
                    url = 'https://vipreader.qidian.com/chapter/1004150862/%s' % (item['id'])
                    r = requests.get(url, params=headers)
                    r.encoding = 'utf-8'
                    soup = BeautifulSoup(r.text, "lxml")
                    content = soup.find_all('div', class_="read-content j_readContent")
                    zj = soup.find_all('span', class_="content-wrap")
                    for neirong,zjmc in zip(content,zj):
                        section_name = zjmc.text
                        section_text = neirong.text
                        fo = open('1.txt', "ab+")  # 打开小说文件
                        # 以二进制写入章节题目 需要转换为utf-8编码，否则会出现乱码
                        fo.write(('\r' + section_name + '\r\n').encode('UTF-8'))
                        # 以二进制写入章节内容
                        fo.write((section_text).encode('UTF-8'))
                        fo.close()
                        print(section_name+'写入成功')# 关闭小说文件
            return neirong
        else:
            print('No response')
            return None
    except ReadTimeout:
        print("ReadTimeout!")
        return None
    except RequestException:
        print("请求页面出错！")
        return None


if __name__ == '__main__':
    neirong()
