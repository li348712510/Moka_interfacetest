from common import db
from data import com_data
import random
# 接口地址
api = '/api/cash-manager/single-out-confirm'
url = com_data.sjht_testhost+api

# 生成存在的用户id，且未入场
def get_userid():
	print('进来了')
	id = random.randint(1, 40)
	sql = "select id from jhi_user where id= '{}'".format(id)
	userid = db.Mysql.select('moka', sql)
	# 是否未入场
	sql1 = "select status from service_record where user_id='{}' ".format(id)
	statuslist = db.Mysql.select('moka', sql1)
	status = 'service_finished'
	if len(statuslist) != 0:
		status=statuslist[0][0]
	while len(userid) == 0 or status != 'service_finished':
		id = random.randint(100001, 199999)
		sql = "select id from jhi_user where id= '{}'".format(id)
		userid = db.Mysql.select('moka', sql)
		sql1 = "select status from service_record where user_id='{}' ".format(id)
		statuslist = db.Mysql.select('moka', sql1)
		if len(statuslist) != 0:
			status = statuslist[0][0]
	else:
		return id


user = {"userId": get_userid(), "enterNum": 1}
user1 = {"userId": get_userid()}