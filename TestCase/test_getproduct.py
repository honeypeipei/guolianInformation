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
from Common import Log
import allure


@allure.feature('GetProduct')
class Testgetproduct:

    print('9999999999999999999999999999999999999999')


    @allure.severity('blocker')
    @allure.story('GetProduct')
    def test_getproduct_01(self, action):
        """
            用例描述：测试get1
        """

        with allure.step("浏览商品"):  # 步骤2，step的参数将会打印到测试报告中
            allure.attach('笔记本', '商品1')

        log = Log.MyLog()
        log.info('文件已经开始执行')
        conf = Config()
        data = GetProduct()


        request = Request.Request(action)

        host = conf.host_debug
        port = conf.portShopService_debug
        req_url = 'http://'+host+':'+port
        print(req_url)
        urls = data.url
        params = data.data
        header = data.header
        requestsql = data.requestsql
        responsecode = data.responsecode
        #responsesql = data.responsesql
        #connection=SqlResult.connect_mysql()
        sqlresult = SqlResult(requestsql[0],'debug').get_sqlresult()

        print(sqlresult['id'])

        api_url = req_url+urls[0]
        #print(api_url)
        #print(params[0][0])
        #params[0][0]['categoryId']=7
        #print(header[0])
        response = request.get_request(api_url, params[0][0],header[0])
        assert response['code'] == responsecode[0]


