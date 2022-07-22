import time
from pprint import pprint
import os
from attr import dataclass
import requests
import json
import yaml

data_demo = {
    "mobile": "17740194052",
    "password": "123456",
    "authCode": "",
    "captcha": "2usw",
    "captchaUUID": "abae3b68-f7c1-4469-bade-0f6bb25f612b"
}
header_old = {
    "Accept": "application/json; charset=utf-8",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,yo;q=0.8",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJVaWQiOjQwNjcsIlNVaWQiOi0xLCJNb2JpbGUiOiIxNzc0MDE5NDA1MiIsIlJlYWxOYW1lIjoi5byg5LiJIiwiRU5hbWUiOiLkvJhFK - iuouWNleWvueaOpeiwg - ivlSIsIkVJRCI6MjAxMzYxLCJFc2Nyb3dOYW1lIjoiIiwiRXNjcm93TW9iaWxlIjoiIiwiaWF0IjoxNjU4Mzk2NDExLCJuYmYiOjE2NTgzOTY0MTEsImV4cCI6MTY1ODQwNzIxMSwiaXNzIjoiU2VydmVyIiwiYXVkIjoiQ2xpZW50In0.GnHCqJxY4RYGQZnUwds7mxkzsPGxoPK3on_BMNtjuXs",
    "Cache - Control": "no - cache",
    "Content - Length": "128",
    "Content - Type": "application/json",
    "Cookie": "Hm_lvt_5051f16aef626d4043437332e22fa100 = 1658123391, 1658210851, 1658280022, 1658364784;Hm_lpvt_5051f16aef626d4043437332e22fa100 = 1658395740",
    "Host": "192.168.1.50",
    "listNeedRightNowSearch": "false",
    "Origin": "http://192.168.1.50",
    "Pragma": "no-cache",
    "Referer": "http://192.168.1.50",
    "User - Agent": "Mozilla/5.0(WindowsNT10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 95.0.4638.69Safari / 537.36",
    "X - Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmIjoiZXlKaGJHY2lPaUpJVXpJMU5pSXNJblI1Y0NJNklrcFhWQ0o5IiwiZSI6IkduSENxSnhZNFJZR1FablV3ZHM3bXhrenNQR3hvUEszb25fQk1OdGp1WHMiLCJzIjozNCwibCI6NywiayI6IkpwYkdVaU8iLCJpYXQiOjE2NTgzOTY0MTEsIm5iZiI6MTY1ODM5NjQxMSwiZXhwIjoxNjU4NDE0NDExLCJpc3MiOiJTZXJ2ZXIiLCJhdWQiOiJDbGllbnQifQ.jx9ihcJjYzvzaTD5cqzv - CC9VZD1qQfIjUZqSKCIkGU"

}
header_demo = {
    "Accept": "text/plain",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJVaWQiOjQwNjcsIlNVaWQiOi0xLCJNb2JpbGUiOiIxNzc0MDE5NDA1MiIsIlJlYWxOYW1lIjoi5byg5LiJIiwiRU5hbWUiOiLkvJhFK - iuouWNleWvueaOpeiwg - ivlSIsIkVJRCI6MjAxMzYxLCJFc2Nyb3dOYW1lIjoiIiwiRXNjcm93TW9iaWxlIjoiIiwiaWF0IjoxNjU4Mzk2NDExLCJuYmYiOjE2NTgzOTY0MTEsImV4cCI6MTY1ODQwNzIxMSwiaXNzIjoiU2VydmVyIiwiYXVkIjoiQ2xpZW50In0.GnHCqJxY4RYGQZnUwds7mxkzsPGxoPK3on_BMNtjuXs",
    "Content - Type": "application/json",
    "Cookie": "Hm_lvt_5051f16aef626d4043437332e22fa100 = 1658123391, 1658210851, 1658280022, 1658364784;Hm_lpvt_5051f16aef626d4043437332e22fa100 = 1658395740",
    "X - Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmIjoiZXlKaGJHY2lPaUpJVXpJMU5pSXNJblI1Y0NJNklrcFhWQ0o5IiwiZSI6IkduSENxSnhZNFJZR1FablV3ZHM3bXhrenNQR3hvUEszb25fQk1OdGp1WHMiLCJzIjozNCwibCI6NywiayI6IkpwYkdVaU8iLCJpYXQiOjE2NTgzOTY0MTEsIm5iZiI6MTY1ODM5NjQxMSwiZXhwIjoxNjU4NDE0NDExLCJpc3MiOiJTZXJ2ZXIiLCJhdWQiOiJDbGllbnQifQ.jx9ihcJjYzvzaTD5cqzv - CC9VZD1qQfIjUZqSKCIkGU"

}
url_demo = 'http://192.168.1.50/api/OrderList/GetOrderList'


def Login(url, data, header):
    login = requests.post(url, json=data, headers=header, )
    return login


def GetTime():
    # time_format = time.strftime("%Y-%m-%d%H:%M:%S", time.localtime())
    time_format = time.strftime("%Y-%m-%H%M%S", time.localtime())
    return time_format


def write_file(url, datas, headers):
    login = Login(url, data=datas, header=headers)
    nt = GetTime()
    # with open(f'json{nt}.txt', mode='w', encoding='utf8') as f:
    #     load_data = json.load(login.json())
    #     f.write(str(load_data))
    print()
    with open(f'text{nt}.json', mode='w', encoding='utf8') as w:
        w.write(login.text)
    print()


# pprint(r.json())
# pprint(r.text)
if __name__ == '__main__':
    res = write_file(url_demo, datas=data_demo, headers=header_demo)
