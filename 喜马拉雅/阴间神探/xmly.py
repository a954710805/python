import requests
import json
import time
# 模拟浏览器
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
}
# 请求url
def get_url(url):
    r = requests.get(url, headers=header)
    res = r.content.decode()
    c = json.loads(res)
    b = c['data']['trackDetailInfos']
    for i in b:
        url = i['trackInfo']['playPath']
        name = i['trackInfo']['title']
        print(url, name)
        response = requests.get(url)
        down = response.content
        with open('./%s.mp3' % name, 'wb') as file:
            file.write(down)


if __name__ == "__main__":
    print("请在喜马拉雅找到需要下载的有声小说的id\n下载的小说位置为当前文件夹")
    content = input('请输入需要下载有声小说的id：')
    # https://m.ximalaya.com/m-revision/common/album/queryAlbumTrackRecordsByPage?albumId=19383749&page=1&pageSize=10
    urls = ["https://m.ximalaya.com/m-revision/common/album/queryAlbumTrackRecordsByPage?albumId=" + str(
        content) + "&page={}&pageSize=10".format
            (str(i)) for i in
            range(1, 300)
            ]
    for url in urls:
        get_url(url)
    time.sleep(1)
