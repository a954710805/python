import requests
from bs4 import BeautifulSoup
#模拟浏览器
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
          }
#请求url
print('笔趣库网站www.biquku.la')
print('例子：小说《飞剑问道》 格式：http://www.biquku.la/0/65/')
urls=input('请输入笔趣库需要下载的小说的url：')
url=urls
r = requests.get(url,headers = header)
r.encoding = 'utf-8'
soup = BeautifulSoup(r.text, "lxml")
content = soup.find_all('div', id="list")
xsmz=soup.find_all('div', id="info")
for xs in xsmz:
    xs= xs.find_all('h1')
    for xs in xs:
     print('准备下载：'+xs.text)
for list in content:
    urls = list.find_all('a')
    for td in urls:
        zj_url=td["href"]
        section_name=td.text
        xsurl=url+zj_url
        res2 = requests.get(xsurl, headers=header)
        res2.encoding = 'utf-8'
        soup = BeautifulSoup(res2.text, "lxml")
        content = soup.find_all('div', id="content")
        mc = soup.find_all('script', language="javascript")
        for nr,mc in zip(content,mc):
         section_text = nr.text
         mc=mc.text
         mc=mc.split(';')[5]
         section_mc = mc.split('"')[1]
         fo = open(section_mc+'.txt', "ab+")  # 打开小说文件
         # 以二进制写入章节题目 需要转换为utf-8编码，否则会出现乱码
         fo.write(('\r' + section_name + '\r\n').encode('UTF-8'))
         # 以二进制写入章节内容
         fo.write((section_text).encode('UTF-8'))
         fo.close()
         print(section_name+'    '+'写入文本成功')  # 关闭小说文件
