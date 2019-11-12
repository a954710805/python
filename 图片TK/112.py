import requests

import tkinter as tk
from tkinter import ttk
from bs4 import BeautifulSoup
import bs4
from tkinter import *
from tkinter.filedialog import askdirectory
from lxml import etree
import re

class DB():
    def __init__(self):
        self.window = tk.Tk()  #创建window窗口
        self.window.title("Crawler Pics")  # 定义窗口名称
        # self.window.resizable(0,0)  # 禁止调整窗口大小
        self.menu = ttk.Combobox(self.window,width=6)
        self.path = StringVar()
        self.lab1 = tk.Label(self.window, text = "输入网易云歌单id:")
        self.page = tk.Entry(self.window, width=5)
        self.input = tk.Entry(self.window, textvariable = self.path, width=80)  # 创建一个输入框,显示图片存放路径
        self.info = tk.Text(self.window, height=20)   # 创建一个文本展示框，并设置尺寸
        # 添加一个按钮，用于选择图片保存路径
        # 添加一个按钮，用于触发爬取功能
        self.t_button = tk.Button(self.window, text='爬取', relief=tk.RAISED, width=8, height=1,command=self.download)
        # 添加一个按钮，用于触发清空输出框功能
        self.c_button2 = tk.Button(self.window, text='清空输出', relief=tk.RAISED,width=8, height=1, command=self.cle)
    def gui_arrang(self):
            """完成页面元素布局，设置各部件的位置"""
            self.lab1.grid(row=0, column=0)
            self.input.grid(row=0, column=1)
            self.info.grid(row=3, rowspan=5, column=0, columnspan=3, padx=15, pady=15)
            self.t_button.grid(row=0, column=2, padx=5, pady=5, sticky=tk.W)
            self.c_button2.grid(row=0, column=3, padx=5, pady=5, sticky=tk.W)


    def download(self):
        content = input('请输入需要下载的网易云歌单id：')
        url = 'https://music.163.com/playlist?id={}'.format(content)
        # url = "https://music.163.com/playlist?id=2916282498"
        base_url = 'https://link.hhtjim.com/163/'
        # 模拟浏览器
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
        # 请求url
        res = requests.get(url, headers=header).text
        dom = etree.HTML(res)
        song_id = dom.xpath('//a[contains(@href,"/song?id")]/@href')
        song_names = re.findall('<li><a href=".*?">(.*?)</a></li>', res)
        for music_ids, song_name in zip(song_id, song_names):
            miusc_id = music_ids.split('/song?id=')[-1]
            if ('$' in miusc_id) == False:  # 出现$符号，取反输出
                miusc_url = base_url + miusc_id + '.mp3'
                # 下载歌曲
                music = requests.get(miusc_url).content
            if ('<' in song_name) == False:  # 出现<符号，取反输出
                str = song_name + '--网易云音乐'
                print(song_name)
                # 保存歌曲
                with open('./%s.mp3' % str, 'wb') as file:
                    file.write(music)

    def cle(self):
        """定义一个函数，用于清空输出框的内容"""
        self.info.delete(1.0, "end")  # 从第一行清除到最后一行

def main():
    t = DB()
    t.gui_arrang()
    tk.mainloop()
if __name__ == '__main__':
    main()