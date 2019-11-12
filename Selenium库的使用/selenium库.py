from selenium import webdriver#导入模块

import time

browser = webdriver.Chrome()  #使用谷歌
browser.get("https://music.163.com/#/artist?id=6472")  #模拟访问
time.sleep(1)
goup=browser.page_source   #打印源代码
browser.close()
print(goup)