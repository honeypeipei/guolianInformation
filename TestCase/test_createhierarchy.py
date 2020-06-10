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
from Params.params import CreateHierarchy
from Common import Log
import allure
import json
from Common.Assert import Assertions
import time


@allure.feature('CreateHierarchy')
class Testcreatehierarchy:

    @allure.severity('blocker')
    @allure.story('创建一级目录')
    def test_hierarchy_01(self, action):
        """
            用例描述：测试创建一级目录
        """

        allure.step("开始创建一级目录")

        # 写log
        log = Log.MyLog()
        log.info('文件已经开始执行')
        conf = Config()
        data = CreateHierarchy()

        with allure.step("写入Log"):
            allure.attach('写入log', '文件已经开始执行')

        request = Request.Request(action)

        # 获取请求域名
        host = conf.host_debug
        req_url = 'http://'+host

        # 获取请求参数
        urls = data.url
        params = data.data
        header = data.header
        requestsql = data.selectsql
        env=conf.environment
        responsecode = data.responsecode
        responsesql = data.responsesql
        casedescription = data.casedec

        #获取token
        token=Session().get_session('debug')
        print(token)
        dict_token={'X-Api-Authorization':token}
        header=dict(header[0])
        header.update(dict_token)
        print(header)


        #参数化请求参数
        try:
            params[0][0]['name']='公司'+str(int(time.time()))
        except:
            with allure.step("获取输入参数值"):
                allure.attach('参数化', params[0][0]['name'])

        # 请求接口
        api_url = req_url+urls[0]
        print(api_url)
        print(params[0][0])
        print(header)

        response = request.post_request(api_url, json.dumps(params[0][0]),header)
        with allure.step("开始请求接口"):
            allure.attach('request', params[0][0])
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

    @allure.severity('blocker')
    @allure.story('创建二级目录')
    def test_hierarchy_02(self, action):
        """
            用例描述：测试创建二级目录
        """

        allure.step("开始创建二级目录")

        # 写log
        log = Log.MyLog()
        log.info('文件已经开始执行')
        conf = Config()
        data = CreateHierarchy()

        with allure.step("写入Log"):
            allure.attach('写入log', '文件已经开始执行')

        request = Request.Request(action)

        # 获取请求域名
        host = conf.host_debug
        req_url = 'http://'+host

        # 获取请求参数
        urls = data.url
        params = data.data
        header = data.header
        requestsql = data.selectsql
        env=conf.environment
        responsecode = data.responsecode
        responsesql = data.responsesql
        casedescription = data.casedec

        #获取token
        token=Session().get_session('debug')
        print(token)
        dict_token={'X-Api-Authorization':token}
        header=dict(header[1])
        header.update(dict_token)
        print(header)


        #参数化请求参数
        try:
            sqlresult = SqlResult(requestsql[1], env).get_sqlresult()
            params[1][0]['name']='部门'+str(int(time.time()))
            params[1][0]['parent_id'] = sqlresult['id']
        except:
            with allure.step("获取输入参数值"):
                allure.attach('参数化', params[1][0]['name'])

        # 请求接口
        api_url = req_url+urls[1]
        print(api_url)
        print(params[1][0])
        print(header)

        response = request.post_request(api_url, json.dumps(params[1][0]),header)
        with allure.step("开始请求接口"):
            allure.attach('request', params[1][0])
            allure.attach('header', header)
            allure.attach('response', response)
        print(response)

        # 数据库查询结果
        try:
            responsesql=str(responsesql[1]).replace('@sqlresult',str(response['body']['id']))
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
        assertbody.assert_text(str(response['code']), str(responsecode[1]))
        if(response['code'] == responsecode[1]):
            assertbody.assert_body(response['body'], 'id',responsesqlresult['id'])
            assertbody.assert_text(responsesqlresult['name'], params[1][0]['name'])
            assertbody.assert_text(str(responsesqlresult['parent_id']), str(sqlresult['id']))
            allure.step("断言完成")
        else:
            with allure.step("执行完成，Code不一致"):
                allure.attach('request', params[1][0])

    @allure.severity('normal')
    @allure.story('Name超长')
    def test_hierarchy_03(self, action):
        """
            用例描述：测试创建二级目录
        """

        allure.step("开始验证名称长度")

        # 写log
        log = Log.MyLog()
        log.info('文件已经开始执行')
        conf = Config()
        data = CreateHierarchy()

        with allure.step("写入Log"):
            allure.attach('写入log', '文件已经开始执行')

        request = Request.Request(action)

        # 获取请求域名
        host = conf.host_debug
        req_url = 'http://' + host

        # 获取请求参数
        urls = data.url
        params = data.data
        header = data.header
        requestsql = data.selectsql
        env = conf.environment
        responsecode = data.responsecode
        responsesql = data.responsesql
        casedescription = data.casedec

        # 获取token
        token = Session().get_session('debug')
        print(token)
        dict_token = {'X-Api-Authorization': token}
        header = dict(header[2])
        header.update(dict_token)
        print(header)

        # 参数化请求参数
        try:
            sqlresult = SqlResult(requestsql[2], env).get_sqlresult()
            params[2][0]['parent_id'] = sqlresult['id']
        except:
            with allure.step("获取输入参数值"):
                allure.attach('参数化', params[2][0]['name'])

        # 请求接口
        api_url = req_url + urls[2]
        print(api_url)
        print(params[2][0])
        print(header)

        response = request.post_request(api_url, json.dumps(params[2][0]), header)
        with allure.step("开始请求接口"):
            allure.attach('request', params[2][0])
            allure.attach('header', header)
            allure.attach('response', response)
        print(response)

        # 增加断言
        assertbody = Assertions()
        assertbody.assert_text(str(response['code']), str(responsecode[2]))
        if (response['code'] == responsecode[2]):
            assertbody.assert_text(response['text'], 'data.name should NOT be longer than 32 characters')
            allure.step("断言完成")
        else:
            with allure.step("执行完成，Code不一致"):
                allure.attach('request', params[1][0])

    @allure.severity('normal')
    @allure.story('parent_id不存在')
    def test_hierarchy_04(self, action):
        """
            用例描述：测试创建二级目录
        """

        allure.step("开始创建二级目录")

        # 写log
        log = Log.MyLog()
        log.info('文件已经开始执行')
        conf = Config()
        data = CreateHierarchy()

        with allure.step("写入Log"):
            allure.attach('写入log', '文件已经开始执行')

        request = Request.Request(action)

        # 获取请求域名
        host = conf.host_debug
        req_url = 'http://'+host

        # 获取请求参数
        urls = data.url
        params = data.data
        header = data.header
        requestsql = data.selectsql
        env=conf.environment
        responsecode = data.responsecode
        responsesql = data.responsesql
        casedescription = data.casedec

        #获取token
        token=Session().get_session('debug')
        print(token)
        dict_token={'X-Api-Authorization':token}
        header=dict(header[3])
        header.update(dict_token)
        print(header)


        #参数化请求参数
        try:
            sqlresult = SqlResult(requestsql[3], env).get_sqlresult()
            params[3][0]['name']='部门'+str(int(time.time()))
        except:
            with allure.step("获取输入参数值"):
                allure.attach('参数化', params[3][0]['name'])

        # 请求接口
        api_url = req_url+urls[3]
        print(api_url)
        print(params[3][0])
        print(header)

        response = request.post_request(api_url, json.dumps(params[3][0]),header)
        with allure.step("开始请求接口"):
            allure.attach('request', params[3][0])
            allure.attach('header', header)
            allure.attach('response', response)
        print(response)

        # 增加断言
        assertbody = Assertions()
        assertbody.assert_text(str(response['code']), str(responsecode[3]))
        if(response['code'] == responsecode[3]):
            assertbody.assert_text(str(response['header']['X-Api-Error-Code']), "ERR_NO_REFERENCED_ROW")
            allure.step("断言完成")
        else:
            with allure.step("执行完成，Code不一致"):
                allure.attach('request', params[3][0])

    @allure.severity('normal')
    @allure.story('name不存在')
    def test_hierarchy_05(self, action):
        """
            用例描述：测试创建二级目录
        """

        allure.step("开始创建二级目录")

        # 写log
        log = Log.MyLog()
        log.info('文件已经开始执行')
        conf = Config()
        data = CreateHierarchy()

        with allure.step("写入Log"):
            allure.attach('写入log', '文件已经开始执行')

        request = Request.Request(action)

        # 获取请求域名
        host = conf.host_debug
        req_url = 'http://'+host

        # 获取请求参数
        urls = data.url
        params = data.data
        header = data.header
        requestsql = data.selectsql
        env=conf.environment
        responsecode = data.responsecode
        responsesql = data.responsesql
        casedescription = data.casedec

        #获取token
        token=Session().get_session('debug')
        print(token)
        dict_token={'X-Api-Authorization':token}
        header=dict(header[4])
        header.update(dict_token)
        print(header)


        #参数化请求参数
        try:
            sqlresult = SqlResult(requestsql[4], env).get_sqlresult()
            params[4][0]['parent_id'] = sqlresult['id']
        except:
            with allure.step("获取输入参数值"):
                allure.attach('参数化', params[4][0]['name'])

        # 请求接口
        api_url = req_url+urls[4]
        print(api_url)
        print(params[4][0])
        print(header)

        response = request.post_request(api_url, json.dumps(params[4][0]),header)
        with allure.step("开始请求接口"):
            allure.attach('request', params[4][0])
            allure.attach('header', header)
            allure.attach('response', response)
        print(response)

        # 增加断言
        assertbody = Assertions()
        assertbody.assert_text(str(response['code']), str(responsecode[4]))
        if(response['code'] == responsecode[4]):
            assertbody.assert_text(response['text'], "data should have required property 'name'")
            allure.step("断言完成")
        else:
            with allure.step("执行完成，Code不一致"):
                allure.attach('request', params[4][0])


    @allure.severity('normal')
    @allure.story('name值传空')
    def test_hierarchy_06(self, action):
        """
            用例描述：测试创建二级目录
        """

        allure.step("开始创建二级目录")

        # 写log
        log = Log.MyLog()
        log.info('文件已经开始执行')
        conf = Config()
        data = CreateHierarchy()

        with allure.step("写入Log"):
            allure.attach('写入log', '文件已经开始执行')

        request = Request.Request(action)

        # 获取请求域名
        host = conf.host_debug
        req_url = 'http://'+host

        # 获取请求参数
        urls = data.url
        params = data.data
        header = data.header
        requestsql = data.selectsql
        env=conf.environment
        responsecode = data.responsecode
        responsesql = data.responsesql
        casedescription = data.casedec

        #获取token
        token=Session().get_session('debug')
        print(token)
        dict_token={'X-Api-Authorization':token}
        header=dict(header[5])
        header.update(dict_token)
        print(header)


        #参数化请求参数
        try:
            sqlresult = SqlResult(requestsql[5], env).get_sqlresult()
            params[5][0]['parent_id'] = sqlresult['id']
        except:
            with allure.step("获取输入参数值"):
                allure.attach('参数化', params[5][0]['name'])

        # 请求接口
        api_url = req_url+urls[5]
        print(api_url)
        print(params[5][0])
        print(header)

        response = request.post_request(api_url, json.dumps(params[5][0]),header)
        with allure.step("开始请求接口"):
            allure.attach('request', params[5][0])
            allure.attach('header', header)
            allure.attach('response', response)
        print(response)

        # 增加断言
        assertbody = Assertions()
        assertbody.assert_text(str(response['code']), str(responsecode[5]))
        if(response['code'] == responsecode[5]):
            assertbody.assert_text(response['text'], "data.name should be string")
            allure.step("断言完成")
        else:
            with allure.step("执行完成，Code不一致"):
                allure.attach('request', params[5][0])

    @allure.severity('normal')
    @allure.story('name值传空')
    def test_hierarchy_07(self, action):
        """
            用例描述：测试创建二级目录
        """

        allure.step("开始创建二级目录")

        # 写log
        log = Log.MyLog()
        log.info('文件已经开始执行')
        conf = Config()
        data = CreateHierarchy()

        with allure.step("写入Log"):
            allure.attach('写入log', '文件已经开始执行')

        request = Request.Request(action)

        # 获取请求域名
        host = conf.host_debug
        req_url = 'http://' + host

        # 获取请求参数
        urls = data.url
        params = data.data
        header = data.header
        requestsql = data.selectsql
        env = conf.environment
        responsecode = data.responsecode
        responsesql = data.responsesql
        casedescription = data.casedec

        # 获取token
        token = Session().get_session('debug')
        print(token)
        dict_token = {'X-Api-Authorization': token}
        header = dict(header[6])
        header.update(dict_token)
        print(header)

        # 参数化请求参数
        try:
            sqlresult = SqlResult(requestsql[6], env).get_sqlresult()
            params[6][0]['parent_id'] = sqlresult['id']
        except:
            with allure.step("获取输入参数值"):
                allure.attach('参数化', params[6][0]['name'])

        # 请求接口
        api_url = req_url + urls[6]
        print(api_url)
        print(params[6][0])
        print(header)

        response = request.post_request(api_url, json.dumps(params[6][0]), header)
        with allure.step("开始请求接口"):
            allure.attach('request', params[6][0])
            allure.attach('header', header)
            allure.attach('response', response)
        print(response)

        # 增加断言
        assertbody = Assertions()
        assertbody.assert_text(str(response['code']), str(responsecode[6]))
        if (response['code'] == responsecode[6]):
            assertbody.assert_text(response['text'], "data.name should NOT be shorter than 1 characters")
            allure.step("断言完成")
        else:
            with allure.step("执行完成，Code不一致"):
                allure.attach('request', params[6][0])

    @allure.severity('normal')
    @allure.story('一级name重复')
    def test_hierarchy_08(self, action):
        """
            用例描述：一级name重复
        """

        allure.step("一级name重复")

        # 写log
        log = Log.MyLog()
        log.info('文件已经开始执行')
        conf = Config()
        data = CreateHierarchy()

        with allure.step("写入Log"):
            allure.attach('写入log', '文件已经开始执行')

        request = Request.Request(action)

        # 获取请求域名
        host = conf.host_debug
        req_url = 'http://' + host

        # 获取请求参数
        urls = data.url
        params = data.data
        header = data.header
        requestsql = data.selectsql
        env = conf.environment
        responsecode = data.responsecode
        responsesql = data.responsesql
        casedescription = data.casedec

        # 获取token
        token = Session().get_session('debug')
        print(token)
        dict_token = {'X-Api-Authorization': token}
        header = dict(header[7])
        header.update(dict_token)
        print(header)

        # 参数化请求参数
        try:
            sqlresult = SqlResult(requestsql[7], env).get_sqlresult()
            params[7][0]['name'] = sqlresult['name']
        except:
            with allure.step("获取输入参数值"):
                allure.attach('参数化', params[7][0]['name'])

        # 请求接口
        api_url = req_url + urls[7]
        print(api_url)
        print(params[7][0])
        print(header)

        response = request.post_request(api_url, json.dumps(params[7][0]), header)
        with allure.step("开始请求接口"):
            allure.attach('request', params[7][0])
            allure.attach('header', header)
            allure.attach('response', response)
        print(response)

        # 增加断言
        assertbody = Assertions()
        assertbody.assert_text(str(response['code']), str(responsecode[7]))
        if (response['code'] == responsecode[7]):
            assertbody = Assertions()
            assertbody.assert_text(response['text'], "data.name should NOT be shorter than 1 characters")
            allure.step("断言完成")
        else:
            with allure.step("执行完成，Code不一致"):
                allure.attach('request', params[7][0])

    @allure.severity('normal')
    @allure.story('二级name重复')
    def test_hierarchy_09(self, action):
        """
            用例描述：一级name重复
        """

        allure.step("二级name重复")

        # 写log
        log = Log.MyLog()
        log.info('文件已经开始执行')
        conf = Config()
        data = CreateHierarchy()

        with allure.step("写入Log"):
            allure.attach('写入log', '文件已经开始执行')

        request = Request.Request(action)

        # 获取请求域名
        host = conf.host_debug
        req_url = 'http://' + host

        # 获取请求参数
        urls = data.url
        params = data.data
        header = data.header
        requestsql = data.selectsql
        env = conf.environment
        responsecode = data.responsecode
        responsesql = data.responsesql
        casedescription = data.casedec

        # 获取token
        token = Session().get_session('debug')
        print(token)
        dict_token = {'X-Api-Authorization': token}
        header = dict(header[8])
        header.update(dict_token)
        print(header)

        # 参数化请求参数
        try:
            sqlresult = SqlResult(requestsql[8], env).get_sqlresult()
            params[8][0]['name'] = sqlresult['name']
            params[8][0]['parent_id'] = sqlresult['parent_id']
        except:
            with allure.step("获取输入参数值"):
                allure.attach('参数化', params[8][0]['name'])

        # 请求接口
        api_url = req_url + urls[8]
        print(api_url)
        print(params[8][0])
        print(header)

        response = request.post_request(api_url, json.dumps(params[8][0]), header)
        with allure.step("开始请求接口"):
            allure.attach('request', params[8][0])
            allure.attach('header', header)
            allure.attach('response', response)
        print(response)

        # 增加断言
        assertbody = Assertions()
        assertbody.assert_text(str(response['code']), str(responsecode[8]))
        if (response['code'] == responsecode[8]):
            assertbody = Assertions()
            assertbody.assert_text(response['text'], "data.name should NOT be shorter than 1 characters")
            allure.step("断言完成")
        else:
            with allure.step("执行完成，Code不一致"):
                allure.attach('request', params[8][0])

    @allure.severity('minor')
    @allure.story('parent_id是字符')
    def test_hierarchy_10(self, action):
        """
            用例描述：一级name重复
        """

        allure.step("parent_id是字符")

        # 写log
        log = Log.MyLog()
        log.info('文件已经开始执行')
        conf = Config()
        data = CreateHierarchy()

        with allure.step("写入Log"):
            allure.attach('写入log', '文件已经开始执行')

        request = Request.Request(action)

        # 获取请求域名
        host = conf.host_debug
        req_url = 'http://' + host

        # 获取请求参数
        urls = data.url
        params = data.data
        header = data.header
        requestsql = data.selectsql
        env = conf.environment
        responsecode = data.responsecode
        responsesql = data.responsesql
        casedescription = data.casedec

        # 获取token
        token = Session().get_session('debug')
        print(token)
        dict_token = {'X-Api-Authorization': token}
        header = dict(header[9])
        header.update(dict_token)
        print(header)

        # 请求接口
        api_url = req_url + urls[9]
        print(api_url)
        print(params[9][0])
        print(header)

        response = request.post_request(api_url, json.dumps(params[9][0]), header)
        with allure.step("开始请求接口"):
            allure.attach('request', params[9][0])
            allure.attach('header', header)
            allure.attach('response', response)
        print(response)

        # 增加断言
        assertbody = Assertions()
        assertbody.assert_text(str(response['code']), str(responsecode[9]))
        if (response['code'] == responsecode[9]):
            assertbody = Assertions()
            assertbody.assert_text(response['text'], "data.parent_id should be integer")
            allure.step("断言完成")
        else:
            with allure.step("执行完成，Code不一致"):
                allure.attach('request', params[9][0])

