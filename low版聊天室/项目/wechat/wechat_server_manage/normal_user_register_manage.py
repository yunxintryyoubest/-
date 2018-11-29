####################后台服务端验证环节###################################################
import  json
import time

import  os,sys
PATH=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(PATH)




import socket

import selectors

f_open=open('QQ_ID.txt','r')
# all_dic_data=json.loads(f_open.read())
all_dic_data=f_open.read()
f_open.close()
Dicyionary = all_dic_data
# print(Dicyionary)
import demjson
if all_dic_data:
    Dicyionary = demjson.decode(Dicyionary)
else:
    dic=[]
    f_open=open('QQ_ID.txt','w')
    Dicyionary=f_open.write(str(dic))
    Dicyionary=demjson.decode(Dicyionary)
    f_open.close()




#################这个可以拿到这个是注册的QQ_ID和相对应的密码###########
f=open('exist_users_QQ.txt','r')
exist=f.read()
f.close()
if len(exist):
    f = open('exist_users_QQ.txt', 'r')
    exist_user_data=f.read()
    exist_user_data=demjson.decode(exist_user_data)
    f.close()
else:
    new_Q_ID_PWD=[]
    f = open('exist_users_QQ.txt', 'w')
    f.write(str(new_Q_ID_PWD))
    f.close()
    f = open('exist_users_QQ.txt', 'r')
    exist_user_data = f.read()
    exist_user_data = demjson.decode(exist_user_data)
    f.close()



# f=open('exist_users_QQ.txt','r')
# exist=f.read()
# f.close()
# import demjson
# exist=demjson.decode(exist)
# print('exist是：',exist)
# print(type(exist))
# import demjson
# if exist:
#     # exist_user_data=exist
#     exist_user_data = demjson.decode(exist)
#     print(type(exist_user_data))
# else:
#     new_Q_ID_PWD=[]
#     f = open('exist_users_QQ.txt', 'w')
#     exist_user_data = f.write(str(new_Q_ID_PWD))
#     print(exist_user_data)
#     exist_user_data=demjson.decode(exist_user_data)
#     f.close()








# print(type(exist_all_QQ))
#
# print(exist_all_QQ)
# f_open=open('exist_users_QQ.txt','r')
# exist_all_QQ=json.loads(f_open.read())
# print(exist_all_QQ)

# print('已经启动后台服务端环节.........................')
#
#
# fh=open('login_QQ_ID.txt','r')
# data_login=fh.read()
# fh.close()
#
# if data_login:
#     data_login = demjson.decode(data_login)
# else:
#     login_QQ = []
#     fl = open('login_QQ_ID.txt', 'w')
#     fl.write(str(login_QQ))
#     fl.close()
#     fh = open('login_QQ_ID.txt', 'r')
#     data_login = fh.read()
#     fh.close()
#     data_login = demjson.decode(data_login)
#
#
# class normal_register_manage:
#     print('进入后台验证环节..........................................')
#     import socket
#     import selectors
#     import time
#     # 一直监听有没有客户进来
#     class FTPconnect():
#         def __init__(self):
#             self.dic = []
#             self.rel = selectors.DefaultSelector()
#             self.create_socket()
#             self.handler()
#
#         def create_socket(self):
#             self.sock = socket.socket()
#             self.sock.bind(('127.1.1.2', 8080))
#             self.sock.listen(100)
#             self.sock.setblocking(False)
#             self.rel.register(self.sock, selectors.EVENT_READ, self.accept)
#             print('创建socket成功')
#
#         def handler(self):
#             while True:
#                 try:
#                     #     while True:
#                     print('开始监听有没有用户进来......')
#                     # self.rel.register(self.sock,selectors.EVENT_READ,self.accept)
#                     events = self.rel.select()
#                     for key, mask in events:
#                         callback = key.data
#                         callback(key.fileobj)  # 开始执行accept函数了
#                 except Exception as e:
#                     # normal_register_manage()
#                     break
#                     # print(e)
#                     #     callback
#
#                     # 当有用户进来时，建立连接
#
#         def accept(self, sock):
#             try:
#                 print('执行后端验证环节..........................................................')
#                 conn, addr = self.sock.accept()
#                 print(conn)
#                 # self.dic[conn] = {}
#                 self.dic.append(conn)
#                 # print(self.dic)
#                 # print('与用户%s建立通信'%self.dic.index(conn))
#                 self.sock.setblocking(False)
#                 self.rel.register(conn, selectors.EVENT_READ, self.read)
#             except Exception as e:
#                 print(e)
#
#
#
#                 # 与用户进行通信循环
# ##############################################################################################################################################
#         def read(self, conn):
#             try:
#                 auth_user_data = {}
#                 data = conn.recv(1024)
#                 data = data.decode('utf-8')
#                 if data=='iq_request':
#                     # ###############分配QQ号码的过程###############################
#                     ##########################################存放的是QQ号码和QQ对应的Ip地址#######################################
#                     QQ_ID_IP_read1 = open('QQ_ID_IP_save.txt', 'r')
#                     QQ_ID_IP_read = QQ_ID_IP_read1.read()
#                     print('这个字典的全部ip是', QQ_ID_IP_read)
#                     QQ_ID_IP_read1.close()
#                     print('号路ip地址中')
#                     import demjson
#                     QQ_ID_IP_read = demjson.decode((QQ_ID_IP_read))
#                     print(type(QQ_ID_IP_read))
#
#                     import random
#                     print('接收到了请求ip的请求了')
#
#                     class all_server:
#                         def __init__(self):
#                             print('开始分配相对应的ip地址了')
#                             print('进入全部的server端')
#                             self.QQ_ID_IP_create()
#                             # self.ip_addr=ip_addr
#                             # self.create_ip()
#                             # self.has_ip()
#
#                         ##################拿到所有的QQ和对应的ip地址
#                         ###########################################这里生成了个ip地址的
#                         def create_ip(self):
#                             print('生成ip地址。。。。。。。。。。。。。。。。。。。。。。。')
#                             # ip_addr='192.168.2.55'
#
#                             last_ip = int(random.randrange(256))
#                             print(last_ip)
#                             seconde_last_ip = int(random.randrange(256))
#                             print(seconde_last_ip)
#                             third_last_ip = int(random.randrange(255))
#                             print(third_last_ip)
#                             ip_addr = '127.{}.{}.{}'.format(third_last_ip, seconde_last_ip, last_ip)
#                             print('这个生成的ip地址是：', ip_addr)
#                             ##################执行此步骤，看看这个ip地址是否重复#########################################
#                             return ip_addr
#                             ########################这个可以返回到init函数里面，这个retrun ip_addr，默认是返回到init函数里面####################
#
#
#                             ########################拿到已经存在的ip地址，去重
#                             #####################拿到已经存在的ip地址
#
#                         def has_ip(self):
#                             ip_addr = self.create_ip()
#                             exist_ip = open('QQ_ID_IP_save.txt', 'r')
#                             existed_ip = exist_ip.read()
#                             exist_ip.close()
#                             existed_ip = demjson.decode(existed_ip)
#                             print('全部的ip地址是：', existed_ip)
#                             print(type(existed_ip))
#                             existip = []
#                             for i in range(0, len(existed_ip)):
#                                 (key, value), = existed_ip[i].items()
#                                 existip.append(value)
#                                 # if ip_addr ==value:
#                                 #     print('已经存在这个ip')
#                             if ip_addr in existip:
#                                 print('已经存在这个ip')
#
#
#                             else:
#                                 print('这个ip不存在，no one is usering ')
#                                 return ip_addr
#
#
#
#
#
#
#                                 # return  ip_addr
#
#                         ####################################这里判断这个数据库里面有没有这个QQ用户
#
#                         def QQ_ID_IP_create(self):
#                             print('运行生成ip的函数...........................................................')
#                             print('此用户没有分配ip地址')
#                             ########################################只生成一个ip地址就好了#########################
#                             QQ_new_IP = self.has_ip()
#                             print('生成的ip地址是:', QQ_new_IP)
#                             if QQ_new_IP == None:
#                                 print('没有生成ip直接返回')
#                             else:
#                                 print('已经执行creat_ip的函数了')
#                                 QQ_dic = {}
#                                 QQ_dic[ID] = QQ_new_IP
#                                 print(QQ_dic)
#
#                                 QQ_ID_IP_read.append(QQ_dic)
#                                 ###############################################保存这个用户和对应的ip到数据库里面
#                                 QQ_ID_IP_save = open('QQ_ID_IP_save.txt', 'w')
#                                 QQ_ID_IP_save.write(str(QQ_ID_IP_read))
#                                 QQ_ID_IP_save.close()
#                                 print('保存成功')
#                                 ip_addr = QQ_dic[ID]
#                                 print(ip_addr)
#                                 ip_request = conn.recv(1024)
#                                 # if ip_request == 'iq_request':
#                                 #     print('已经接收到请求了')
#                                 msg = ip_addr
#                                 conn.send(msg.encode('utf-8'))
#                                 QQ_ID_DIC = []
#                                 QQ_ID_DIC[ID] = ip_addr
#                                 # data.append(QQ_ID_DIC)
#                                 login_QQ.append(QQ_ID_DIC)
#                                 ##################3跳到了一个页面#############################################
#                                 f = open('login_QQ_ID' + '.txt', 'w')
#                                 f.write(str(login_QQ))
#                                 f.close()
#                                 print('这个ip地址已经登录成功...............................')
#                                 #################################写入login_QQ_ID里面去
#                                 ############发送对应的ip地址到注册页面######################################
#                                 # conn.send(msg.encode('utf-8'))
#                                 from  wechat_server_manage import multi_user_work_manage
#                                 multi_user_work_manage.multi_user()
#
#                     all_server()
#                 else:
#                     print('接收到数据（手机号码和密码）是', data)
#                     import json
#                     if data:
#                         # self.dic.append(conn)
#                         print('用户%s连接进来了' % self.dic.index(conn))
#                         print('分配QQ号给用户.....................................................')
#
#                         # print('已经接收到%s的数据%s' %((self.dic.index(conn)),(data.decode('UTF-8'))))
#                         import json
#                         import time
#                         import random
#                         import demjson
#                         data = demjson.decode(data)
#                         (phone_number, QQ_IP_PWD), = data.items()
#
#                         class test:
#                             def __init__(self):
#                                 # self.QQ_num=QQ_num
#                                 self.run()
#
#                             def run_randoom_QQ_ID(self):
#                                 QQ_ID = random.randrange(10000000000)
#                                 return QQ_ID
#
#                             def run(self):
#                                 print('执行test验证')
#                                 ID = self.run_randoom_QQ_ID()
#                                 # print(ID)
#                                 if ID not in Dicyionary:
#                                     print('没有分配的QQ号码')
#                                     # print(ID)
#                                     Dicyionary.append(ID)
#                                     with open('QQ_ID.txt', 'w')as f:
#                                         f.write(str(Dicyionary))
#                                         f.close()
#                                 else:
#                                     print('已经分配这个QQ号码')
#                                     self.run()
#                                     print('已经重新分配这个QQ号码')
#                                 print(ID)
#                                 global  ID
#                                 register_QQ_ID = {}
#
#                                 register_QQ_ID[ID] = QQ_IP_PWD
#                                 exist_user_data.append(register_QQ_ID)
#                                 ##########################生成QQ_ID和密码的数据库#####
#                                 with open('exist_users_QQ.txt', 'w')as f:
#                                     f.write(str(exist_user_data))
#                                     f.close()
#                                     #####保存成功
#                                 conn.send(str(ID).encode('utf-8'))
#                         print('发送数据给%s用户' % self.dic.index(conn))
#                     ################分配一个ip给这个用户ID
#                         test()
#             except Exception as e:
#                 print(e)
#             return True
#
#
#     if __name__ == '__main__':
#         FTPconnect()
print('已经启动后台服务端环节.........................')
import demjson
fh = open('login_QQ_ID.txt', 'r')
data_login = fh.read()
fh.close()
# data_login=demjson.decode(data_login)
if len(data_login):
    data_login = demjson.decode(data_login)
else:
    login_QQ = []
    fl = open('login_QQ_ID.txt', 'w')
    fl.write(str(login_QQ))
    fl.close()
    fh = open('login_QQ_ID.txt', 'r')
    data_login = fh.read()
    data_login = demjson.decode(data_login)
    fh.close()
class normal_register_manage:

    print('进入后台验证环节..........................................')
    import socket
    import selectors
    import time
    # 一直监听有没有客户进来
    class FTPconnect():
        def __init__(self):
            self.dic = []
            self.rel = selectors.DefaultSelector()
            self.create_socket()
            self.handler()

        def create_socket(self):
            self.sock = socket.socket()
            self.sock.bind(('127.0.0.1', 8080))
            self.sock.listen(100)
            self.sock.setblocking(False)
            self.rel.register(self.sock, selectors.EVENT_READ, self.accept)
            print('创建socket成功')

        def handler(self):
            while True:
                try:
                    #     while True:
                    print('开始监听有没有用户进来......')
                    # self.rel.register(self.sock,selectors.EVENT_READ,self.accept)
                    events = self.rel.select()
                    for key, mask in events:
                        callback = key.data
                        callback(key.fileobj)  # 开始执行accept函数了
                except Exception as e:
                    # normal_register_manage()
                    break
                    # print(e)
                    #     callback

                    # 当有用户进来时，建立连接

        def accept(self, sock):
            try:
                print('执行后端验证环节..........................................................')
                conn, addr = self.sock.accept()
                print(conn)
                # self.dic[conn] = {}
                self.dic.append(conn)
                # print(self.dic)
                # print('与用户%s建立通信'%self.dic.index(conn))
                self.sock.setblocking(False)
                self.rel.register(conn, selectors.EVENT_READ, self.read)
            except Exception as e:
                print(e)



                # 与用户进行通信循环
                ##############################################################################################################################################

        def read(self, conn):
            try:
                auth_user_data = {}
                data = conn.recv(1024)
                data = data.decode('utf-8')
                print('接收到数据（手机号码和密码）是', data)
                import json
                if data:
                    # self.dic.append(conn)
                    print('用户%s连接进来了' % self.dic.index(conn))
                    print('分配QQ号给用户.....................................................')

                    # print('已经接收到%s的数据%s' %((self.dic.index(conn)),(data.decode('UTF-8'))))
                    import json
                    import time
                    import random
                    import demjson
                    data = demjson.decode(data)
                    (phone_number, QQ_IP_PWD), = data.items()

                    class test:
                        def __init__(self):
                            # self.QQ_num=QQ_num
                            self.run()

                        def run_randoom_QQ_ID(self):
                            QQ_ID = random.randrange(10000000000)
                            return QQ_ID

                        def run(self):
                            print('执行test验证')
                            ID = self.run_randoom_QQ_ID()
                            # print(ID)
                            if str(ID) not in Dicyionary:
                                print('没有分配的QQ号码')
                                # print(ID)
                                Dicyionary.append(ID)
                                with open('QQ_ID.txt', 'w')as f:
                                    f.write(str(Dicyionary))
                                    f.close()
                            else:
                                print('已经分配这个QQ号码')
                                self.run()
                                print('已经重新分配这个QQ号码')
                            print(ID)

                            # global ID
                            register_QQ_ID = {}

                            register_QQ_ID[ID] = QQ_IP_PWD
                            exist_user_data.append(register_QQ_ID)
                            ##########################生成QQ_ID和密码的数据库#####
                            with open('exist_users_QQ.txt', 'w')as f:
                                f.write(str(exist_user_data))
                                f.close()
                                #####保存成功
                            conn.send(str(ID).encode('utf-8'))
                            QQ_ID_IP_read1 = open('QQ_ID_IP_save.txt', 'r')
                            QQ_ID_IP_read3 = QQ_ID_IP_read1.read()
                            print('这个字典的全部ip是', QQ_ID_IP_read3)
                            QQ_ID_IP_read1.close()
                            print('号路ip地址中')
                            if QQ_ID_IP_read3:
                                QQ_ID_IP_read = demjson.decode((QQ_ID_IP_read3))
                                print(type(QQ_ID_IP_read))
                            else:
                                QQ_ID_IP_dic=[]
                                QQ_ID_IP_read2 = open('QQ_ID_IP_save.txt', 'w')
                                QQ_ID_IP_read = QQ_ID_IP_read2.write(str(QQ_ID_IP_dic))
                                QQ_ID_IP_read2.close()
                                print(type(QQ_ID_IP_read))
                                QQ_ID_IP_read=demjson.decode(QQ_ID_IP_read)

                            import random
                            print('接收到了请求ip的请求了')

                            class all_server:
                                def __init__(self):
                                    print('开始分配相对应的ip地址了')
                                    print('进入全部的server端')
                                    self.QQ_ID_IP_create()
                                    # self.ip_addr=ip_addr
                                    # self.create_ip()
                                    # self.has_ip()

                                ##################拿到所有的QQ和对应的ip地址
                                ###########################################这里生成了个ip地址的
                                def create_ip(self):
                                    print('生成ip地址。。。。。。。。。。。。。。。。。。。。。。。')
                                    # ip_addr='192.168.2.55'

                                    last_ip = int(random.randrange(256))
                                    print(last_ip)
                                    seconde_last_ip = int(random.randrange(256))
                                    print(seconde_last_ip)
                                    third_last_ip = int(random.randrange(255))
                                    print(third_last_ip)
                                    ip_addr = '127.{}.{}.{}'.format(third_last_ip, seconde_last_ip, last_ip)
                                    print('这个生成的ip地址是：', ip_addr)
                                    ##################执行此步骤，看看这个ip地址是否重复#########################################
                                    return ip_addr
                                    ########################这个可以返回到init函数里面，这个retrun ip_addr，默认是返回到init函数里面####################


                                    ########################拿到已经存在的ip地址，去重
                                    #####################拿到已经存在的ip地址

                                def has_ip(self):
                                    ip_addr = self.create_ip()
                                    exist_ip = open('QQ_ID_IP_save.txt', 'r')
                                    existed_ip = exist_ip.read()
                                    exist_ip.close()
                                    existed_ip = demjson.decode(existed_ip)
                                    print('全部的ip地址是：', existed_ip)
                                    print(type(existed_ip))
                                    existip = []
                                    for i in range(0, len(existed_ip)):
                                        (key, value), = existed_ip[i].items()
                                        existip.append(value)
                                        # if ip_addr ==value:
                                        #     print('已经存在这个ip')
                                    if ip_addr in existip:
                                        print('已经存在这个ip')


                                    else:
                                        print('这个ip不存在，no one is usering ')
                                        return ip_addr






                                        # return  ip_addr

                                ####################################这里判断这个数据库里面有没有这个QQ用户

                                def QQ_ID_IP_create(self):
                                    print( '运行生成ip的函数...........................................................')
                                    print('此用户没有分配ip地址')
                                    ########################################只生成一个ip地址就好了#########################
                                    QQ_new_IP = self.has_ip()
                                    print('生成的ip地址是:', QQ_new_IP)
                                    if QQ_new_IP == None:
                                        print('没有生成ip直接返回')
                                    else:
                                        print('已经执行creat_ip的函数了')
                                        QQ_dic = {}
                                        QQ_dic[ID] = QQ_new_IP
                                        print(QQ_dic)
                                        QQ_ID_IP_read.append(QQ_dic)
                                        ###############################################保存这个用户和对应的ip到数据库里面
                                        QQ_ID_IP_save = open('QQ_ID_IP_save.txt', 'w')
                                        QQ_ID_IP_save.write(str(QQ_ID_IP_read))
                                        QQ_ID_IP_save.close()
                                        print('保存成功')
                                        ip_addr = QQ_dic[ID]
                                        print(ip_addr)
                                        ip_request = conn.recv(1024)
                                        # if ip_request == 'iq_request':
                                        #     print('已经接收到请求了')
                                        msg = ip_addr
                                        conn.send(msg.encode('utf-8'))
                                        QQ_ID_DIC = {}
                                        QQ_ID_DIC[ID] = ip_addr
                                        # data.append(QQ_ID_DIC)
                                        data_login.append(QQ_ID_DIC)
                                        print(QQ_ID_DIC)
                                        print('已经登录成功')
                                        # from  wechat_server_manage import server
                                        # server.all_server()
                                        ##################3跳到了一个页面#############################################
                                        f = open('login_QQ_ID' + '.txt', 'w')
                                        f.write(str(data_login))
                                        f.close()
                                        print('这个ip地址已经登录成功...............................')
                                        #################################写入login_QQ_ID里面去
                                        ############发送对应的ip地址到注册页面######################################
                                        # conn.send(msg.encode('utf-8'))
                                        from  wechat_server_manage import multi_user_work_manage
                                        multi_user_work_manage.multi_user()

                            all_server()

                    print('发送数据给%s用户' % self.dic.index(conn))
                    ################分配一个ip给这个用户ID
                    test()
            except Exception as e:
                print(e)
                # return True

    if __name__ == '__main__':
        FTPconnect()
#
#
normal_register_manage.FTPconnect()







            #     print('每一个用户分配一个ip')
        #     print('执行这个QQ用户对应的某个ip')
        #     QQ_ID =ID
        #
        #     # print(Dicyionary.last(cd))
        #
        #     print('这个输入的QQ用户是：', QQ_ID)
        #     try:
        #         if QQ_ID:
        #             ###################这里去执行这个生成ip的函数#######################################################
        #             exist_QQ_ID = []
        #             for i in range(0, len(QQ_ID_IP_read)):
        #                 print('这个QQ_ID_IP的类型是:', type(QQ_ID_IP_read))
        #                 (key, value), = QQ_ID_IP_read[i].items()
        #                 print('key是:', key)
        #                 print('QQ_ID是', QQ_ID)
        #                 exist_QQ_ID.append(key)
        #             ################做判断
        #             print(exist_QQ_ID)
        #             print('正在遍历查询有没有这个QQ用户')
        #             QQ_ID = int(QQ_ID)
        #             if QQ_ID in exist_QQ_ID:
        #                 print('已经存在此用户，不需要再生成ip地址..........................')
        #                 for i in range(0, len(QQ_ID_IP_read)):
        #                     (key, value), = QQ_ID_IP_read[i].items()
        #                     if key == QQ_ID:
        #                         print(QQ_ID_IP_read[i][key])
        #                         print('这个就是已经存在的ip')
        #                         ip_addr = QQ_ID_IP_read[i][key]
        #                         msg = ip_addr
        #                         conn.send(msg.encode('utf-8'))
        #                         QQ_ID_DIC = {}
        #                         QQ_ID_DIC[ID] = ip_addr
        #                         print('这个已经生成的ip用户是:', QQ_ID_DIC)
        #                         print(type(data_login))
        #                         data_login.append(QQ_ID_DIC)
        #                         #################跳到了一个页面#############################################
        #                         f = open('login_QQ_ID' + '.txt', 'w')
        #                         print('执行写入操作')
        #                         f.write(str(data_login))
        #                         f.close()
        ##################3跳到了一个页面#############################################
        # from  wechat_server_manage import multi_user_work_manage
        # multi_user_work_manage.multi_user()





        # return QQ_dic[QQ_ID]

        # all_server()