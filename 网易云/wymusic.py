#下载网易云歌单的python程序
import  requests
from lxml import etree
import re
content =   input('请输入需要下载的网易云歌单id：')
url ='https://music.163.com/playlist?id={}'.format(content)
# url = "https://music.163.com/playlist?id=2916282498"
base_url = 'https://link.hhtjim.com/163/'
#模拟浏览器
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
#请求url
res = requests.get(url,headers = header).text
dom =etree.HTML(res)
song_id =dom.xpath('//a[contains(@href,"/song?id")]/@href')
song_names= re.findall('<li><a href=".*?">(.*?)</a></li>',res)
for music_ids,song_name in zip(song_id,song_names):
    miusc_id = music_ids.split('/song?id=')[-1]
    if ('$' in miusc_id) == False: #出现$符号，取反输出
        miusc_url = base_url + miusc_id +  '.mp3'
        #下载歌曲
        music = requests.get(miusc_url).content
    if ('<' in song_name) == False:   #出现<符号，取反输出
        str = song_name  + '--网易云音乐'
        print(song_name)
        #保存歌曲
        with open('./%s.mp3'%str,'wb') as file:
            file.write(music)
