#####################################这个是自己的那个聊天页面，一登录成功就会开启



###################################################注册和登录成功的页面#####################################
#####################取ip地址中





#####################################################注册功能和登录成功的页面，已经拿到这个ip地址######################################################
import threading
import time
import os, sys

PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# PATH= os.path.abspath(os.path.dirname(__file__))
##########################这个是当前的绝对路径
sys.path.append(PATH)
import json







f_open = open('QQ_ID_docu.txt', 'r')
all_dic_data = json.loads(f_open.read())
QQ_ID = all_dic_data
# print(QQ_ID)


QQ_IP = open('ip_save.txt', 'r')
QQ_IP = QQ_IP.read()
print('已经取到这个ip地址：', QQ_IP)


#################当有消息发过来的时候，做个判断，是否查看这个消息#############################################


# import socket
# sk = socket.socket()
# sk.connect((QQ_IP, 8080))
# print('运行message线程了')
# data = sk.recv(1024)
# msg = input('输入:').strip()
# # tcp_client.sendto(client_main_choice.encode('utf-8'), ip_port)
# print('已经发送消息给服务端了')
# sk.send(msg.encode('utf-8'))
# # sk.send(client_main_choice)
# print('已经发送')
# print(data.decode('utf-8'))









print('线程 message已经开启...................................................................')
class normal_user_message:

    try:
        def __init__(self):
            import socket
            sk = socket.socket()
            self.sk = sk
            sk.connect((QQ_IP, 8080))
            print('欢迎用户【{}】进入消息页面'.format(QQ_ID))
            # print('QQ用户【{}】已经上线..................................'.format(QQ_ID))
            self.main_start()
        def start(self):
            print('执行start页面')
            try:
                data = sk.recv(102400)

                ###########################会卡主######################################################
                print('判断是否有数据................................')
                if data:
                    with open('existed_message.txt','w')as f:
                        f.write(str(data))
                        f.close()
                    see_message=input('是否查看这个消息?(y/n)')
                    if see_message=='y':
                        print('您选择了是')
                        fh=open('existed_message.txt','w')
                        see_data=fh.read()
                        fh.close()
                        print('这个消息是：',see_data)
                    elif see_message=='n':
                        print('您选择了取消')
                        self.main_start()
                else:
                    self.main_start()
            except Exception as e:
                print(e)
                ##########################接收到好友发送过来的消息#############################################################################
        def main_start(self):
            try:
                client_main_menus = '''
                                  1,选择已经发送消息的好友
                                  2,搜索（个人，群，公众号等anything）
                                   '''
                # msg = input('输入：')
                print(client_main_menus)
                client_main_choice = input('请输入你的选择（1-2）:').strip()
                print('开始运行客户端了')
                # msg = input('输入:').strip()
                    # tcp_client.sendto(client_main_choice.encode('utf-8'), ip_port)
                print('已经发送消息给服务端了')
                self.sk.send(client_main_choice.encode('utf-8'))
                    # sk.send(client_main_choice)
                print('已经发送')
                if client_main_choice==str(1):
                    print('已经发送消息的好友如下：')


                elif client_main_choice==str(2):
                    print('您选择了搜索功能')
                else:
                    print('输入非法，找不到..................')
                # data = sk.recv(1024)
                # print(data.decode('utf-8'))
            except Exception as e:
                print(e)
    except Exception as e:
        print(e)
                ####################################################菜单选项#################################################################################






