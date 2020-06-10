# -*- coding: utf-8 -*-
# @Time    : 2018/7/30 下午4:14
# @Author  : Grady
# @File    : Teset_Getproduct.py


import allure
import pytest
from  Common.SqlResult import SqlResult

from Common import Consts
from Common import Request
from Conf.Config import Config
from Params.params import Login
from Common import Log
import allure
import json
import requests
from Common.Assert import Assertions
from Common.MyEncoder import MyEncoder


@allure.feature('Login')
class Testlogin:

    @allure.severity('blocker')
    @allure.story('测试正常登录')
    def test_login_01(self, action):
        """
            用例描述：测试正常登录
        """
        # 写log
        with allure.step("写入Log"):
            log = Log.MyLog()
            log.info('文件已经开始执行')
            conf = Config()
            data = Login()


        request = Request.Request(action)

        #获取域名
        host = conf.host_debug
        req_url = 'http://'+host

        #获取请求参数
        urls = data.url
        params = data.data
        header = data.header
        requestsql = data.selectsql
        env=conf.environment
        responsecode = data.responsecode
        responsesql = data.responsesql
        casedescription = data.casedec

        #请求参数化
        with allure.step("获取输入参数值,{0}".format(requestsql[1])):
            try:
                sqlresult = SqlResult(requestsql[0],env).get_sqlresult()
                params[0][0]['auth']=sqlresult['register_name']
            except:
                log.info("执行sql报错：："+requestsql[0])

        print(params[0][0])

        # 请求接口
        api_url = req_url+urls[0]
        with allure.step("开始请求接口,RUL: {0},header:{1},request:{2}".format(api_url, header[0], params[0][0])):
            response = request.post_request(api_url, json.dumps(params[0][0]),header[0])
            print(response)

        # 数据库查询结果
        try:
            responsesql = str(responsesql[0]).replace('@sqlresult', sqlresult['register_name'])
            responsesqlresult = SqlResult(responsesql, env).get_sqlresult()
            with allure.step("获取预期结果值成功，查询Sql：{0},查询结果：{1}".format(responsesql,responsesqlresult)):
                log.info('查询结果数据库成功：'+responsesql)
        except:
            log.info('查询结果数据库失败：'+responsesql)

        # 增加断言
        assertbody = Assertions()
        # if response['code'] == responsecode[0]:
        #     for k, v in responsesqlresult.items():
        #         assertbody.assert_body(response['body'], k,responsesqlresult[k])
        #         if not assertbody.assert_body(response['body'], k, responsesqlresult[k]):
        #             break
        #         allure.attach(k, params[0][0])

        with allure.step("接口返回结果：{0}".format(response)):
            assertbody.assert_text(str(response['code']), str(responsecode[0]))




    @allure.severity('blocker')
    @allure.story('密码错误登录')
    def test_login_02(self, action):
        """
            用例描述：密码错误数据
        """

        # 写log
        with allure.step("写入Log"):
            log = Log.MyLog()
            log.info('文件已经开始执行')
            conf = Config()
            data = Login()


        request = Request.Request(action)

        #获取域名
        host = conf.host_debug
        req_url = 'http://'+host

        #获取请求参数
        urls = data.url
        params = data.data
        header = data.header
        requestsql = data.selectsql
        env=conf.environment
        responsecode = data.responsecode
        responsesql = data.responsesql
        casedescription = data.casedec

        #请求参数化
        with allure.step("获取输入参数值,{0}".format(requestsql[1])):
            try:
                sqlresult = SqlResult(requestsql[1],env).get_sqlresult()
                params[1][0]['auth']=sqlresult['register_name']
            except:
                log.info("执行sql报错：："+requestsql[1])

        print(params[1][0])

        # 请求接口
        api_url = req_url+urls[1]
        with allure.step("开始请求接口,RUL: {0},header:{1},request:{2}".format(api_url, header[0], params[0][0])):
            response = request.post_request(api_url, json.dumps(params[1][0]),header[1])
            print(response)

        assertbody = Assertions()
        assertbody.assert_text(str(response['code']), str(responsecode[1]))
        with allure.step("增加断言,ResponseCode：{0}=TestCode：{1}，ResponseHeader：{2}".format(response['code'], responsecode[1], response['header'])):
            if(response['code'] == responsecode[1]):
                #assertbody.assert_body(response['body'], 'message','密码错误')
                assertbody.assert_body(response['header'], 'X-Api-Error-Code','ERR_LOGIN_FAILED')
            else:
                log.info("执行完成，Code不一致")


    # @allure.severity('normal')
    # @allure.story('账号不存在')
    # def test_login_03(self, action):
    #     """
    #         用例描述：账号不存在
    #     """
    #
    #     with allure.step("登录用例执行开始"):
    #         allure.attach('账户名', 'admin')
    #
    #     #记录log
    #     log = Log.MyLog()
    #     log.info('文件已经开始执行')
    #     conf = Config()
    #     data = Login()
    #
    #     with allure.step("写入Log"):
    #         allure.attach('写入log', '文件已经开始执行')
    #
    #     request = Request.Request(action)
    #
    #     #获取域名
    #     host = conf.host_debug
    #     req_url = 'http://'+host
    #
    #     #获取请求参数
    #     urls = data.url
    #     params = data.data
    #     header = data.header
    #     env=conf.environment
    #     responsecode = data.responsecode
    #     casedescription = data.casedec
    #
    #
    #     # 请求接口
    #     api_url = req_url+urls[2]
    #     response = request.post_request(api_url, json.dumps(params[2][0]),header[2])
    #     with allure.step("开始请求接口"):
    #         allure.attach('request', params[0][0])
    #         allure.attach('header', header[2])
    #         allure.attach('response', str(response))
    #     print(response)
    #
    #     assertbody = Assertions()
    #     assertbody.assert_text(str(response['code']), str(responsecode[2]))
    #     if(response['code'] == responsecode[2]):
    #         #assertbody.assert_body(response['body'], 'message','账户不存在')
    #         assertbody.assert_body(response['header'], 'X-Api-Error-Code','ERR_LOGIN_FAILED')
    #         with allure.step("断言完成"):
    #             allure.attach('X-Api-Error-Code', params[2][0])
    #     else:
    #         with allure.step("执行完成，Code不一致"):
    #             allure.attach('request', params[2][0])
    #
    # @allure.severity('normal')
    # @allure.story('账号超长')
    # def test_login_04(self, action):
    #     """
    #         用例描述：账号超长
    #     """
    #
    #     allure.step("登录用例执行开始")
    #
    #     #记录log
    #     log = Log.MyLog()
    #     log.info('文件已经开始执行')
    #     conf = Config()
    #     data = Login()
    #
    #     with allure.step("写入Log"):
    #         allure.attach('写入log', '文件已经开始执行')
    #
    #     request = Request.Request(action)
    #
    #     #获取域名
    #     host = conf.host_debug
    #     req_url = 'http://'+host
    #
    #     #获取请求参数
    #     urls = data.url
    #     params = data.data
    #     header = data.header
    #     env=conf.environment
    #     responsecode = data.responsecode
    #     casedescription = data.casedec
    #
    #
    #     # 请求接口
    #     api_url = req_url+urls[3]
    #     response = request.post_request(api_url, json.dumps(params[3][0]),header[3])
    #     with allure.step("开始请求接口"):
    #         allure.attach('request', params[3][0])
    #         allure.attach('header', header[3])
    #         allure.attach('response', str(response))
    #     print(response)
    #     print(params[3][0])
    #
    #     assertbody = Assertions()
    #     assertbody.assert_text(str(response['code']), str(responsecode[3]))
    #     if(response['code'] == responsecode[3]):
    #         #assertbody.assert_body(response['body'], 'message','账户不存在')
    #         assertbody.assert_body(response['header'], 'X-Api-Error-Code','ERR_LOGIN_FAILED')
    #         with allure.step("断言完成"):
    #             allure.attach('X-Api-Error-Code', params[3][0])
    #     else:
    #         with allure.step("执行完成，Code不一致"):
    #             allure.attach('request', params[3][0])
    #
    # @allure.severity('normal')
    # @allure.story('密码超长')
    # def test_login_05(self, action):
    #     """
    #         用例描述：密码超长
    #     """
    #
    #     allure.step("登录用例执行开始")
    #
    #     #记录log
    #     log = Log.MyLog()
    #     log.info('文件已经开始执行')
    #     conf = Config()
    #     data = Login()
    #
    #     with allure.step("写入Log"):
    #         allure.attach('写入log', '文件已经开始执行')
    #
    #     request = Request.Request(action)
    #
    #     #获取域名
    #     host = conf.host_debug
    #     req_url = 'http://'+host
    #
    #     #获取请求参数
    #     urls = data.url
    #     params = data.data
    #     header = data.header
    #     env=conf.environment
    #     responsecode = data.responsecode
    #     casedescription = data.casedec
    #
    #
    #     # 请求接口
    #     api_url = req_url+urls[4]
    #     response = request.post_request(api_url, json.dumps(params[4][0]),header[4])
    #     with allure.step("开始请求接口"):
    #         allure.attach('request', params[4][0])
    #         allure.attach('header', header[4])
    #         allure.attach('response', str(response))
    #     print(response)
    #     print(params[4][0])
    #
    #     assertbody = Assertions()
    #     assertbody.assert_text(str(response['code']), str(responsecode[4]))
    #     if(response['code'] == responsecode[4]):
    #         #assertbody.assert_body(response['body'], 'message','账户不存在')
    #         assertbody.assert_body(response['header'], 'X-Api-Error-Code','ERR_LOGIN_FAILED')
    #         with allure.step("断言完成"):
    #             allure.attach('X-Api-Error-Code', params[4][0])
    #     else:
    #         with allure.step("执行完成，Code不一致"):
    #             allure.attach('request', params[4][0])
    #
    # @allure.severity('normal')
    # @allure.story('mode节点传值不对')
    # def test_login_06(self, action):
    #     """
    #         用例描述：mode节点传值不对
    #     """
    #
    #     allure.step("登录用例执行开始")
    #
    #     #记录log
    #     log = Log.MyLog()
    #     log.info('文件已经开始执行')
    #     conf = Config()
    #     data = Login()
    #
    #     with allure.step("写入Log"):
    #         allure.attach('写入log', '文件已经开始执行')
    #
    #     request = Request.Request(action)
    #
    #     #获取域名
    #     host = conf.host_debug
    #     req_url = 'http://'+host
    #
    #     #获取请求参数
    #     urls = data.url
    #     params = data.data
    #     header = data.header
    #     env=conf.environment
    #     responsecode = data.responsecode
    #     casedescription = data.casedec
    #
    #
    #     # 请求接口
    #     api_url = req_url+urls[5]
    #     response = request.post_request(api_url, json.dumps(params[5][0]),header[5])
    #     with allure.step("开始请求接口"):
    #         allure.attach('request', params[5][0])
    #         allure.attach('header', header[5])
    #         allure.attach('response', str(response))
    #     print(response)
    #     print(params[5][0])
    #
    #     assertbody = Assertions()
    #     assertbody.assert_text(str(response['code']), str(responsecode[5]))
    #
    #     if(response['code'] == responsecode[5]):
    #         #assertbody.assert_body(response['body'], 'message','账户不存在')
    #         assertbody.assert_body(response['header'], 'X-Api-Error-Code','ERR_BAD_REQUEST')
    #         assertbody.assert_text(response['text'], 'data.mode should be equal to one of the allowed values')
    #         with allure.step("断言完成"):
    #             allure.attach('X-Api-Error-Code', params[5][0])
    #     else:
    #         with allure.step("执行完成，Code不一致"):
    #             allure.attach('request', params[5][0])
    #
    # @allure.severity('normal')
    # @allure.story('mode节点缺失')
    # def test_login_07(self, action):
    #     """
    #         用例描述：mode节点缺失
    #     """
    #
    #     allure.step("登录用例执行开始")
    #
    #     #记录log
    #     log = Log.MyLog()
    #     log.info('文件已经开始执行')
    #     conf = Config()
    #     data = Login()
    #
    #     with allure.step("写入Log"):
    #         allure.attach('写入log', '文件已经开始执行')
    #
    #     request = Request.Request(action)
    #
    #     #获取域名
    #     host = conf.host_debug
    #     req_url = 'http://'+host
    #
    #     #获取请求参数
    #     urls = data.url
    #     params = data.data
    #     header = data.header
    #     env=conf.environment
    #     responsecode = data.responsecode
    #     casedescription = data.casedec
    #
    #
    #     # 请求接口
    #     api_url = req_url+urls[6]
    #     response = request.post_request(api_url, json.dumps(params[6][0]),header[6])
    #     with allure.step("开始请求接口"):
    #         allure.attach('request', params[6][0])
    #         allure.attach('header', header[6])
    #         allure.attach('response', str(response))
    #     print(response)
    #     print(params[6][0])
    #     assertbody = Assertions()
    #     if(response['code'] == responsecode[6]):
    #
    #         #assertbody.assert_body(response['body'], 'message','账户不存在')
    #         assertbody.assert_body(response['header'], 'X-Api-Error-Code','ERR_BAD_REQUEST')
    #         assertbody.assert_text(response['text'], "data should have required property 'mode'")
    #         with allure.step("断言完成"):
    #             allure.attach('X-Api-Error-Code', params[6][0])
    #     else:
    #         assertbody.assert_text('11111', '200')
    #         with allure.step("执行完成，Code不一致"):
    #             allure.attach('request', params[6][0])
    #
    # @allure.severity('normal')
    # @allure.story('auth节点缺失')
    # def test_login_08(self, action):
    #     """
    #         用例描述：auth节点缺失
    #     """
    #
    #     allure.step("登录用例执行开始")
    #
    #     #记录log
    #     log = Log.MyLog()
    #     log.info('文件已经开始执行')
    #     conf = Config()
    #     data = Login()
    #
    #     with allure.step("写入Log"):
    #         allure.attach('写入log', '文件已经开始执行')
    #
    #     request = Request.Request(action)
    #
    #     #获取域名
    #     host = conf.host_debug
    #     req_url = 'http://'+host
    #
    #     #获取请求参数
    #     urls = data.url
    #     params = data.data
    #     header = data.header
    #     env=conf.environment
    #     responsecode = data.responsecode
    #     casedescription = data.casedec
    #
    #
    #     # 请求接口
    #     api_url = req_url+urls[7]
    #     response = request.post_request(api_url, json.dumps(params[7][0]),header[7])
    #     with allure.step("开始请求接口"):
    #         allure.attach('request', params[7][0])
    #         allure.attach('header', header[7])
    #         allure.attach('response', str(response))
    #     print(response)
    #     print(params[7][0])
    #     print(responsecode[7])
    #     assertbody = Assertions()
    #     if(response['code'] == responsecode[7]):
    #
    #         #assertbody.assert_body(response['body'], 'message','账户不存在')
    #         assertbody.assert_body(response['header'], 'X-Api-Error-Code','ERR_BAD_REQUEST')
    #         assertbody.assert_text(response['text'], "data should have required property 'auth'")
    #         with allure.step("断言完成"):
    #             allure.attach('X-Api-Error-Code', params[7][0])
    #     else:
    #         assertbody.assert_text('11111', '200')
    #         with allure.step("执行完成，Code不一致"):
    #             allure.attach('request', params[7][0])
    #
    # @allure.severity('normal')
    # @allure.story('password节点缺失')
    # def test_login_09(self, action):
    #     """
    #         用例描述：password节点缺失
    #     """
    #
    #     allure.step("登录用例执行开始")
    #
    #     #记录log
    #     log = Log.MyLog()
    #     log.info('文件已经开始执行')
    #     conf = Config()
    #     data = Login()
    #
    #     with allure.step("写入Log"):
    #         allure.attach('写入log', '文件已经开始执行')
    #
    #     request = Request.Request(action)
    #
    #     #获取域名
    #     host = conf.host_debug
    #     req_url = 'http://'+host
    #
    #     #获取请求参数
    #     urls = data.url
    #     params = data.data
    #     header = data.header
    #     env=conf.environment
    #     responsecode = data.responsecode
    #     casedescription = data.casedec
    #
    #
    #     # 请求接口
    #     api_url = req_url+urls[8]
    #     response = request.post_request(api_url, json.dumps(params[8][0]),header[8])
    #     with allure.step("开始请求接口"):
    #         allure.attach('request', params[8][0])
    #         allure.attach('header', header[8])
    #         allure.attach('response', str(response))
    #     print(response)
    #     print(params[8][0])
    #     print(responsecode[8])
    #     assertbody = Assertions()
    #     if(response['code'] == responsecode[8]):
    #
    #         #assertbody.assert_body(response['body'], 'message','账户不存在')
    #         assertbody.assert_body(response['header'], 'X-Api-Error-Code','ERR_BAD_REQUEST')
    #         assertbody.assert_text(response['text'], "data should have required property 'password'")
    #         with allure.step("断言完成"):
    #             allure.attach('X-Api-Error-Code', params[8][0])
    #     else:
    #         assertbody.assert_text('11111', '200')
    #         with allure.step("执行完成，Code不一致"):
    #             allure.attach('request', params[8][0])
    #
    # @allure.severity('normal')
    # @allure.story('mode为空')
    # def test_login_10(self, action):
    #     """
    #         用例描述：mode为空
    #     """
    #
    #     allure.step("登录用例执行开始")
    #
    #     #记录log
    #     log = Log.MyLog()
    #     log.info('文件已经开始执行')
    #     conf = Config()
    #     data = Login()
    #
    #     with allure.step("写入Log"):
    #         allure.attach('写入log', '文件已经开始执行')
    #
    #     request = Request.Request(action)
    #
    #     #获取域名
    #     host = conf.host_debug
    #     req_url = 'http://'+host
    #
    #     #获取请求参数
    #     urls = data.url
    #     params = data.data
    #     header = data.header
    #     env=conf.environment
    #     responsecode = data.responsecode
    #     casedescription = data.casedec
    #
    #
    #     # 请求接口
    #     api_url = req_url+urls[9]
    #     response = request.post_request(api_url, json.dumps(params[9][0]),header[9])
    #     with allure.step("开始请求接口"):
    #         allure.attach('request', params[9][0])
    #         allure.attach('header', header[9])
    #         allure.attach('response', str(response))
    #     print(response)
    #     print(params[9][0])
    #     print(responsecode[9])
    #     assertbody = Assertions()
    #     if(response['code'] == responsecode[9]):
    #
    #         #assertbody.assert_body(response['body'], 'message','账户不存在')
    #         assertbody.assert_body(response['header'], 'X-Api-Error-Code','ERR_BAD_REQUEST')
    #         assertbody.assert_text(response['text'], "data.mode should be equal to one of the allowed values")
    #         with allure.step("断言完成"):
    #             allure.attach('X-Api-Error-Code', params[9][0])
    #     else:
    #         assertbody.assert_text('11111', '200')
    #         with allure.step("执行完成，Code不一致"):
    #             allure.attach('request', params[9][0])
    #
    # @allure.severity('normal')
    # @allure.story('auth为空')
    # def test_login_11(self, action):
    #     """
    #         用例描述：auth为空
    #     """
    #
    #     allure.step("登录用例执行开始")
    #
    #     #记录log
    #     log = Log.MyLog()
    #     log.info('文件已经开始执行')
    #     conf = Config()
    #     data = Login()
    #
    #     with allure.step("写入Log"):
    #         allure.attach('写入log', '文件已经开始执行')
    #
    #     request = Request.Request(action)
    #
    #     #获取域名
    #     host = conf.host_debug
    #     req_url = 'http://'+host
    #
    #     #获取请求参数
    #     urls = data.url
    #     params = data.data
    #     header = data.header
    #     env=conf.environment
    #     responsecode = data.responsecode
    #     casedescription = data.casedec
    #
    #
    #     # 请求接口
    #     api_url = req_url+urls[10]
    #     response = request.post_request(api_url, json.dumps(params[10][0]),header[10])
    #     with allure.step("开始请求接口"):
    #         allure.attach('request', params[10][0])
    #         allure.attach('header', header[10])
    #         allure.attach('response', str(response))
    #     print(response)
    #     print(params[10][0])
    #     print(responsecode[10])
    #     assertbody = Assertions()
    #     if(response['code'] == responsecode[10]):
    #
    #         #assertbody.assert_body(response['body'], 'message','账户不存在')
    #         assertbody.assert_body(response['header'], 'X-Api-Error-Code','ERR_BAD_REQUEST')
    #         assertbody.assert_text(response['text'], "data.auth should be equal to one of the allowed values")
    #         with allure.step("断言完成"):
    #             allure.attach('X-Api-Error-Code', params[10][0])
    #     else:
    #         assertbody.assert_text('11111', '200')
    #         with allure.step("执行完成，Code不一致"):
    #             allure.attach('request', params[10][0])
    #
    #
    # @allure.severity('normal')
    # @allure.story('password为空')
    # def test_login_12(self, action):
    #     """
    #         用例描述：password为空
    #     """
    #
    #     allure.step("登录用例执行开始")
    #
    #     #记录log
    #     log = Log.MyLog()
    #     log.info('文件已经开始执行')
    #     conf = Config()
    #     data = Login()
    #
    #     with allure.step("写入Log"):
    #         allure.attach('写入log', '文件已经开始执行')
    #
    #     request = Request.Request(action)
    #
    #     #获取域名
    #     host = conf.host_debug
    #     req_url = 'http://'+host
    #
    #     #获取请求参数
    #     urls = data.url
    #     params = data.data
    #     header = data.header
    #     env=conf.environment
    #     responsecode = data.responsecode
    #     casedescription = data.casedec
    #
    #
    #     # 请求接口
    #     api_url = req_url+urls[11]
    #     response = request.post_request(api_url, json.dumps(params[11][0]),header[11])
    #     with allure.step("开始请求接口"):
    #         allure.attach('request', params[11][0])
    #         allure.attach('header', header[11])
    #         allure.attach('response', str(response))
    #     print(response)
    #     print(params[11][0])
    #     print(responsecode[11])
    #     assertbody = Assertions()
    #     if(response['code'] == responsecode[11]):
    #
    #         #assertbody.assert_body(response['body'], 'message','账户不存在')
    #         assertbody.assert_body(response['header'], 'X-Api-Error-Code','ERR_BAD_REQUEST')
    #         assertbody.assert_text(response['text'], "data.password should be equal to one of the allowed values")
    #         with allure.step("断言完成"):
    #             allure.attach('X-Api-Error-Code', params[11][0])
    #     else:
    #         assertbody.assert_text('11111', '200')
    #         with allure.step("执行完成，Code不一致"):
    #             allure.attach('request', params[11][0])
    #
    # @allure.severity('normal')
    # @allure.story('账号已被禁用')
    # def test_login_13(self, action):
    #     """
    #         用例描述：password为空
    #     """
    #
    #     allure.step("登录用例执行开始")
    #
    #     #记录log
    #     log = Log.MyLog()
    #     log.info('文件已经开始执行')
    #     conf = Config()
    #     data = Login()
    #
    #     with allure.step("写入Log"):
    #         allure.attach('写入log', '文件已经开始执行')
    #
    #     request = Request.Request(action)
    #
    #     #获取域名
    #     host = conf.host_debug
    #     req_url = 'http://'+host
    #
    #     #获取请求参数
    #     urls = data.url
    #     params = data.data
    #     header = data.header
    #     env=conf.environment
    #     responsecode = data.responsecode
    #     casedescription = data.casedec
    #
    #
    #     # 请求接口
    #     api_url = req_url+urls[12]
    #     response = request.post_request(api_url, json.dumps(params[12][0]),header[12])
    #     with allure.step("开始请求接口"):
    #         allure.attach('request', params[11][0])
    #         allure.attach('header', header[11])
    #         allure.attach('response', str(response))
    #     print(response)
    #     print(params[12][0])
    #     print(responsecode[12])
    #     assertbody = Assertions()
    #     assertbody.assert_text(str(response['code']), str(responsecode[12]))
    #     if(response['code'] == responsecode[11]):
    #
    #         #assertbody.assert_body(response['body'], 'message','账户不存在')
    #         assertbody.assert_body(response['header'], 'X-Api-Error-Code','ERR_BAD_REQUEST')
    #         assertbody.assert_text(response['text'], "data.password should be equal to one of the allowed values")
    #         with allure.step("断言完成"):
    #             allure.attach('X-Api-Error-Code', params[12][0])
    #     else:
    #         assertbody.assert_text('11111', '200')
    #         with allure.step("执行完成，Code不一致"):
    #             allure.attach('request', params[12][0])