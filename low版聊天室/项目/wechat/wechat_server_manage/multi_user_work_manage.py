# ##########################################################这里有多个用户在此运行########################################################
#
#
# #########################################################多线程运行多个用户######################################################################
#
# ############从这个数据库里面去这个相对应的ip
# class multi_user:
#     def __init__(self):
#         print('#' * 200)
#         print('正打开这个多用户环节..............................')
#         # self.take_ip()
#         # self.QQ_IP_login()
#         print('已经进入此服务器的多用户环节............................................................')
#     ############################可以拿到这个上线的QQ和对应的ip地址
#
#
#     def take_ip(self):
#         f = open('login_QQ_ID.txt', 'r')
#         data= f.read()
#         f.close()
#         import demjson
#         data=demjson.decode(data)
#         print('这个已经上线的用户是:',data)
#         print(type(data))
#         all_QQ_IP=[]
#         for i in range(0, len(data)):
#             (key, value), = data[i].items()
#             ########################这里是对过来的用户进行ip匹配
#             print(value)
#             print(key)
#             if value in all_QQ_IP:
#                 print('已经存在此用户，不需要在存入')
#                 continue
#             else:
#                 print('不存在，写入进去')
#                 all_QQ_IP.append(value)
#             print('这个用户对应的ip地址是：',data[i])
#             # return  value
#
#         print('所有已经上线的QQ用户IP是：',all_QQ_IP)
#         print('，。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。')
#         for ip_addr in all_QQ_IP:
#             print('循环返回这个ip地址')
#             print(ip_addr)
#             # global  ip_addr
#             # return ip_addr
#
#
#         # fh = open('login_QQ_ID.txt', 'r')
#         # data = fh.read()
#         # fh.close()
#         # import demjson
#         # data = demjson.decode(data)
#         # (key, value), = data.items()
#         # print(value)
#         # print('这个对应的ip地址是')
#         # return  value
#
#
#
#     ###########################################进入相应的ip地址###########################################
#     def QQ_IP_login(self):
#         print('执行Myserver函数，请等待..................................')
#         Myserver()
#         # ip_addr=self.take_ip()
#         # print('这个取到的ip地址是:',ip_addr)
#         #################拿到相对应的ip地址
#
#
# #########################################每进来一个用户，就进行通信
#     def create_QQ_ID_thread(self):
#         print('开始监听用户进来，就开一个线程')
#         ####################################取已经登录的用户
#         ##############拿到所有已经上线的用户####################################################################################
# multi_user()
#
# ###############################################高并发写入用户进来，在这里进行通信
#
#
# # for i in range(0,)
#
#
#
# # all_QQ_IP=multi_user.take_ip('self')
# # print('拿到所有已经上线的QQ用户')
# # print(all_QQ_IP)
# # print(type(all_QQ_IP))
# # t1 = threading.Thread(target=music)
#
#
#
#
#
#
# f = open('login_QQ_ID.txt', 'r')
# data = f.read()
# f.close()
# import demjson
#
# data = demjson.decode(data)
# print('这个已经上线的用户是:', data)
# print(type(data))
# all_QQ_IP = []
# for i in range(0, len(data)):
#     (key, value), = data[i].items()
#     ########################这里是对过来的用户进行ip匹配
#     print(value)
#     print(key)
#     if value in all_QQ_IP:
#         print('已经存在此用户，不需要在存入')
#         continue
#     else:
#         print('不存在，写入进去')
#         all_QQ_IP.append(value)
#     print('这个用户对应的ip地址是：', data[i])
#
#
# print(all_QQ_IP)
#
#
#
#
#
#
#
#
#
#
#
#
# ###################################################开启多线程通信#####################################
############进行监听#############################################################################################

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
all_QQ=[]
for i in range(0, len(data)):
    (key, value), = data[i].items()
    print('运行')
    print('........................................................')
    if value in all_QQ:
        print('已经存在此用户，不需要在存入')
        continue
    else:
        print('不存在，写入进去')
        all_QQ_dic={}
        all_QQ_dic[key]=value
        all_QQ.append(all_QQ_dic)
    print('这个用户对应的ip地址是：', data[i])


print(all_QQ)
print('全部的用户ip已经上线的QQ用户')




import  threading
import  time
import  socket
import selectors
import  time
#一直监听有没有客户进来
class multi_user():
    print('已经开始执行这个多线程用户work环节了')
    def __init__(self,QQ_ID,QQ_IP):
        self.QQ_ID=QQ_ID
        self.QQ_IP=QQ_IP
        print('开始时间是%s' % time.ctime())
        print('hello %s'%QQ_ID)
        self.dic=[]
        self.rel=selectors.DefaultSelector()
        self.create_socket()
        self.handler()
    def create_socket(self):
        self.sock=socket.socket()
        print('正在请求连接的用户是:',self.QQ_ID)
        print('这个正在请求连接的ip是',self.QQ_IP)
        self.sock.bind((self.QQ_IP,8080))
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
                print('[%s]用户已经连接进来'%self.QQ_ID)
            # self.rel.register(self.sock,selectors.EVENT_READ,self.accept)
                events=self.rel.select()
                for key,mask in events:
                    callback=key.data
                    callback(key.fileobj)#开始执行accept函数了
            except Exception as e:
                print(e)
        #     callback

#当有用户进来时，建立连接
    def accept(self,sock):
        try:
            print('有新用户进来，开始建立链接了')
            conn, addr = self.sock.accept()
            print(conn)
            # self.dic[conn] = {}
            self.dic.append(conn)
            # print(self.dic)
            # print('与用户%s建立通信'%self.dic.index(conn))
            print('与用户%s建立通信'%self.QQ_ID)
            self.sock.setblocking(True)
            # self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.rel.register(conn, selectors.EVENT_READ, self.read)
        except Exception as e:
            print(e)



#与用户进行通信循环
    def read(self,conn):
        try:
            data = conn.recv(1024)
            data = data.decode('UTF-8')

            print(data)
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
                # print(type(data))
                # print(str(4))
                # print(type(str(4)))
                if data == str(0):
                    print('选择了查看消息的功能')
                elif data == str(1):
                    print('选择了查看你的好友（在线，离线）的功能')
                    import demjson
                    open('self_QQ_main_chat.txt', 'w')
                    with open('self_QQ_main_chat.txt', 'r')as f:
                        self_QQ_ID = f.read()
                        f.close()
                    if len(self_QQ_ID):
                        print('这里面有用户跳到主页面了')
                        self_QQ_ID = demjson.decode(self_QQ_ID)
                    else:
                        print('没有用户跳转到主页面')
                        dic = []
                        with open('self_QQ_main_chat.txt', 'w')as f:
                            f.write(str(dic))
                            f.close()
                    with open('self_QQ_main_chat.txt', 'r')as fr:
                        all_main_QQ = fr.read()
                        fr.close()
                    print('>'*100,all_main_QQ)
                    all_main_QQ_ID = demjson.decode(all_main_QQ)
                    from  wechat_server_manage import create_main_chat_ip
                    ip = create_main_chat_ip.has_ip()
                    print(ip)
                    self_dic = {}
                    self_dic[self.QQ_ID] = ip
                    ####################3这个是自己的id和生成的ip地址
                    all_main_QQ_ID.append(self_dic)
                    print('*'*1000)
                    print('这个原来的数据是:',all_main_QQ_ID)
                    with open('self_QQ_main_chat.txt', 'w')as fw:
                        fw.write(str(all_main_QQ_ID))
                        fw.close()
                    print('已经保存这个用户{}进主页面文件里面了（聊天）'.format(self_dic))



                    ##########################################################################
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
                        result = re.compile(str(exist_frined[i])).findall(login_QQ_ID)
                        if result:
                            send_login_QQ_ID.append(result)
                    print(send_login_QQ_ID)
                    conn.send(str(send_login_QQ_ID).encode('utf-8'))
                    print('已经发送上线的好友出去')


                    conn.send(ip.encode('utf-8'))
                    print('已经发送成功')


                    # if not os.path.exists('{}/IP_data'):
                    #     os.mkdir('{}/IP_data')
                    # open('{}/IP_data/main_ip.txt','w')
                    # with open('{}/IP_data/main_ip.txt','r')as fo:
                    #     ip_before=fo.read()
                    #     fo.close()
                    # ip_main_before=demjson.decode(ip_before)
                    # if len(ip_main_before):
                    #     print('有数据')
                    #     dic={}
                    #     dic[]
                    #     ip_main_before.append()
                    # else:
                    #     dic=[]
                    #     with open('{}/IP_data/main_ip.txt', 'w')as f:
                    #         f.write(str(ip))
                    #         f.close()
                    #

                    # with open('{}/IP_data/main_ip.txt','w')as f:
                    #     f.write(str(ip))
                    #     f.close()
                    # print('写入成功')
                    print('跳转页面开始..........................................................')
                    from  wechat_server_manage import wechat_QQ_ID_main_manage
                    wechat_QQ_ID_main_manage.chat_main_manage()
                    # #####################################做选择，对好友菜单选项选择################################
                    # print('所有上线的QQ用户:  ', all_login_QQ)
                    #
                    # with open('login_QQ_ID.txt', 'r')as f:
                    #     exist_data = f.read()
                    #     f.close()
                    # import demjson
                    # remove_data = demjson.decode(exist_data)
                    # print('要移除的自己的QQ:', self.QQ_ID)
                    # print('已经存在的全部的好友:', remove_data)
                    # print(type(remove_data))
                    # print(type(self.QQ_ID))
                    # for i in range(0, len(remove_data)):
                    #     (key, value), = remove_data[i].items()
                    #     if str(key) == str(self.QQ_ID):
                    #         print('已经找到')
                    #         remove_data.remove(remove_data[i])
                    #         fr = open('login_QQ_ID.txt', 'w')
                    #         fr.write(str(remove_data))
                    #         fr.close()
                    #         print('移除成功，自己移除成功，跳转到了一个页面...................................')
                        # else:
                        #     continue
                    # else:
                    #     print('没有找到，不存在这个用户')


                    # print('这个remove_data.......................................')
                    # print('这个remove_data是',remove_data)
                    # remove_data=[{173402236: '127.252.97.71'}, {7405443047: '127.0.255.134'}, {3469509180: '127.249.132.141'}, {9500025787: '127.70.120.9'}]
                    # for j in range(0,len(remove_data)):
                    #     print('重新刷新这个页面')
                    #     (key,value),=remove_data[j].items()
                    #     multi_user(key,value)

                    # print('执行跳转页面的功能')
                    # from  wechat_server_manage import wechat_QQ_ID_main_manage
                    # wechat_QQ_ID_main_manage.chat_main_manage()

                            # def restart_QQ_login_data():
                            #     print('重新刷新这个登录的数据')
                            #     # multi_thread()
                            #     # with open('login_QQ_ID.txt','r')as fr:
                            #     #     fr.write()
                            #     # with open('login_QQ_ID.txt','r')as f:
                            #     #     last_QQ=f.read()
                            #     #     f.close()
                            #     # last_QQ=demjson.decode(last_QQ)
                            #     # print(last_QQ)
                            #     print('开始重新运行这个函数了')
                            #     for i in  range(0,len(last_QQ)):
                            #         (key,value),=all_QQ[i].items()
                            #         print('这个key是：',key)
                            #         print('这个value',value)
                            #         multi_user(key,value)
                            #     else:
                            #         multi_user()
                            # restart_QQ_login_data()

                            # def drop_main_page():
                            #     from  wechat_server_manage import wechat_QQ_ID_main_manage
                            #     wechat_QQ_ID_main_manage.chat_main_manage()
                            # restart = threading.Thread(target=restart_QQ_login_data)
                            # drop_page = threading.Thread(target=drop_main_page)
                            # drop_page.setDaemon(True)#########################守护主线程
                            # restart.start()
                            # time.sleep(1)
                            # drop_page.start()




                            # from  wechat_server_manage import test
                            # test.test()
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
                        for i in range(0,len(exist_QQ)):
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
    # print('结束时间是%s'%time.ctime())
    # print(t2.isAlive())


print('执行下面的多线程')

thread = []
t = []
for i in range(0, len(all_QQ)):
    (key, value), = all_QQ[i].items()
    print('这个当前用户ip是:', value)
    print('这个当前用户是:', key)
    i = threading.Thread(target=multi_user, args=(key, value,))
    # i._stop()
    thread.append(i)
for j in thread:
    j.start()

print('ending................。。。。')

