import requests
import json


# 获取后台token
def get_token(url, header, json_data):
    r = requests.post(url=url, headers=header, json=json_data)
    token = json.loads(r.text, strict=False)['data']['Authorization']
    return token
