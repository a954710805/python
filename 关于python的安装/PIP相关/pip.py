#安装好python的环境后可直接运行
#使用命令python pip.py
"""
python建立pip.ini.py
2016年4月30日 03:35:11 codegay
"""
import os

ini="""[global]
index-url = https://pypi.doubanio.com/simple/
[install]
trusted-host=pypi.doubanio.com
"""
pippath=os.environ["USERPROFILE"]+"\\pip\\"

if not os.path.exists(pippath):
    os.mkdir(pippath)

with open(pippath+"pip.ini","w+") as f:
    f.write(ini)
