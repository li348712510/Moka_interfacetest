# _*_ encoding: utf-8 _*_
from common import get_token
# 商家后台host
sjht_testhost = 'https://catht.yztest.top'
# 小程序host
xcx_testhost = 'https://cat.yztest.top'
# 运营后台host
yyht_testhost = 'http://mkbomstest.yzapi.top'

# 无token
header = {"Accept-Encoding": "gzip",
          "Content-Type": "application/json; charset=UTF-8",
          }
# 商家后台header post
user_data = {"login": "admin", "pwd": "111111"}
# 获取门店1 token
sjht_token = get_token.get_token(url='https://catht.yztest.top/api/login', header=header, json_data=user_data)
header1 = {"Accept-Encoding": "gzip",
           "Content-Type": "application/json; charset=UTF-8",
           "Authorization": sjht_token
           }
# if __name__ == '__main__':
#     print('输出'+get_token.get_token(url='https://catht.yztest.top/api/login', header=header, json_data=user_data))






