#
# import  os,sys
# import socket
#
# PATH=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.append(PATH)
# ################################客户端#################################首页
# import  time
# class client_main:
#     print('正在启动clent聊天室，请等待.....................')
#     # time.sleep(3)
#     def __init__(self):
#         print('启动成功..........................')
#         self.client_start()
#
#     def client_start(self):
#         import socket
#         sk = socket.socket()
#         sk.connect(('127.1.1.0', 8080))
#         # print('进入普通用户验证环节...........................')
#         print('已进入聊天室(client端）...............................................')
#         nomal_user_menus_choices = '''
#         1,'登录'
#         2,'注册'
#         3,'退出'
#         '''
#         print(nomal_user_menus_choices)
#         nomal_user_menus_choice = input('请输入你的选择:')
#         print('已经发送数据出去')
#         # data = sk.recv(1024)
#         # print('接收到数据:', data)
#         if nomal_user_menus_choice == str(1):
#             print('进入登录环节...........................')
#             # msg=input('输入:')
#             try:
#                 # msg = input('输入：')
#                 msg='login_request'
#                 sk.send(msg.encode('utf-8'))
#                 print('已经发送')
#                 data = sk.recv(1024)
#                 print('接收成功')
#                 print('接收到服务端的数据是:', data.decode('utf-8'))
#                 # if data:
#                 #     from   nomal_user import normal_user_authenticate
#                 #     normal_user_authenticate.user_authenticate()
#             except Exception as e:
#                 print(e)
#         elif nomal_user_menus_choice==str(2):
#             print('进入注册环节')
#             try:
#                 # msg = input('输入：')
#                 msg = 'register_request'
#                 sk.send(msg.encode('utf-8'))
#                 print('已经发送')
#                 data = sk.recv(1024)
#                 print('接收成功')
#                 print('接收到服务端的数据是:', data.decode('utf-8'))
#                 # if data:
#                 #     from nomal_user import nomal_user_register
#                 #     nomal_user_register.normal_user_register()
#             except Exception as e:
#                 print(e)
# client_main()

import  os,sys
import socket

PATH=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(PATH)
################################客户端#################################首页
import  time
class client_main:
    print('正在启动clent聊天室，请等待.....................')
    # time.sleep(3)
    def __init__(self):
        print('启动成功..........................')
        self.client_start()

    def client_start(self):
        # print('进入普通用户验证环节...........................')
        print('已进入聊天室(client端）...............................................')
        nomal_user_menus_choices = '''
        1,'登录'
        2,'注册'
        3,'退出'
        '''
        print(nomal_user_menus_choices)
        nomal_user_menus_choice = input('请输入你的选择:')
        print('已经发送数据出去')
        if nomal_user_menus_choice == str(1):
            print('进入登录环节...........................')
            try:
                from   nomal_user import normal_user_authenticate
                normal_user_authenticate.user_authenticate()
            except Exception as e:
                print(e)
        elif nomal_user_menus_choice==str(2):
            print('进入注册环节')
            try:
                from nomal_user import nomal_user_register
                nomal_user_register.normal_user_register()
            except Exception as e:
                print(e)
client_main()

