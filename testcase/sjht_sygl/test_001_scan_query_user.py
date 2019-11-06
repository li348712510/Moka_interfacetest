from data.sjht_sygl_data import scanqueryuser_data
import requests
import pytest
import json
from data import com_data
#  商家扫码


class TestSjsm:
    def setup_class(self):
        self.url = scanqueryuser_data.url
        print(self.url)
        self.header = com_data.header1

    def teardown_class(self):
        pass

    @pytest.mark.parametrize('user, return_Msg', [(scanqueryuser_data.user1, scanqueryuser_data.msg1), (scanqueryuser_data.user2, scanqueryuser_data.msg2)])
    def test_smrc(self, user, return_Msg):
        r = requests.post(url=self.url, headers=self.header, json=user)
        print(user)
        msg = json.loads(r.text, strict=False)['msg']
        print("msg==="+msg)
        assert msg == return_Msg


if __name__ == '__main__':
    pytest.main(['-s', 'test_001_scan_query_user.py'])

