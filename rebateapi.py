import requests
import time
import json


datas = {
    "secretKey": "B5599595-21CB-0C45-D491-04EA48DC235D",
    "data": [
        {
            "uniqueCode": "weg4w4g",
            "pwNumber": "B5599595",
            "serialNumberTime": "2022-2-3 15:40:00",
            "supplierNameId": "123456",
            "details": [
                {
                    "uniqueCode": "w4egfwg",
                    "pwNumber": "12w5feg5",
                    "psn": "1243545",
                    "quantityReal": 152,
                    "price": 12.3623,
                    "priceTaxi": 13.698,
                    "drugsBase_DrugName": "阿莫西林",
                    "drugsBase_Specification": "1mg*200粒",
                    "drugsBase_Manufacturer": "阿莫西林厂",
                    "approvalNumber": "国药准字156464"
                }
            ]
        }
    ]
}

header ={
    'Accept': 'text/plain',
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJVaWQiOjQwNjcsIlNVaWQiOi0xLCJNb2JpbGUiOiIxNzc0MDE5NDA1MiIsIlJlYWxOYW1lIjoi5byg5LiJIiwiRU5hbWUiOiLkvJhFK - iuouWNleWvueaOpeiwg - ivlSIsIkVJRCI6MjAxMzYxLCJFc2Nyb3dOYW1lIjoiIiwiRXNjcm93TW9iaWxlIjoiIiwiaWF0IjoxNjU4Mzk2NDExLCJuYmYiOjE2NTgzOTY0MTEsImV4cCI6MTY1ODQwNzIxMSwiaXNzIjoiU2VydmVyIiwiYXVkIjoiQ2xpZW50In0.GnHCqJxY4RYGQZnUwds7mxkzsPGxoPK3on_BMNtjuXs',
    'Content-Type': 'application/json',
    'Cookie':  'Hm_lvt_5051f16aef626d4043437332e22fa100 = 1658123391, 1658210851, 1658280022, 1658364784;Hm_lpvt_5051f16aef626d4043437332e22fa100 = 1658395740',
    'X-Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmIjoiZXlKaGJHY2lPaUpJVXpJMU5pSXNJblI1Y0NJNklrcFhWQ0o5IiwiZSI6IkduSENxSnhZNFJZR1FablV3ZHM3bXhrenNQR3hvUEszb25fQk1OdGp1WHMiLCJzIjozNCwibCI6NywiayI6IkpwYkdVaU8iLCJpYXQiOjE2NTgzOTY0MTEsIm5iZiI6MTY1ODM5NjQxMSwiZXhwIjoxNjU4NDE0NDExLCJpc3MiOiJTZXJ2ZXIiLCJhdWQiOiJDbGllbnQifQ.jx9ihcJjYzvzaTD5cqzv - CC9VZD1qQfIjUZqSKCIkGU'
}

r = requests.post(
    'http://192.168.1.12:9999/Api/RebateAgreement/RebatePurcWarehousing', datas, header)

print(r.json)
