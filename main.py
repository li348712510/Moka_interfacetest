# _*_ encoding: utf-8 _*_

import pytest
import datetime


str1 = datetime.datetime.now().strftime('%Y-%m-%d %H_%M_%S')
str2 = "--html=./report/test_report_{}.html".format(str1)

if __name__ == "__main__":
    pytest.main(["-s", "./testcase/sjht_login", str2])