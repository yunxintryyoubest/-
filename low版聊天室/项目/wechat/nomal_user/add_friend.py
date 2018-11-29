# #######################################################################欢迎进入加好友的页面
# import  socket
# import selectors
# import  threading
# import time
# import  os,sys
# PATH=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.append(PATH)
# QQ_IP = open('ip_save.txt', 'r')
# QQ_IP = QQ_IP.read()
# print('已经取到这个ip地址：', QQ_IP)
#
# import json
# f_open = open('QQ_ID_docu.txt', 'r')
# all_dic_data = json.loads(f_open.read())
# QQ_ID = all_dic_data
#
#
# class add_friend:
#
#     print('欢迎QQ用户[{}]进入加好友页面......................................................'.format(QQ_ID))
#     def __init__(self):
#         import socket
#         sk = socket.socket()
#         # self.sk = sk
#         sk.connect((QQ_IP, 8080))
#         print('进来...............................')
#         data = sk.recv(1024)
#         print('接收到数据:', data)
#         add_number = input('请输入你要加的好友QQ：')
#         sk.send(str(add_number).encode('utf-8'))
#         print('已经发送请求给服务端>>>>>>>>>>>>>>>>>>>>>>>>>>>')
#         # self.add_start()
#     # def add_start(self):
#     #     while True:
#             # print('进来...............................')
#             # data = self.sk.recv(1024)
#             # print('接收到数据:', data)
#             # add_number = input('请输入你要加的好友QQ：')
#             # self.sk.send(str(add_number).encode('utf-8'))
#             # print('已经发送请求给服务端>>>>>>>>>>>>>>>>>>>>>>>>>>>')
#
#
# add_friend()