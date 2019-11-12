import re
import requests
import os
from requests.exceptions import RequestException

case = str(input("请输入你要下载的图片分类："))
category = {
   'DX': 2,
   'XQT': 6,
   'HSW': 7,
   'MTK': 3,
   'YYZ': 4,
   'DZH': 5
}
def get_cid():
    cid = None
    if case == "大胸妹":
        cid = category["DX"]
    elif case == "小翘臀":
        cid = category["XQT"]
    elif case == "黑丝袜":
        cid = category["HSW"]
    elif case == "美腿控":
        cid = category["MTK"]
    elif case == "有颜值":
        cid = category["YYZ"]
    elif case == "大杂烩":
        cid = category["DZH"]
    return cid



base_url = 'https://www.dbmeinv.com/index.htm?'
url = base_url + 'cid=' + str(get_cid())
r = requests.get(url)
# print(r.status_code)
html = r.text
# print(r.text)
# print(html)

name_pattern = re.compile(r'<img class="height_min".*?title="(.*?)"', re.S)
src_pattern = re.compile(r'<img class="height_min".*?src="(.*?.jpg)"', re.S)

name = name_pattern.findall(html)  # 提取title
src = src_pattern.findall(html)  # 提取src
data = [name,src]
# print(name)
# print(src)
d=[]
for i in range(len(name)):
    d.append([name[i], src[i]])

dictdata = dict(d)
# for i in dictdata.items():
#     print(i)

def get_content(url):
    try:
        r = requests.get(url)
        if r.status_code == 200:
            return r.content
        return None
    except RequestException:
        return None

root_dir = os.path.dirname(os.path.abspath('.'))

case_list = ["大胸妹","小翘臀","黑丝袜","美腿控","有颜值","大杂烩"]
for t in case_list:
    if not os.path.exists(root_dir+'/pics'):
        os.makedirs(root_dir+'/pics')
    if not os.path.exists(root_dir+'/pics/'+str(t)):
        os.makedirs(root_dir+'/pics/'+str(t))

def Type(type):
    save_path = root_dir + '/pics/' + str(type)
    # print(save_path)
    for t in dictdata.items():
        try:
            #file_path = '{0}/{1}.{2}'.format(save_path, t[1], 'jpg')
            file_path = save_path + '/' + t[0]+ 'q' +'.jpg'
            print("正在下载: "+'"'+t[0]+'"'+t[1])
            if not os.path.exists(file_path):  # 判断是否存在文件，不存在则爬取
                with open(file_path, 'wb') as f:
                    f.write(get_content(t[1]))
                    f.close()
        except FileNotFoundError:
            continue
if case == "大胸妹":
    Type(case)

elif case == "小翘臀":
    Type(case)

elif case == "黑丝袜":
    Type(case)

elif case == "美腿控":
    Type(case)

elif case == "有颜值":
    Type(case)

elif case == "大杂烩":
    Type(case)