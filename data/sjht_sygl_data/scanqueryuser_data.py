import random
from common import db
from data import com_data

# 接口地址
api = '/api/cash-manager/scan-query-user-noStatusChange'
url = com_data.sjht_testhost+api
#  用户id为空
user = {"userId": ""}
msg = ''
# 用户id不存在


# 生成不存在的用户id
def get_userid():
	id = random.randint(1, 40)
	sql = "select id from jhi_user where id= '{}'".format(id)
	userid = db.Mysql.select('moka', sql)
	while len(userid) == 1:
		id = random.randint(41, 9999)
		sql = "select id from jhi_user where id= '{}'".format(id)
		userid = db.Mysql.select('moka', sql)
	else:
		return id


user1 = {"userId": get_userid()}
msg1 = '用户不存在！'


# 生成存在的用户id，且未入场
def get_userid1():
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
	while len(userid)==0 or status!='service_finished':
		id = random.randint(100001, 199999)
		sql = "select id from jhi_user where id= '{}'".format(id)
		userid = db.Mysql.select('moka', sql)
		sql1 = "select status from service_record where user_id='{}' ".format(id)
		statuslist = db.Mysql.select('moka', sql1)
		if len(statuslist) != 0:
			status = statuslist[0][0]
	else:
		return id


user2 = {"userId": get_userid1()}
msg2 = '成功'



