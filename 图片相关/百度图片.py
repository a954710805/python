#导入模块
import requests
import re
import os
#1.获取URL

star  =   input('输入想要下载的图片：')
url  =  f'https://image.baidu.com/search/flip?tn=baiduimage&word={star}'
#2.请求
res = requests.get(url).text
#3删选
image_urls  = re.findall('"objURL":"(.*?)",',res) #删选得到图片URL
for image_url in image_urls:
    image_name   =  image_url.split('/')[-1]   #将获取的URLS使用/分割
    image_end  =  re.search('(.jpg|.bmp|.png|.tif|.gif)$',image_name)   #删选得到图片名字
    if image_end == None:   #图片结尾无以.JPG  .BMP  .PNG结尾的
        print(image_name)
#3.下载图片
    image = requests.get(image_url).content
    str = star  + image_name

#4.保存图片
    with open('./%s.jpg'%str,'wb') as f:
      f.write(image)
