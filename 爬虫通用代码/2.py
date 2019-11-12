import requests
url="https://mmxzqxl1.com/common/all/201906/om_CFwdmQWT/om_CFwdmQWT.mp4"
music = requests.get(url).content
with open('./1.mp3', 'wb') as file:
    file.write(music)