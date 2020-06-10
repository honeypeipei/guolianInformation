# -*- coding: utf-8 -*-
# @Time    : 2020/04/1 下午2:54
# @Author  : Grady
# @File    : SqlResult.py

import pymysql
from Common import Log
from Conf.Config import Config
import pymysql


class SqlResult:

    def __init__(self, sqlstr,env,*args):
        self.config = Config()
        self.log = Log.MyLog()
        self.sqlstr=sqlstr
        self.args=args
        self.env=env


        # host = self.config.sql_host
        # user = self.config.sql_user
        # password = self.config.sql_password
        # db = self.config.sql_database


    def get_sqlresult(self):


        if self.env == "debug":
            connection = pymysql.connect(host = self.config.sql_host_debug,
                                     user=self.config.sql_user_debug,
                                     password=self.config.sql_password_debug,
                                     db=self.config.sql_database_debug,
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)
        elif self.env == "release":
            connection = pymysql.connect(host = self.config.sql_host_release,
                                     user=self.config.sql_user_release,
                                     password=self.config.sql_password_release,
                                     db=self.config.sql_database_release,
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)

        try:
            with connection.cursor() as cursor:
                # Read a single record
                cursor.execute(self.sqlstr, self.args)
                result = cursor.fetchone()

        finally:
            connection.close()
        return result

    # def execute_sqlresult(self, sqlstr, *args):
    #
    #     try:
    #         connection = pymysql.connect(host=self.config.sql_host,
    #                                      user=self.config.sql_user,
    #                                      password=self.config.sql_password,
    #                                      db=self.config.sql_database,
    #                                      charset='utf8mb4',
    #                                      cursorclass=pymysql.cursors.DictCursor)
    #
    #         with connection.cursor() as cursor:
    #             # Read a single record
    #             cursor.execute(self, sqlstr, *args)
    #             connection.commit()
    #
    #     finally:
    #         connection.close()
