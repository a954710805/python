# coding=utf-8
import requests
import json
import re
import os
import time
# 请求搜索列表数据
search = input("音乐名:")  # 控制台输入搜索关键词
pagesize = "10"  # 请求数目


url = 'https://songsearch.kugou.com/song_search_v2?callback=jQuery11240251602301830425_1548735800928&keyword=%s&page=1&pagesize=%s&userid=-1&clientver=&platform=WebFilter&tag=em&filter=2&iscorrection=1&privilege_filter=0&_=1548735800930' % (search, pagesize)
res = requests.get(url)# 进行get请求

# 需要注意一点，返回的数据并不是真正的json格式，前后有那个多余字符串需要用正则表达式去掉,只要大括号{}包着的内容
# json.loads就是将json数据转为python字典的函数
res = json.loads(re.match(".*?({.*}).*", res.text, re.S).group(1))
list = res['data']['lists']
musicList = []
for item in list:
    song_url='https://wwwapi.kugou.com/yy/index.php?r=play/getdata&callback=jQuery19105229806071431062_1573001974625&hash=%s&album_id=%s&dfid=0i1c1L4TBnDr0XpmJ73nar3A&mid=09ab757595bffe589a8834d99bed464f&platid=4&_=1573001974735'  %(
        item['FileHash'],item['AlbumID'])
    res2 = requests.get(song_url)
    res2 = json.loads(re.match(".*?({.*}).*", res2.text, re.S).group(1))['data']
    dict = {
            '作者': res2['author_name'],
            '歌名': res2['song_name'],
            'id': str(res2['album_id']),
            'type': 'kugou',
            'pic': res2['img'],
            'url': res2['play_url'],
            'lrc': res2['lyrics']
        }
    musicList.append(dict)
    print(dict["作者"],dict["歌名"],"正在下载中")
    my_dir = "E:\\酷狗音乐\\" + search
    # 判断目录是否存在
    mp=dict["歌名"]+' - '+dict["作者"]
    if not os.path.exists(my_dir):  # 创建文件夹
        os.makedirs(my_dir)
    response = requests.get(dict["url"])
    down = response.content
    with open(my_dir + "./%s.mp3" % mp, 'wb') as file:
        file.write(down)


