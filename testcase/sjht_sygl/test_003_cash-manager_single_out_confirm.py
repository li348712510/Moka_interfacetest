from data.sjht_sygl_data import single_out_confirm_data
from data.sjht_sygl_data import cash_manager_confirm_data
import requests
import pytest
import json
from data import com_data
from common import db
import datetime


#  确认出场
class TestOutConfirm:
    def setup_class(self):
        # 入场url
        self.url = cash_manager_confirm_data.url
        # 出场url
        self.url1 = single_out_confirm_data.url
        print(self.url)
        self.header = com_data.header1
        self.user = single_out_confirm_data.user
        self.user1 = {"userId": self.user['userId']}

    def teardown_class(self):
        pass

    # 先入场，再出场
    def test_out_confirm(self):
        print()
        # 入场
        requests.post(url=self.url, headers=self.header, json=self.user)
        # 出场
        r = requests.post(url=self.url1, headers=self.header, json=self.user1)
        # 出场时间校验
        endtime = json.loads(r.text)['data']['payUser']['repayList'][0]['leaveTime']
        sql = "select DATE_FORMAT(end_time, '%Y-%m-%d %H:%i:%s'),order_id,end_time,create_time from  main_order  where uid='{}' order by create_time desc LIMIT 1".format(self.user1['userId'])
        # sql1 = "select end_time from  main_order  where uid='{}' order by create_time desc LIMIT 1".format(self.user1['userId'])
        ordermsg = db.Mysql.select('moka', sql)

        # 校验结束时间是否正确
        assert endtime == ordermsg[0][0]
        # 校验根据最低最高消费 计算用户需支付金额是否正确。
        create_time = ordermsg[0][2]
        end_time = ordermsg[0][3]
        # 用户在门店吸猫时间 instore_time
        if len(create_time.strip()) != 0and len(end_time.strip() != 0):
            instore_time = (endtime-create_time).seconds
            # 获取当前门店最低最高消费

        # 转换成分钟
        instore_time = round(instore_time/60)
        # 消费金额


        # 校验返回信息校验
        assert "成功"in r.text
        assert "waiting_pay"in r.text


if __name__ == '__main__':
    pytest.main(['-s', 'test_003_cash-manager_single_out_confirm.py'])

