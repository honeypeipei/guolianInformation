# -*- coding: utf-8 -*-
# @Time    : 2018/7/30 下午4:14
# @Author  : Grady
# @File    : Teset_Getproduct.py


import allure
import pytest
from  Common.SqlResult import SqlResult

# from Common import Consts
from Common import Request
from Conf.Config import Config
from Params.params import GetProduct


class tet666:


    def getproduct_01():
        """
            用例描述：测试get1
        """
        conf = Config()
        data = GetProduct()

        host = conf.host_debug
        req_url = 'http://'+host
        urls = data.url
        params = data.data
        header = data.header
        requestsql = data.requestsql
        #connection=SqlResult.connect_mysql()

        sqlresult = SqlResult(requestsql[0])
        print(sqlresult.get_sqlresult())
        for x in (sqlresult):
            for j in x:
                print(j, "=>", x[j])
                print(" ")
            print(x)
        print(sqlresult)
        print( params[0][0])
        api_url = req_url+urls[0]
        #response = request.get_request(api_url, params[0][0],header[0])
        #assert response['code'] == responsecode

