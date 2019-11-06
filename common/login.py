# _*_ encoding: utf-8 _*_

import requests
import copy
from data import com_data


class Login:
    header = com_data.heard
    data = com_data.data
    url1 = com_data.url1
    url2 = com_data.url2

    @classmethod
    def login(cls, mobile):

        """获取token"""
        header = copy.deepcopy(cls.header)
        r1 = requests.get(cls.url1)
        token = r1.headers.get('XSRF-TOKEN')
        header['X-XSRF-TOKEN'] = token

        """获取cookie"""
        data = copy.deepcopy(cls.data)
        data['mobile'] = mobile
        r2 = requests.post(url=cls.url2, headers=header, json=data)
        cookie = requests.cookies.RequestsCookieJar()
        cookie.set('access_token', r2.headers.get('access_token'))
        cookie.set('refresh_token', r2.headers.get('refresh_token'))

        return header, cookie
