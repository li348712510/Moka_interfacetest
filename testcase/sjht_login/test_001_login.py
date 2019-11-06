import pytest
import requests
from data.sjht_login_data import login_data
import json
# 商家后台登录、获取token



class TestLogin:
    def setup_class(self):
        self.logindata=login_data
        print('数据准备')

    def teardown_class(self):
        print('结束处理')

    def getresponse_text(self,loginmsg):
        msg = requests.post(url=login_data.url, headers=login_data.header, json=loginmsg).text
        return msg
    # 账号密码为空返回msg'用户名或密码错误'
    @pytest.mark.parametrize('loginMsg, returnMsg', [(login_data.data, login_data.msg), (login_data.data3, login_data.msg3)])
    def test_login1(self, loginMsg, returnMsg):
        msg = self.getresponse_text(loginMsg)
        msg = json.loads(msg)['msg']
        print(msg)
        assert msg != returnMsg
        print('执行参数化')


# 获取token
def get_token(self):
    r = requests.post(url=login_data.url, headers=login_data.header, json=login_data.data3)
    sjht_token = r.json()["data"]["Authorization"]
    print(sjht_token)
    return sjht_token


if __name__ == "__main__":
    pytest.main(['-s', 'test_001_login.py'])
