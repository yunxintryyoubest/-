
#########

import json
import time
import random
# f_open = open('QQ_ID.txt', 'r')
# all_dic_data = json.loads(f_open.read())
# Dicyionary = all_dic_data
# print('执行')
# Dicyionary=[]
import json
# fh=open('exist_users_QQ.txt','r')
# Dicyionary=fh.read()
# print(Dicyionary)
# print(type(Dicyionary))
# Dicyionary=dict(Dicyionary)
# Dicyionary=[{62000301709,123}]
# Dicyionary.append({1:2})
# Dicyionary.__add__()

# Dicyionary=[]
# Dicyionary.append({19306918606: '1212'})
# Dicyionary.append({11111111111: '123'})
#
# with open('exist_users_QQ.txt', 'w')as f:
#     f.write(str(Dicyionary))
#     f.close()

# Dicyionary=[]
# Dicyionary.append({68857394205: '192.168.49.49'})
# with open('QQ_ID_IP_save.txt', 'w')as f:
#     f.write(str(Dicyionary))
#     f.close()




#
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


##############################测试这个用户匹配不重复的ip###########################################################

################################这里可以配置全部的ip地址##############################################################################
#
# import  demjson
# import time
# time.sleep(3)
# print('#'*100)
# print('欢迎来到server端。。。。。。。。。。。。。。。。。。')
# QQ_ID_IP_read = open('QQ_ID_IP_save.txt' , 'r')
# QQ_ID_IP_read=QQ_ID_IP_read.read()
# print('这个字典的全部ip是',QQ_ID_IP_read)
# print(type(QQ_ID_IP_read))
# #
# # demjson.decode(QQ_ID_IP_read)
# #
# #
# # print('这个转化后的类型是',type(QQ_ID_IP_read))
# # print('全部的QQ号码对应的ip地址是',QQ_ID_IP_read)
# import  os,sys
# PATH=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# # PATH= os.path.abspath(os.path.dirname(__file__))
# ##########################这个是当前的绝对路径
# sys.path.append(PATH)
# import json
# import random
#
# class all_server:
#     # while True:
#     print('进入全部的server端')
#     print('每一个用户分配一个ip')
#     last_ip = int(random.randrange(100))
#
#     print(last_ip)
#     seconde_last_ip = int(random.randrange(100))
#     print(seconde_last_ip)
#     ip_addr='192.168.{}.{}'.format(seconde_last_ip,last_ip)
#     print(ip_addr)
#     f_open = open('QQ_ID.txt', 'r')
#     all_dic_data = json.loads(f_open.read())
#     print(all_dic_data)
#     QQ_ID = all_dic_data[-1]
#     print('QQ_ID是',QQ_ID)
#     # print(Dicyionary.last())
#     QQ_dic={}
#     QQ_dic[QQ_ID]=ip_addr
#     print(QQ_dic)
#         # ##############拿到用户和ip地址,每一个用户都分配一个ip地址
#     QQ_ID_IP_read=demjson.decode(QQ_ID_IP_read)
#     #####################################demjson会转化为就可以导入这个字典里面对象，
#     QQ_ID_IP_read.append(QQ_dic)
#
#
#     QQ_ID_IP_save=open('QQ_ID_IP_save.txt','w')
#
#     QQ_ID_IP_save.write(str(QQ_ID_IP_read))
#     QQ_ID_IP_save.close()
#     print('保存成功')
#     # print(QQ_dic)
#
#
#
#     # if QQ_ID in
#
#
#
#
#
# all_server()
#
#
#
#




print('进入到多用户高并发环节......................................................')

import os, sys

PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(PATH)
f = open('login_QQ_ID.txt', 'r')
data = f.read()
f.close()
import demjson

data = demjson.decode(data)
print('这个已经上线的用户是:', data)
all_QQ = []
for i in range(0, len(data)):
    (key, value), = data[i].items()
    print('运行')
    print('........................................................')
    if value in all_QQ:
        print('已经存在此用户，不需要在存入')
        continue
    else:
        print('不存在，写入进去')
        all_QQ_dic = {}
        all_QQ_dic[key] = value
        all_QQ.append(all_QQ_dic)
    print('这个用户对应的ip地址是：', data[i])

print(all_QQ)
print('全部的用户ip已经上线的QQ用户')

import threading
import time
import socket
import selectors
import time


# 一直监听有没有客户进来
class multi_user():
    def __init__(self, QQ_ID, QQ_IP):
        self.QQ_ID = QQ_ID
        self.QQ_IP = QQ_IP
        print('开始时间是%s' % time.ctime())
        print('hello %s' % QQ_ID)
        self.dic = []
        self.rel = selectors.DefaultSelector()
        self.create_socket()
        self.handler()

    def create_socket(self):
        self.sock = socket.socket()
        print('正在请求连接的用户是:', self.QQ_ID)
        print('这个正在请求连接的ip是', self.QQ_IP)
        self.sock.bind((self.QQ_IP, 8080))
        self.sock.listen(100)
        self.sock.setblocking(True)
        # self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.rel.register(self.sock, selectors.EVENT_READ, self.accept)
        print('创建多用户socket成功.........................................................')

    def handler(self):
        while True:
            try:
                #     while True:
                print('开始监听有没有用户进来......')
                print('[%s]用户已经连接进来' % self.QQ_ID)
                # self.rel.register(self.sock,selectors.EVENT_READ,self.accept)
                events = self.rel.select()
                for key, mask in events:
                    callback = key.data
                    callback(key.fileobj)  # 开始执行accept函数了
            except Exception as e:
                print(e)
                #     callback

                # 当有用户进来时，建立连接

    def accept(self, sock):
        try:
            print('有新用户进来，开始建立链接了')
            conn, addr = self.sock.accept()
            print(conn)
            # self.dic[conn] = {}
            self.dic.append(conn)
            # print(self.dic)
            # print('与用户%s建立通信'%self.dic.index(conn))
            print('与用户%s建立通信' % self.QQ_ID)
            self.sock.setblocking(True)
            # self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.rel.register(conn, selectors.EVENT_READ, self.read)
        except Exception as e:
            print(e)



            # 与用户进行通信循环

    def read(self, conn):
        try:
            data = conn.recv(1024)
            print(data.decode('utf-8'))
            if data:
                # while True:
                print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>注明一下，这个是已经进来的用户..........................')
                # self.dic.append(conn)
                #     print('与用户%s建立通信' % self.dic.index(conn))
                #     print('与用户%s建立通信' % key)

                # '''
                #                           0:查看消息
                #                           1,查看你的好友（在线，离线）
                #                           2,个人账户信息
                #                           3,搜索（个人，群，公众号等anything）
                #                           4,加好友
                #                           5,退出此账号
                #                           6,注销
                #                            '''
                #    print('已经接收到QQ用户%s的数据：%s' %(key,(data.decode('UTF-8'))))
                # print('已经接收到QQ用户%s的数据：%s' % (key, data))
                # msg = input('输入:')
                # conn.send(msg.encode('utf-8'))
                # # print('发送数据给%s'%self.dic.index(conn))
                # print('发送数据给%s' % key)

                #######################################################判断这个接收到的数据##################################################################
                data = data.decode('UTF-8')
                # print(type(data))
                # print(str(4))
                # print(type(str(4)))
                if data == str(0):

                    print('选择了查看消息的功能')
                elif data == str(1):
                    print('选择了查看你的好友（在线，离线）的功能')
                    exist_frineds = conn.recv(1024).decode('utf-8')
                    print('接收到全部的好友:', exist_frineds)
                    with open('login_QQ_ID.txt', 'r')as fr:
                        all_login_QQ = fr.read()
                        fr.close()
                    print('全部已经上线的QQ是:', all_login_QQ)
                    print(type(all_login_QQ))
                    import demjson
                    exist_frined = demjson.decode(exist_frineds)
                    login_QQ_ID = str(all_login_QQ)
                    import re
                    print(type(all_login_QQ))
                    send_login_QQ_ID = []
                    for i in range(0, len(exist_frined)):
                        print(exist_frined[i])
                        print(type(login_QQ_ID))
                        result = re.compile(exist_frined[i]).findall(login_QQ_ID)
                        if result:
                            send_login_QQ_ID.append(result)
                    print(send_login_QQ_ID)
                    conn.send(str(send_login_QQ_ID).encode('utf-8'))
                    print('已经发送上线的好友出去')
                    #####################################做选择，对好友菜单选项选择################################
                    friend_choice = conn.recv(1024).decode('utf-8')
                    print(friend_choice)
                    print('接收到')
                    print('所有上线的QQ用户:  ', all_login_QQ)
                    with open('login_QQ_ID.txt', 'r')as fr:
                        reve_chat_QQ_id = fr.read()
                        fr.close()
                    print(reve_chat_QQ_id)
                    ###################################如果要请求连接的QQ号码是离线的话，就保存到数据库里面
                    print(type(reve_chat_QQ_id))
                    print('去找有没有这个在线的好友')
                    reve_chat_QQ_id = demjson.decode(reve_chat_QQ_id)
                    all_login_QQ = []
                    for i in range(0, len(reve_chat_QQ_id)):
                        (recv_id, recv_ip), = reve_chat_QQ_id[i].items()
                        all_login_QQ.append(recv_id)
                        if str(friend_choice) == str(recv_id):
                            print('已经找到')
                            remove_QQ_login = {}
                            remove_QQ_login[friend_choice] = recv_ip
                            import os

                            print('当前路径是:', PATH)
                            if not os.path.exists('{}/wechat_recode/{} '.format(PATH, self.QQ_ID)):
                                print('不存在这个路径，要新建这个用户的数据库')
                                os.mkdir('{}/wechat_recode/{}'.format(PATH, self.QQ_ID))
                                break
                            print('执行文件这步')
                            chat_recode = '{}'.format(recv_id) + ' chat_recode'
                            print(chat_recode)
                            f = open(
                                '{}/wechat_recode/{}/{}  wechat_recode.txt'.format(PATH, self.QQ_ID, friend_choice),
                                'w')
                            #####################################创建完成
                            recode = '{}  and {}wechat recode list:'.format(self.QQ_ID, friend_choice).encode('utf-8')
                            f.write(str(recode))
                            f.close()
                            print('success')
                            QQ_IP_chat = open('QQ_IP_CHAT.txt', 'w')
                            QQ_IP_chat.write(recv_ip)
                            print('保存对应的聊天记录成功...........................................')
                            ################当选择某个好友聊天的时候，就切换到了一个页面，login_QQ_ID移除这个要选择的好友（在线）
                            print('跳转到相应的聊天好友页面')

                            #############################当最外面的下线之后，就清除这个上线记录,拿到之前存在的上线记录
                            with open('login_QQ_ID.txt', 'r')as f:
                                exist_data = f.read()
                                f.close()
                            import demjson
                            remove_data = demjson.decode(exist_data)
                            print('要移除的好友QQ用户:', remove_QQ_login)
                            print('已经存在的全部的好友:',remove_data)
                            print(type(remove_data))
                            print(type(remove_QQ_login))
                            for i in range(0,len(remove_data)):
                                (key,value),=remove_data[i].items()
                                if str(key)==str(friend_choice):
                                    print('已经找到')
                                    remove_data.remove(remove_data[i])
                                    fr = open('login_QQ_ID.txt', 'w')
                                    fr.write(str(remove_data))
                                    fr.close()
                                    print('移除成功，这个选择要聊天的好友')
                                    from  wechat_server_manage import test
                                    test.test()
                                    break
                                else:
                                    continue




                            ####################################移除成功后在再来一个地方开启一个线程单独处理，实际这个是正在要选择的聊天的好友
                            # from  wechat_server_manage import mult_chat_handler_manage
                            # mult_chat_handler_manage.multi_user_chat()

                            break
                            # mult_chat_server_manage.multi_user_chat()
                            # print(recv_ip)
                        else:
                            continue
                    else:
                        #########################不在线的情况
                        print('不在线')








                elif data == str(2):
                    print('个人账户信息')
                elif data == str(3):
                    print('个人账户信息')
                elif data == str(4):
                    try:
                        print('加好友')
                        add_number = conn.recv(1024).decode('utf-8')
                        print('接收到这个数据:', add_number)
                        with open('QQ_ID.txt', 'r')as f:
                            import json
                            exist_QQ = json.loads(f.read())
                            f.close()
                            print('已经存在的QQ是：', exist_QQ)
                        for i in range(0, len(exist_QQ)):
                            if str(add_number) == str(exist_QQ[i]):
                                print('存在这个QQ')
                                msg = '是否添加此好友(y/n)?'
                                conn.send(msg.encode('utf-8'))
                                print('发送')
                                data = conn.recv(1024).decode('utf-8')
                                print(data)
                                import json
                                import demjson
                                import json
                                add_number = int(add_number)
                                print(type(add_number))
                                with open('QQ_ID_IP_save.txt', 'r')as f:
                                    add_QQ_ID_information = f.read()
                                    f.close()
                                #####################拿到对应的ip和QQ信息
                                dic = {}
                                add_QQ_ID_information = demjson.decode(add_QQ_ID_information)
                                for i in range(0, len(add_QQ_ID_information)):
                                    (key1, value1), = add_QQ_ID_information[i].items()
                                    if add_number in add_QQ_ID_information[i]:
                                        print('已经找到')
                                        print(add_QQ_ID_information[i])
                                        dic = add_QQ_ID_information[i]
                                        add_QQ_ID_information_data = add_QQ_ID_information[i]
                                    else:
                                        print('fail')
                                        continue
                                print(dic)
                                conn.send(str(dic).encode('utf-8'))  #####发送添加的好友############################
                            else:
                                continue
                        else:
                            msg = '不存在'
                            conn.send(msg.encode('utf-8'))

                    except Exception as e:
                        print('里面一层掉线')
                        print(e)
                        ##3469509180
            else:
                print('错误')
        except Exception as e:
            print(e)
            # print('有用户下线')
            # print('这个下线的QQ是：', self.QQ_ID)
            # remove_QQ_login = {}
            # remove_QQ_login[self.QQ_ID] = self.QQ_IP
            # #############################当最外面的下线之后，就清除这个上线记录,拿到之前存在的上线记录
            # with open('login_QQ_ID.txt', 'r')as f:
            #     exist_data = f.read()
            #     f.close()
            # import demjson
            # remove_data = demjson.decode(exist_data)
            # print('要移除的QQ用户:', remove_QQ_login)
            # # print('全部已经上线的用户是：', remove_data)
            # def remove_QQ_login_ID():
            #     print('这个下线的QQ是：', self.QQ_ID)
            #     remove_data.remove(remove_QQ_login)
            #     fr = open('login_QQ_ID.txt', 'w')
            #     fr.write(str(remove_data))
            #     fr.close()
            #     print('移除成功，这个掉线的用户')
            # for i in  range(0,len(remove_data)):
            #     if remove_QQ_login == remove_data[i]:
            #         remove_QQ_login_ID()
            #     else:
            #         continue
            # else:
            #     print('下线的QQ用户{}已经移除'.format(self.QQ_ID))
            #     print(e)
            ###############################################################################################################################################################

            # if __name__ == '__main__':
            #     FTPconnect()



            # print('结束时间是%s'%time.ctime())
            # print(t2.isAlive())


thread = []
t = []
for i in range(0, len(all_QQ)):
    # (key,value),=all_QQ.items()
    (key, value), = all_QQ[i].items()
    print('这个当前用户ip是:', value)
    print('这个当前用户是:', key)
    # current_QQ_IP=
    # print(current_QQ_ID)
    # t1=threading.Thread(target=hi,args=(3,))
    i = threading.Thread(target=multi_user, args=(key, value,))
    thread.append(i)
for j in thread:
    j.start()
print('ending................。。。。')













