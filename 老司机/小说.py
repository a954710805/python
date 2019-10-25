
#http://gnr.wodeapi001.xyz/941novel.php?method=novel&novelLink={加上下方解析网站的URL能直接读取}

#http://gnr.wodeapi001.xyz/941novel.php?method=novelList&categoryLink=http://941novel.com/archives/category/【綜合成人文學】/經驗分享系列&page=1

#http://gnr.wodeapi001.xyz/941novel.php?method=novelList&categoryLink=http://941novel.com/archives/category/【綜合成人文學】/其他類別系列&page=1

#http://gnr.wodeapi001.xyz/941novel.php?method=novelList&categoryLink=http://941novel.com/archives/category/【綜合成人文學】/凌辱調教系列&page=1

#http://gnr.wodeapi001.xyz/941novel.php?method=novelList&categoryLink=http://941novel.com/archives/category/【綜合成人文學】/不倫戀曲系列&page=1

#http://gnr.wodeapi001.xyz/941novel.php?method=novelList&categoryLink=http://941novel.com/archives/category/【綜合成人文學】/科幻劇情系列&page=1

#http://gnr.wodeapi001.xyz/941novel.php?method=novelList&categoryLink=http://941novel.com/archives/category/【綜合成人文學】/玄幻武俠系列&page=1

#http://gnr.wodeapi001.xyz/941novel.php?method=novelList&categoryLink=http://941novel.com/archives/category/【綜合成人文學】/人妻熟女系列&page=1

#http://gnr.wodeapi001.xyz/941novel.php?method=novelList&categoryLink=http://941novel.com/archives/category/【綜合成人文學】/日常生活系列&page=1

#http://gnr.wodeapi001.xyz/941novel.php?method=novelList&categoryLink=http://941novel.com/archives/category/【綜合成人文學】/校園師生系列&page=1

import requests
import json
import time

#模拟浏览器
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
          }
#请求url
def get_url(url):           
    r = requests.get(url,headers = header)
    res = r.content.decode()   
    a=res.split("novelLink")  
    for i in a:
       b=i.split(",")[0]
       if('{' in b) == False:
           d=i.split(",")[1]
           name= d.split('"')[3]
           xs_url=b.split('"')[2]
           sss=xs+xs_url 
           print(xs_url)
  #  b = c['novelLink']
  #  print(b)
 #   for i in b:
   #     url =i['trackInfo'][ 'playPath']
    #    name = i['trackInfo']['title']
    #    print(url,name) 
    #    response = requests.get(url)
      #  down = response.content
      #  with open('./%s.m4a'%name,'a') as file:
       #   file.write(down)
          
if __name__ == "__main__":
  url="http://gnr.wodeapi001.xyz/941novel.php?method=novelList&categoryLink=http://941novel.com/archives/category/%E3%80%90%E7%B6%9C%E5%90%88%E6%88%90%E4%BA%BA%E6%96%87%E5%AD%B8%E3%80%91/%E7%B6%93%E9%A9%97%E5%88%86%E4%BA%AB%E7%B3%BB%E5%88%97&page=1"
  urlsss="http://gnr.wodeapi001.xyz/941novel.php?method=novel&novelLink="
                          
get_url(url)
