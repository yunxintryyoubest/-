
#########

import json
import time
import random
# f_open = open('QQ_ID.txt', 'r')
# all_dic_data = json.loads(f_open.read())
# Dicyionary = all_dic_data

# Dicyionary=[]

# class test:
#     def __init__(self):
#         self.run()
#     def run_randoom_QQ_ID(self):
#         QQ_ID = random.randrange(100000000000)
#         return  QQ_ID
#
#     def run(self):
#         print('执行test验证')
#         ID=self.run_randoom_QQ_ID()
#         print(ID)
#         if ID  not  in Dicyionary:
#             print('没有分配的QQ号码')
#             print(ID)
#             Dicyionary.append(ID)
#             print(Dicyionary)
#         # Dicyionary.append(ID)
#             with open('QQ_ID.txt', 'w')as f:
#                 f.write(str(Dicyionary))
#                 f.close()
#         else:
#             print('已经分配这个QQ号码')
#             self.run()
#             print('已经重新分配这个QQ号码')
# test()

import  os,sys
import demjson
PATH=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# PATH= os.path.abspath(os.path.dirname(__file__))
##########################这个是当前的绝对路径
sys.path.append(PATH)
###################超级用户界面
from  conf import  settings
import  json,os,sys
import configparser
# from  conf import settings
# PATH=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# PATH= os.path.abspath(os.path.dirname(__file__))
# sys.path.append(PATH)
# print('admin_path这个绝对路径是:',PATH)
# print('导入admin账户成功')
from  admin_user import *
#
import demjson
# # QQ_docu=open('account'+".txt",'w')
# f_open1=open('account_data1'+'.txt','w')
# f_open=open('account_data1.txt','r')
# Dicyionary=json.loads(f_open.read())
# ################这个是一个字典形式
# class admin:
#     print('进入超级用户端..........')
#     print('请进入身份验证............')
#     admin_menus_start_choices='''
#     1,'直接登录',
#     2,'注册'
#     '''
#     print(admin_menus_start_choices)
#     admin_menus_start_choices_choice=input('请输入你的选择:')
#     ##########################登录页面#####################################
#     if admin_menus_start_choices_choice==str(1):
#         print('进入登录页面....................')
#         fh = open('account_data1.txt', 'r')
#         has_registered_admin_data=json.loads(fh.read())
#         print(has_registered_admin_data)
#         print(type(has_registered_admin_data))
#
#         input_admin_username = input('请输入账号：')
#         input_admin_keyword = str(input('请输入密码：'))
#         input_data = {}
#         input_data[input_admin_username] = input_admin_keyword
#         print(input_data)
#         print(len(has_registered_admin_data))
#         i=0
#         for i in range(0,len(has_registered_admin_data)):
#             if input_data ==  has_registered_admin_data[i]:
#                 print('用户匹配成功')
#                 print('身份验证成功')
#                 print('欢迎管理员【{}】进入后台管理系统............'.format(input_admin_username))
#                 print('welcome  to admin 界面...................')
#                 admin_menus = '''
#                           1,'查看'
#                           2,'搜索',
#                           3,'管理,
#                           4'账户信息'''
#                 print(admin_menus)
#                 admin_menu_choice=input('请输入你要选择的操作:')
#                 if admin_menu_choice == str(1):
#                     from  admin_user import look_informations
#                     look_informations.all_informations()
#                     break
#                 if admin_menu_choice==str(2):
#                     from  admin_user import admin_search
#                     admin_search.admin_serach()
#                     break
#                 if admin_menu_choice == str(4):
#                     # print('进入账户信息界面')
#                     from  admin_user  import  admin_user_personal_information
#                     admin_user_personal_information.admin_personal_information()
#                     break
#                 else:
#                     print('认证失败')
#                     break
#             else:
#                 continue
#         else:
#             print('身份验证失败')
















        ########################注册页面
    # elif admin_menus_start_choices_choice==str(2):
    #     print('进入注册页面')
    #     account={}
    #     admin_username=input('请输入你要添加的admin账号：')
    #     admin_keyword=input('请输入你要添加的admin密码：')
    #     account[admin_username]=admin_keyword
    #     Dicyionary.append(account)
    #     account_data_str=json.dumps(Dicyionary)
    #     f = open('account_data1.txt', 'w')
    #     f.write(account_data_str)
    #     f.close()
    #     # dic1 = open('account_data.txt', 'r')
    #     # all_data = json.loads(dic1.read())
    #     # print(all_data)
    #     # print('已经添加成功')
    #     print('注册成功')



# a=[{1:2}]

# fh=open('exist_users_QQ.txt','w')
# d=fh.write(str(a))
# fh.close()




########################################################取已经存在的QQ号码

# f=open('exist_users_QQ.txt','r')
# data=f.read()
# f.close()
# # print(data.encode('utf-8'))
# data=data.encode('utf-8')
# # print(type(data))
# import demjson
#
# da=demjson.decode(data)
# print(da)
# # print(type(da))
#
# exist={3:4}
# da.append(exist)
# print(da)
#
#
# fh=open('exist_users_QQ.txt','w')
# info=fh.write(str(da))
# fh.close()
# print(info)

# [{1: 2}, {3: 4}, {3: 4}, {3: 4}, {3: 4}]
#
#
# data={1:2}
# f = open('exist_users_QQ.txt', 'r')
# data1 = f.read()
# f.close()
# # print(data.encode('utf-8'))
# data2 = data1.encode('utf-8')
# # print(type(data))
# import demjson
#
# Dicyionary = demjson.decode(data2)
# print(Dicyionary)
# # i = 0
# print('data是,', data)
# for i in range(0, len(Dicyionary)):
#     print('第一步通过')
#     if Dicyionary[i] == data:
#         print('验证通过')
#
#         # break
#
#     else:
#         print('pass')
#         continue


# import json
# add_number=input('请输入：')
# with open('QQ_ID_IP_save.txt', 'r')as f:
#     add_QQ_ID_information = json.loads(f.read())
#     f.close()
#     #####################拿到对应的ip和QQ信息
# for i in range(0, len(add_QQ_ID_information)):
#     (key, value), = add_QQ_ID_information[i].items()
#     if key == add_number:
#         print('已经找到')
#         print(add_QQ_ID_information[i])
#         add_QQ_ID_information_data = add_QQ_ID_information[i]




# conn.send(add_QQ_ID_information_data.encode('utf-8'))









import os,sys

# if not os.path.exists('wechat_recode/9500025787_wechat'):
#     os.mkdir('wechat_recode/9500025787_wechat')
# print('wanghcneg ')

# import os,sys
#
# # os.mkdir('wechat_recode/9500025787_wechat')
# # PATH=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# PATH=os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# sys.path.append(PATH)
# print(PATH)

# import  QQ
# if not  os.path.exists('QQ/32332323'):
#     os.mkdir('QQ/32332323')


# class test:
#     print('test' * 100)
#     print('跳转到相应的聊天好友页面')
#     with open('login_QQ_ID.txt', 'r')as f:
#         exist_login_QQ_ID = f.read()
#         f.close()
#     print(type(exist_login_QQ_ID))
#     print(exist_login_QQ_ID)

# QQ_IP=1
# QQ_ID=2
# import demjson
# open('self_QQ_main_chat.txt', 'w')
# with open('self_QQ_main_chat.txt', 'r')as f:
#     self_QQ_ID = f.read()
#     f.close()
# if len(self_QQ_ID):
#     print('这里面有用户跳到主页面了')
#     self_QQ_ID = demjson.decode(self_QQ_ID)
# else:
#     print('没有用户跳转到主页面')
#     dic = []
# with open('self_QQ_main_chat.txt', 'w')as f:
#     f.write(str(dic))
#     f.close()
# with open('self_QQ_main_chat.txt', 'r')as fr:
#     all_main_QQ = fr.read()
#     fr.close()
# print('>'*100,all_main_QQ)
# all_main_QQ_ID = demjson.decode(all_main_QQ)
# self_dic = {}
# self_dic[QQ_ID] = QQ_IP
# all_main_QQ_ID.append(self_dic)
# print('这个自己是:',self_dic)
# print('*'*1000)
# print('这个原来的数据是:',all_main_QQ_ID)
# with open('self_QQ_main_chat.txt', 'w')as fw:
# fw.write(str(all_main_QQ_ID))
# fw.close()
# print('已经保存这个用户{}进主页面文件里面了（聊天）'.format(self_dic))








#################################################测试ip生成的部分

# from  wechat_server_manage import  server

# id=server.all_server()
# class create_id:
#     def create():
#         # id=input('输入:')
#         id=32323
#         return  id
# print('组队上课的')
#
# # create_id()
# ID=create_id.create()
# print(ID)
PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(PATH)


from  wechat_server_manage import create_main_chat_ip
ip=create_main_chat_ip.has_ip()
print(ip)


