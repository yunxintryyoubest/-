################################################################这里是与其他人聊天的界面############################################
import os,sys
PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(PATH)

import json
f_open = open('QQ_ID_docu.txt', 'r')
all_dic_data = json.loads(f_open.read())
QQ_ID = all_dic_data
with open(('{}/nomal_user/nomal_all_ip_data/chat_others_ip/{}/chat_ID.txt'.format(PATH, QQ_ID)), 'r')as f:
    other_ID=f.read()
    f.close()


with open(('{}/nomal_user/nomal_all_ip_data/chat_others_ip/{}/chat.txt'.format(PATH, QQ_ID)), 'r')as f:
    other_ip=f.read()
    f.close()


print('拿到这个ip地址：',other_ip)
import demjson

class nomal_user_chat_others:
    print('欢迎和QQ好哟【{}】聊天!!!!!!!!'.format(other_ID))
    def __init__(self):
        import socket
        sk = socket.socket()
        sk.connect((other_ip, 8080))
        self.sk = sk
        self.other_chat_start()
    def other_chat_start(self):
        print('开始和{}聊天了'.format(other_ID))
        while True:
            try:
                send_message=input('请输入你要发送的message>>>>>>>>>>>：')
                # print('已经发送消息',send_message)
                print('success send message  :',send_message)
                self.sk.send(send_message.encode('utf-8'))
                recv_message=self.sk.recv(1024).decode('utf-8')
                print('接收到QQ好友【{}】的消息:'.format(other_ID),recv_message)
            except Exception as e:
                print(e)