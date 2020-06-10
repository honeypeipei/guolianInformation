# -*- coding: utf-8 -*-
# @Time    : 2018/7/24 下午3:33
# @Author  : Grady
# @File    : Session.py

"""
封装获取cookie方法

"""

import requests
import json
import ast

from Common import Log
from Conf import Config


class Session:
    def __init__(self):
        self.config = Config.Config()
        self.log = Log.MyLog()


    def get_session(self, env):
        """
        获取session
        :param env: 环境变量
        :return:
        """

        if env == "debug":
            login_url = 'http://' + self.config.host_debug+self.config.loginHost_debug
            parm = self.config.loginInfo_debug

            #ast.literal_eval 字符串转字典
            headers = ast.literal_eval(self.config.loginheader_debug)
            print (parm)
            print (headers)
            print (login_url)
            session_debug = requests.session()
            response = session_debug.post(login_url, parm, headers=headers)
            self.log.debug('token: %s' % response.json()['token'])
            return response.json()['token']

        # elif env == "release":
        #     login_url = 'http://' + self.config.loginHost_release
        #     parm = self.config.loginInfo_release
        #
        #     session_release = requests.session()
        #     response = session_release.post(login_url, parm, headers=headers)
        #     print(response)
        #     self.log.debug('cookies: %s' % response.cookies.get_dict())
        #     return response.cookies.get_dict()

        else:
            print("get cookies error")
            self.log.error('get cookies error, please checkout!!!')


if __name__ == '__main__':
    ss = Session()
    ss.get_session('debug')