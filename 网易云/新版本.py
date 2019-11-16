from bs4 import BeautifulSoup
import requests
import os
print('下载地址为E:\\网易云歌曲')
content =   input('请输入需要下载的网易云歌单id：')
url ='https://music.163.com/playlist?id={}'.format(content)
#模拟浏览器
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
#请求url
res = requests.get(url,headers = header)
r = requests.get(url, headers=header)
soup = BeautifulSoup(r.text, "lxml")
gd_name=soup.find_all('meta', property="og:title")
hide=soup.find_all('ul', class_="f-hide")
for td,gd_name in zip(hide,gd_name):
    pm = td.find_all('a')
    gd_name=gd_name['content']
    for zzr in pm:
      song_id=zzr['href']
      song_name = zzr.text
      song_id=song_id.split('=')[1]
      # print(song_id,song_name)
      my_dir = "E:\\网易云歌曲\\" + gd_name
      # 判断目录是否存在
      if not os.path.exists(my_dir):  # 创建文件夹
          os.makedirs(my_dir)
      image_url='https://link.hhtjim.com/163/'+song_id+'.mp3'
      response = requests.get(image_url)
      down = response.content
      with open(my_dir + "./%s.mp3" %song_name, 'wb') as file:
          file.write(down)
          print(song_name+'下载成功')
