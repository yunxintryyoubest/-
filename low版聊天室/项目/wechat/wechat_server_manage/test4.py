
################################################################这里是与其他人聊天的界面############################################
import os ,sys
PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(PATH)

# import json
# f_open = open('QQ_ID_docu.txt', 'r')
# all_dic_data = json.loads(f_open.read())
# QQ_ID = all_dic_data
# with open(('{}/nomal_user/nomal_all_ip_data/chat_others_ip/{}/chat_{}.txt'.format(PATH, QQ_ID, number)), 'w')as f: other_ip=f. read()
#     f.close()
import demjson

# other_ip=input('输入：')

#
# class nomal_user_chat_others:
#     print('欢迎与others聊天!!!!!!!!')
#     def __init__(self):
#         import socket
#         sk = socket.socket()
#         sk.connect(('127.70.120.9', 8080))
#         self.sk = sk
#         self.other_chat_start()
#     def other_chat_start(self):
#         print('开始聊天了')
#         while True:
#             try:
#                 input('请输入你要发送的message>>>>>>>>>>>:')
#
#                 pass
#             except Exception as e:
#                 print(e)

import socket
sk = socket.socket()
sk.connect(('127.70.120.9', 8080))
# self.sk = sk



print('欢迎与others聊天!!!!!!!!')

# recv_message = sk.recv(1024).decode('utf-8')


def start():
    print('启动start')
start()
# while True:
#     send_message = input('（我）输入:')
#     sk.send(send_message.encode('utf-8'))
#     print('已经发送')
#
#     recv_message = sk.recv(1024).decode('utf-8')
#     print(recv_message)
#
#     if not recv_message:
#         send_message = input('（我）输入:')
#         sk.send(send_message.encode('utf-8'))
#
#
#
# while True:
#     send_message = input('（我）输入:')
#     # if not send_message:
#     #     break
#     # send_message = input('（我）输入:')
#     sk.send(send_message.encode('utf-8'))
#     recv_message = sk.recv(1024).decode('utf-8')
#
#     if  not recv_message:
#         break
#     recv_message = sk.recv(1024).decode('utf-8')








# def send():
#     # # while True:
#     # print('发送的消息')
#     # send_message = input('（我）输入:')
#     # sk.send(send_message.encode('utf-8'))
#     # print(send_message)
        # return send_message


# def recv():
#     # while True:
#     # print('接收的消息')
#     recv_message = sk.recv(1024).decode('utf-8')
#
#     print('接收到',recv_message)
#         # return recv_message

#
# while True:                #通信循环
#     data = input('> ')       #客户端输入信息
#     if not data:     #如果输入信息为空，则跳出循环，关闭通信
#         break
#
#     data = str.encode(data)
#     sk.send(data)     #发送客户端信息
#     data = sk.recv(1024)     #接受服务器返回信息
#     if not data:        #如果服务器未返回信息，关闭通信循环
#         break
#     print('get:',data.decode('utf-8'))


# while True:
#     if time.sleep(5):
#
#         recv()
#     else:
#         send()



# ##############################################展示在这里


# while True:
#     if not  recv_list:
#         send()
#         print(send_list)
#     else:
#         recv()
#         print(recv_list)
# while True:
#     if send_list:
#         print(send_list)
#     elif recv_list:
#
#         print(recv_list)
#     else:
#         print('没有值输入输出。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。')
# import threading
# send_thread=threading.Thread(target=send())
# recv_thread=threading.Thread(target=recv())
# send_thread.start()
# recv_thread.start()














# t1 = threading.Thread(target=multi_user, args=(key, value,))





















# thread = []
# t = []
# for i in range(0, len(all_QQ)):
#     (key, value), = all_QQ[i].items()
#     print('这个当前用户ip是:', value)
#     print('这个当前用户是:', key)
#     i = threading.Thread(target=multi_user, args=(key, value,))
#     # i._stop()
#     thread.append(i)
# for j in thread:
#     j.start()

print('ending................。。。。')





































































