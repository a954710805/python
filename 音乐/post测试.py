# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
#
# import requests
# import json
#
# url = 'https://tool2.cn/Tools/music2/'
# body = {"type": "text", "content": "测试文本", "tag_id": "20717"}
# headers = {'content-type': "application/json", 'Authorization': 'APP appid = 4abf1a,token = 9480295ab2e2eddb8'}
#
# # print type(body)
# # print type(json.dumps(body))
# # 这里有个细节，如果body需要json形式的话，需要做处理
# # 可以是data = json.dumps(body)
# response = requests.post(url, data=json.dumps(body), headers=headers)
# # 也可以直接将data字段换成json字段，2.4.3版本之后支持
# # response  = requests.post(url, json = body, headers = headers)
#
# # 返回信息
# print
# response.text
# # 返回响应头
# print
# response.status_code
namess = input('请输入需要下载的歌曲名称或者歌手名称：')
sl = input('请输入需要下载的歌曲数量：')
url = 'http://search.kuwo.cn/r.s?all=' + str(namess) + '&ft=music&client=kt&cluster=0&pn=0&rn=' + str(
    sl) + '&rformat=json&callback=searchMusicResult&encoding=utf8&r=1572669234660'.format()
print(url)