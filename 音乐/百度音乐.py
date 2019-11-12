import time
from bs4 import BeautifulSoup
import requests
import os
# 模拟浏览器
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
# 'Cookie': 'log_sid=1572661807946CC1E9D96069C9062DCB36D684F307D39; BAIDUID=CC1E9D96069C9062DCB36D684F307D39:FG=1; log_sid=1572661807946CC1E9D96069C9062DCB36D684F307D39; Hm_lvt_d0ad46e4afeacf34cd12de4c9b553aa6=1572661808; tracesrc=-1%7C%7C-1; u_lo=0; u_id=; u_t=; __qianqian_pop_tt=3; Hm_lpvt_d0ad46e4afeacf34cd12de4c9b553aa6=1572664084'
'Cookie': 'BAIDUID=CC1E9D96069C9062DCB36D684F307D39:FG=1; log_sid=1572661807946CC1E9D96069C9062DCB36D684F307D39; tracesrc=-1%7C%7C-1; u_t=; u_id=; __qianqian_pop_tt=3; device_type=1; device_id=v2pcweb-luadnexowy15726643302731; tpl=baidu_music; token_=1820360513161117131A1513111215726643613577ba000b014297fe88ee2536; refresh_token=3b14c99ef55df277a31fa1f821ab654e; Hm_lvt_d0ad46e4afeacf34cd12de4c9b553aa6=1572661808,1572664363; u_login=1; userid=1435187130; Hm_lvt_03ebc396eb9eeb344da124bee12c91fb=1572664367; Hm_lpvt_03ebc396eb9eeb344da124bee12c91fb=1572664367; u_lo=0; Hm_lpvt_d0ad46e4afeacf34cd12de4c9b553aa6=1572664387'
}
def get_url(url):
    r = requests.get(url, headers=header)
    r.encoding = 'utf-8'
    soup = BeautifulSoup(r.text, "lxml")
    content = soup.find_all('span', class_="song-title")
    for td in content:
        zzr = td.find_all('a')
        for td in zzr:
            music_id = td["href"]
            music_name = td.text
            if ('/mv' in music_id) == False:
                print(music_id,music_name)

if __name__ == "__main__":
    url='http://music.taihe.com/top/dayhot'
    get_url(url)