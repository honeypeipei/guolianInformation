# # # # -*- coding: utf-8 -*-
# # # # @Time    : 2018/7/30 下午4:14
# # # # @Author  : Grady
# # # # @File    : Teset_Getproduct.py
# # #
# # #
# # import requests
# # import json
# # #
# # # # http://dev.udms.guolianzj.com/api/system/login
# # # # {"mode": "un","auth": "admin","password": "123"}
# # # # {'Content-Type': 'application/json;charset=utf-8', 'X-Api-Version': '1.X'}
# # #
# # url="http://dev.udms.guolianzj.com/api/system/login"
# # data={"mode": "un","auth": "admin","password": "1234"}
# # header={"Content-Type": "application/json;charset=utf-8", "X-Api-Version": "1.X"}
# # data=json.dumps(data)
# # response=requests.post(url=url,data=data,headers=header)
# # print(response.headers)
# # #
# # # aa='111'
# # # aa.replace()
# # #
# # # dd={'id': 1, 'register_name': 'admin', 'password': '202cb962ac59075b964b07152d234b70', 'real_name': '管理员',
# # #   'phone_number': '18691094417'}
# # #
# # # for k, v in dd.items():
# # #     print(dd[k])
#
#
# import time
# time_stamp = time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))
# print(time_stamp)
# print(int(time.time()))
#
# import datetime
# time_stamp = '{0:%Y-%m-%d-%H-%M}'.format(datetime.datetime.now())
# print(time_stamp);
#
# print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))

# dict_A={'A':1}
# dict_B={'B':1}
# dict_A.update(dict_B)
#
# print(dict_A)
# import json
# dict_A={'name': '公司'}
# print(json.dumps(dict_A))


a= "SELECT id,name,parent_id from tb_hierarchy where id ='@sqlresult'"
a=a.replace('@sqlresult','66')
print(a)