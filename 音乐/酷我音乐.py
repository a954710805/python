import re
from bs4 import BeautifulSoup
import requests
import os
# 模拟浏览器
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
}
def get_url(url):
    ret = requests.get(url, headers=headers).text
    a=re.findall("abslist.*'}]}",ret)
    str = "".join(a)
    names = str.split(',')
    for td in names:
        if ("MUSICRID" in td) == True:
            musicid = td.split("'")[3]
            id_url='http://player.kuwo.cn/webmusic/st/getNewMuiseByRid?rid='+musicid
            r = requests.get(id_url, headers=headers)
            r.encoding = 'utf-8'
            soup = BeautifulSoup(r.text, "lxml")
            artists = soup.find_all('artist')
            names = soup.find_all('name')
            for artist,name in zip(artists,names):
                gesou=artist.text
                name=name.text
                print('歌名'+':'+name+'——'+'歌手'+':'+gesou+'   '+'正在下载中...')
                mp3url='https://antiserver.kuwo.cn/anti.s?useless='+'&format=mp3&rid='+musicid+'&response=res&type=convert_url&'
                mp='歌名：'+name+'  '+'歌手：'+gesou
                my_dir = "E:\\歌曲\\" + namess
                # 判断目录是否存在
                if not os.path.exists(my_dir):  # 创建文件夹
                    os.makedirs(my_dir)
                response = requests.get(mp3url)
                down = response.content
                with open(my_dir + "./%s.mp3"%mp, 'wb') as file:
                    file.write(down)

if __name__ == "__main__":
    print('音乐源为酷我音乐，url搜索地址：http://m.kuwo.cn/?key=gohotword&bdfrom=newh5#2，下载的位置为：E:\\歌曲\\')
    print('输入歌曲名下载不同歌手唱这首歌的，输入歌手名字可下载歌手唱的歌曲')
    namess=input('请输入需要下载的歌曲名称或者歌手名称：')
    sl = input('请输入需要下载的歌曲数量：')
    url='http://search.kuwo.cn/r.s?all='+str(namess)+'&ft=music&client=kt&cluster=0&pn=0&rn='+str(sl)+'&rformat=json&callback=searchMusicResult&encoding=utf8&r=1572669234660'.format()
    get_url(url)
    print(sl+'首歌下载完毕，欢迎下次使用')