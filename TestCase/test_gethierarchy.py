# -*- coding: utf-8 -*-
# @Time    : 2018/7/30 下午4:14
# @Author  : Grady
# @File    : test_hierarchy.py


import allure
import pytest


from Common.SqlResult import SqlResult

from Common import Consts
from Common import Request
from Common.Session import Session
from Conf.Config import Config
from Params.params import GetHierarchy
from Common import Log
import allure
import json
from Common.Assert import Assertions
import time


@allure.feature('GetHierarchy')
class Testgethierarchy:

    @allure.severity('blocker')
    @allure.story('获取目录')
    def test_hierarchy_01(self, action):
        """
            用例描述：获取目录
        """

        allure.step("获取目录")

        # 写log
        log = Log.MyLog()
        log.info('文件已经开始执行')
        conf = Config()
        data = GetHierarchy()

        with allure.step("写入Log"):
            allure.attach('写入log', '文件已经开始执行')

        request = Request.Request(action)

        # 获取请求域名
        host = conf.host_debug
        req_url = 'http://'+host

        # 获取请求参数
        urls = data.url
        #params = data.data
        header = data.header
        #requestsql = data.selectsql
        env=conf.environment
        responsecode = data.responsecode
        responsesql = data.responsesql
        #casedescription = data.casedec

        #获取token
        token=Session().get_session('debug')
        print(token)
        dict_token={'X-Api-Authorization':token}
        header=dict(header)
        header.update(dict_token)
        print(header)


        # 请求接口
        api_url = req_url+urls
        print(api_url)
        print(header)

        response = request.get_request(api_url,None,header)
        with allure.step("开始请求接口"):
            allure.attach('header', header)
            allure.attach('response', response)
        print(response)

        # 数据库查询结果
        try:
            responsesql=str(responsesql[0]).replace('@sqlresult',str(response['body']['id']))
            responsesqlresult = SqlResult(responsesql,env).get_sqlresult()
            print(responsesqlresult)
            with allure.step("获取预期结果值成功"):
                allure.attach('获取SQL', responsesql)
        except:
            with allure.step("获取预期结果值失败"):
                allure.attach('获取SQL', responsesql)

        print(responsesqlresult['parent_id'])
        # 增加断言
        assertbody = Assertions()
        assertbody.assert_text(str(response['code']), str(responsecode[0]))
        if(response['code'] == responsecode[0]):
            assertbody.assert_body(response['body'], 'id',responsesqlresult['id'])
            assertbody.assert_text(responsesqlresult['name'], params[0][0]['name'])
            assertbody.assert_text(str(responsesqlresult['parent_id']), 'None')
            allure.step("断言完成")
        else:
            with allure.step("执行完成，Code不一致"):
                allure.attach('request', params[0][0])

