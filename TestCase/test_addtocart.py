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
from Params.params import AddToCart
from Common import Log
import allure


@allure.feature('AddCart1')
class Testaddtocart:

    print('9999999999999999999999999999999999999999')

    #@pytest.mark.skipif(reason='本次不执行')
    @pytest.fixture(params=[True, False], ids=['param_true', 'param_false'])
    @allure.severity('blocker')
    @allure.story('AddCartstory')
    def test_getproduct_01(self, action):
        """
            用例描述：测试get1
        """

        with allure.step("用例开始"):  # 步骤2，step的参数将会打印到测试报告中
            allure.attach('test2','开始测试'),

        log = Log.MyLog()
        log.info('文件已经开始执行')
        conf = Config()
        data = AddToCart()
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
        with allure.step('请求参数：' ):  # 步骤2，step的参数将会打印到测试报告中
            allure.attach(str(urls[0]),'请求url')
            allure.attach(str(params[0][0]),'请求参数：')
            allure.attach(str(urls[0]),'请求heder：')

        sqlresult = SqlResult(requestsql[0],'debug').get_sqlresult()


        print(sqlresult['id'])

        api_url = req_url+urls[0]
        #print(api_url)
        print(params[0][0])
        params[0][0]['memberId']=7
        print(params[0][0])
        #print(header[0])
        response = request.post_request(api_url, params[0][0],header[0])
        with allure.step('执行测试完成：' ):  # 步骤2，step的参数将会打印到测试报告中
            allure.attach(str(response['code']),'请求结果')
            allure.attach(str(response['body']), '请求结果体')
        assert response['code'] == responsecode[0]


