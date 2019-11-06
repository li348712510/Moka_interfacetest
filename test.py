import datetime
from common import db, assertion_method

#now = datetime.date.today()
#print(now.strftime('%Y-%m-%d'))

#y = now + datetime.timedelta(days=-3)
#print(y.strftime('%Y-%m-%d'))

str1 = "123aa"
print(str1.replace('aa', '33'))
print(str1)

dic1 = {'a': 1}
dic2 = {'b': 2}
dic1.update(dic2)
print(dic1)