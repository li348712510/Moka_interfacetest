from data.sjht_sygl_data import cash_manager_confirm_data
import requests
import pytest
import json
from data import com_data
#  商家扫码—确认入场


class TestEntrance:
    def setup_class(self):
        print('开始1111')
        # 确认入场url
        self.url = cash_manager_confirm_data.url

        print(self.url)
        self.header = com_data.header1

    def teardown_class(self):
        pass

    @pytest.mark.parametrize('user, return_Msg', [(cash_manager_confirm_data.user1, cash_manager_confirm_data.msg1), (cash_manager_confirm_data.user2, cash_manager_confirm_data.msg2)])
    def test_manger_confirm(self, user, return_Msg):
        r = requests.post(url=self.url, headers=self.header, json=user)
        msg = json.loads(r.text, strict=False)['msg']
        print("msg==="+msg)
        assert msg == return_Msg

    def test_01(self):
        print('==========进来')
        # 存在且未入场用户id
        user = cash_manager_confirm_data.user2
        print(user)
        # 用户入场
        requests.post(url=self.url, headers=self.header, json=user)
        # 该用户已入场,再次调用确认入场
        r = requests.post(url=self.url, headers=self.header, json=user)
        msg = json.loads(r.text)['msg']
        assert msg == '服务中或待支付用户不能重新入场！'


if __name__ == '__main__':
    pytest.main(['-s', 'test_002_cash_manager_confirm.py'])


