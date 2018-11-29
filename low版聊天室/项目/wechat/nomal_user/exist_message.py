############################################当有消息的时候，就发送到主页面###########################################

import  socket
import selectors
import  threading
import time
import  os,sys
PATH=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(PATH)
import json
f_open = open('QQ_ID_docu.txt', 'r')
all_dic_data = json.loads(f_open.read())
QQ_ID = all_dic_data
# print(QQ_ID)


QQ_IP=open('ip_save.txt','r')
QQ_IP=QQ_IP.read()
print('已经取到这个ip地址：',QQ_IP)




class normal_user_main:
    print('开始运行这个客户端了')
    # def __init__(self):
    print('欢迎登录成功')
    print('QQ用户【{}】已经上线..................................'.format(QQ_ID))
    print('打开普通用户服务端.......................................')
        # self.start()
        # self.message_thread()
    def start():
        try:
            client_main_menus = '''
                       0:查看消息
                       1,查看你的好友（在线，离线）
                       2,个人账户信息
                       3,搜索（个人，群，公众号等anything）
                       4,退出此账号
                       5,注销
                        '''
            # msg = input('输入：')
            print(client_main_menus)
            client_main_choice = input('请输入你的选择（1-5）:').strip()
            import socket
            sk = socket.socket()
            # self.sk = sk
            sk.connect((QQ_IP, 8080))

            print('开始运行客户端了')
            msg = input('输入:').strip()
            # tcp_client.sendto(client_main_choice.encode('utf-8'), ip_port)
            print('已经发送消息给服务端了')
            sk.send(client_main_choice.encode('utf-8'))
            print('已经发送')
            data = sk.recv(1024)
            print(data.decode('utf-8'))
            if client_main_choice==str(0):
                sk.send(str(0).encode('utf-8'))
                message_thread()
            elif client_main_choice == str(1):
                sk.send(str(1).encode('utf-8'))
                look_friend()
            elif client_main_choice == str(2):
                personal_information()
            elif client_main_choice == str(3):
                sk.send(str(3).encode('utf-8'))
                user_search()
            elif client_main_choice == str(4):
                print('退出普通用户登录端..........')
                exit()
            elif client_main_choice == str(5):
                sk.send(str(5).encode('utf-8'))
                data = sk.recv(1024)
            elif client_main_choice == '':
                print('没有输入')
            else:
                print('输入有误')
        except Exception as e:
            print(e)




####################################################菜单选项###############################################################################
    def message_thread():
        print('开启message线程页面.......................................................')
        from  nomal_user import  self_user_main_wechat
        self_user_main_wechat.normal_user_message()

    def look_friend(self):
        from  nomal_user import existed_friend
        existed_friend.look_existed_friend()

        # print('进入查看你的好友界面')

    def personal_information(self):
        from  nomal_user import personal_information
        # print('进入个人账户信息页面')
        personal_information.personal_information()

    def user_search(self):
        from  nomal_user import user_search
        user_search.search()



# normal_user_main()
#######################开了多个线程,实现并发操作#########################################


other_thread=threading.Thread(target=normal_user_main.start,)
# look_friend_thread=threading.Thread(target=normal_user_main.look_friend,)
# user_search_thread=threading.Thread(target=normal_user_main.user_search,)
# personal_information_thread=threading.Thread(target=normal_user_main.personal_information,)
message_thread=threading.Thread(target=normal_user_main.message_thread,)
    # i=threading.Thread(target=FTPconnect,args=(key,value,))
message_thread.setDaemon(True)
# look_friend_thread.setDaemon(True)
# user_search_thread.setDaemon(True)
# personal_information_thread.setDaemon(True)




###########守护主线程###################################################

message_thread.start()
other_thread.start()

print('ending................。。。。')








