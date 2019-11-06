from data import com_data

sjhthost = com_data.sjht_testhost
api = '/api/login'
url = sjhthost+api
header = com_data.header1


# 密码错误
data = {"login": "admin2", "pwd": "123456"}
msg = "用户名或密码错误"
# 账号为空
data1 = {"login": "", "pwd": "123456"}
msg1 = ""
# 密码为空
date2 = {"login": "admin2", "pwd": ""}
# 账号密码正确
data3 = {"login": "admin2", "pwd": "111111"}
msg3 = "成功"






