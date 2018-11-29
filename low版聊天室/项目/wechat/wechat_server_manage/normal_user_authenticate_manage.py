##############################普通用户验证环节#######################################################

############################建一个用户在线的数据库
import demjson

################做判断###################################
fh=open('login_QQ_ID.txt','r')
data_login=fh.read()
fh.close()

if len(data_login):
    data_login = demjson.decode(data_login)
else:
    login_QQ = []
    fl = open('login_QQ_ID.txt', 'w')
    fl.write(str(login_QQ))
    fl.close()


###############################在打开########################################
fh=open('login_QQ_ID.txt','r')
data_login=fh.read()
fh.close()
data_login=demjson.decode(data_login)
# print(type(data_login))




import socket
import selectors
import time
import json
import socket

import  os,sys
PATH=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# PATH= os.path.abspath(os.path.dirname(__file__))
##########################这个是当前的绝对路径
sys.path.append(PATH)

class normal_user_auth:
    print('进入普通用户验证环节')



    # 一直监听有没有客户进来
    class FTPconnect():
        def __init__(self):
            self.dic = []
            ###############################这个字典把全部的都放在里面了，可以后面调用使用#########################
            self.rel = selectors.DefaultSelector()
            self.create_socket()
            self.handler()

        def create_socket(self):
            self.sock = socket.socket()
            self.sock.bind(('127.0.0.2', 8080))
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

        def read(self, conn):
            try:
                data = conn.recv(1024)
                print(data)
                if data:
                    data=data.decode('utf-8')
                    print('接收到的验证信息的数据是:',data)
                    import demjson
                    data=demjson.decode(data)
                    print(data)
                    print(type(data))
                    (QQ_send_ID,QQ_send_PWD),=data.items()

                    import json
                    ###############做出连接这个server的选择来
                    f = open('exist_users_QQ.txt', 'r')
                    exist_user_QQ = f.read()
                    f.close()

                    Dicyionary = demjson.decode(exist_user_QQ)
                    print(Dicyionary)#######字典形式的

                    print('用户%s连接进来了' % self.dic.index(conn))
                    #################################验证环节########################################################
                    print('已经接收到%s的数据%s' %((self.dic.index(conn)),data))
                    class auth:
                        def __init__(self):
                            self.auth_QQ_ID_PWD()
                        def auth_QQ_ID_PWD(self):
                            print('验证环节')
                            for i in range(0,len(Dicyionary)):
                                (QQ_ID,QQ_PWD),=Dicyionary[i].items()
                                print(Dicyionary[i])
                                if str(QQ_ID)==QQ_send_ID:
                                    print('第一步验证通过')
                                    if QQ_send_PWD==QQ_PWD:
                                        print('验证通过')
                                        QQ_ID_IP_read = open('QQ_ID_IP_save.txt', 'r')
                                        QQ_ID_IP_read = QQ_ID_IP_read.read()
                                        print('这个字典的全部ip是', QQ_ID_IP_read)
                                        import demjson
                                        QQ_ID_IP_read=demjson.decode((QQ_ID_IP_read))
                                        print(type(QQ_ID_IP_read))
                                        import random
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
                                            ####################################这里判断这个数据库里面有没有这个QQ用户

                                            def QQ_ID_IP_create(self):
                                                print('每一个用户分配一个ip')
                                                print('执行这个QQ用户对应的某个ip')
                                                QQ_ID =QQ_send_ID

                                                # print(Dicyionary.last(cd))

                                                print('这个输入的QQ用户是：', QQ_ID)
                                                try:
                                                    if QQ_ID:
                                                        ###################这里去执行这个生成ip的函数#######################################################
                                                        exist_QQ_ID = []
                                                        for i in range(0, len(QQ_ID_IP_read)):
                                                            print('这个QQ_ID_IP的类型是:', type(QQ_ID_IP_read))
                                                            (key, value), = QQ_ID_IP_read[i].items()
                                                            print('key是:', key)
                                                            print('QQ_ID是', QQ_ID)
                                                            exist_QQ_ID.append(key)
                                                        ################做判断
                                                        print(exist_QQ_ID)
                                                        print('正在遍历查询有没有这个QQ用户')
                                                        QQ_ID = int(QQ_ID)
                                                        if QQ_ID in exist_QQ_ID:
                                                            print('已经存在此用户，不需要再生成ip地址..........................')
                                                            for i in range(0, len(QQ_ID_IP_read)):
                                                                (key, value), = QQ_ID_IP_read[i].items()
                                                                if key == QQ_ID:
                                                                    print(QQ_ID_IP_read[i][key])
                                                                    print('这个就是已经存在的ip')
                                                                    ip_addr = QQ_ID_IP_read[i][key]
                                                                    msg = ip_addr
                                                                    conn.send(msg.encode('utf-8'))
                                                                    QQ_ID_DIC = {}
                                                                    QQ_ID_DIC[QQ_send_ID] = ip_addr
                                                                    print('这个已经生成的ip用户是:', QQ_ID_DIC)
                                                                    # print(type(data_login))
                                                                    data_login.append(QQ_ID_DIC)
                                                                    #################跳到了一个页面#############################################
                                                                    f = open('login_QQ_ID' + '.txt', 'w')
                                                                    print('执行写入操作')
                                                                    f.write(str(data_login))
                                                                    f.close()
                                                                    ##################3跳到了一个页面#############################################
                                                                    from  wechat_server_manage import  multi_user_work_manage
                                                                    multi_user_work_manage.multi_user()

                                                        else:
                                                            print('走这步')
                                                            print(
                                                                '运行生成ip的函数...........................................................')
                                                            # has_QQ = self.QQ_ID_IP_create()
                                                            # print(has_QQ)
                                                            print('此用户没有分配ip地址')
                                                            # return  None
                                                            ########################################只生成一个ip地址就好了#########################
                                                            # QQ_new_IP = self.create_ip()
                                                            QQ_new_IP = self.has_ip()
                                                            print('生成的ip地址是:', QQ_new_IP)
                                                            if QQ_new_IP == None:
                                                                print('没有生成ip直接返回')
                                                            else:
                                                                print('已经执行creat_ip的函数了')
                                                                QQ_dic = {}
                                                                QQ_dic[QQ_ID] = QQ_new_IP
                                                                print(QQ_dic)

                                                                QQ_ID_IP_read.append(QQ_dic)
                                                                ###############################################保存这个用户和对应的ip到数据库里面
                                                                QQ_ID_IP_save = open('QQ_ID_IP_save.txt', 'w')

                                                                QQ_ID_IP_save.write(str(QQ_ID_IP_read))
                                                                QQ_ID_IP_save.close()
                                                                print('保存成功')
                                                                ip_addr = QQ_dic[QQ_ID]
                                                                print(ip_addr)
                                                                msg = ip_addr
                                                                conn.send(msg.encode('utf-8'))
                                                                QQ_ID_DIC = []
                                                                QQ_ID_DIC[QQ_send_ID] = ip_addr
                                                                data.append(QQ_ID_DIC)
                                                                ##################3跳到了一个页面#############################################
                                                                f = open('login_QQ_ID' + '.txt', 'w')
                                                                f.write(str(data))
                                                                f.close()
                                                                from  wechat_server_manage import multi_user_work_manage
                                                                multi_user_work_manage.multi_user()
                                                    else:
                                                        print(
                                                            '没有QQ_ID传过来...........................................................')


                                                except Exception as e:
                                                    print(e)

                                        all_server()
                                    else:
                                        continue
                                else:
                                    continue
                            else:
                                msg='auth fail,please input again'
                                conn.send(msg.encode('utf-8'))
                                print('验证失败')

                    auth()





#                     for i in range(0,len(Dicyionary)):
#                         if data==str(Dicyionary[i]):
#                             print('QQ身份验证通过')
#                             ##################################发送QQ_ID对应的ip地址#####################
#                             IP=open('QQ_ID_IP_save.txt','r')
#                             QQ_IP=IP.read()
#                             IP.close()
#                             print(QQ_IP)
#                             QQ_IP=demjson.decode(QQ_IP)
#                             print('转换后的QQ_IP类型是:',type(QQ_IP))
#                             j=0
#                             # d = {'name': 'haohao'}
#                             ####################这个是取QQ的id,在传送过来的数据里面取
#                             # (QQ_ID_key, value), = data.items()
#                             # print(QQ_ID_key)
#                             #####################这个是取QQ_IP字典里面对应的ip你的QQ_ID
#                             print('接收过来的data类型是:',type(data))
#                             data2 = demjson.decode(data)
#                             print(type(data2))
#                             (QQ_ID_key, QQ_ID_VALUE), = data2.items()
#                             print(QQ_ID_key)
#                             print(data2)
#
# ######################################对QQ_IP进行类型转化############################################################
#         ####################在QQ_IP这里面拿到所有的已经注册号的QQ_ID,在QQ_ID.txt也有所有已经注册的QQ号码
#                             all_QQ_ID = []
#                             for j in range(0, len(QQ_IP)):
#                                 (QQ_ID, value), = QQ_IP[j].items()
#                                 all_QQ_ID.append(QQ_ID)
#
#
#
#                             print(all_QQ_ID)
#                             print('这个所有的QQ_IP的QQ_ID类型是：',type(all_QQ_ID))
#
# ######################################进行验证环节########################################################################################################
#                             print('这个QQ_ID_KEY是:',type(str(QQ_ID_key)))
#                             print('这个QQ_IP【1】的数据类型是:',type(QQ_IP[1]))
#
#                             #########################这步是进行密码验证环节#########################
#                             # for z in range(0, len(Dicyionary)):
#                             #     print('进行查找这个用户....')
#                             #     # if str(QQ_ID_key) == str(QQ_IP[z]):
#                             #     print('这个数据库用户与密码是:',Dicyionary[z])
#                             #     #######################在这里去相对应的数据库里面的QQ用户的密码
#                             #     (DATA_QQ_ID, QQ_ID_PWD), = Dicyionary[z].items()
#                             #     print(type(QQ_ID_VALUE))
#                             #     print(type(QQ_ID_PWD))
#                             #     if QQ_ID_VALUE==str(QQ_ID_PWD):
#                             #         print('用户传送过来的密码是', QQ_ID_VALUE)
#                             #         print('这个数据库的密码是:', QQ_ID_PWD)
#                             #         print('验证通过')
#                             #         print('QQ用户号码是:',QQ_ID_key)
#                             #         print('这个QQ密码是:',Dicyionary[z][QQ_ID_key])
#                             #         import json
#                             #         import random
#                             #         import demjson
#                             #         import time
#                             #         # time.sleep(3)
#                             #         print('#' * 100)
#                             #         print('欢迎来到server端。。。。。。。。。。。。。。。。。。')
#                             #         ##################################拿到登录注册环节传过来的QQ用户##############################################
#                             #
#                             #         QQ_ID_IP_read = open('QQ_ID_IP_save.txt', 'r')
#                             #         QQ_ID_IP_read = QQ_ID_IP_read.read()
#                             #         print('这个字典的全部ip是', QQ_ID_IP_read)
#                             #         print(type(QQ_ID_IP_read))
#                             #         #########################转换类型
#                             #         import demjson
#                             #
#                             #         QQ_ID_IP_read = demjson.decode(QQ_ID_IP_read)
#                             #         print(type(QQ_ID_IP_read))
#                             #         #########################已经转换成功list类型
#                             #         ip_open = open('QQ_ID_IP_save.txt', 'r')
#                             #         QQ_IP = ip_open.read()
#                             #         ip_open.close()
#                             #         print('全部的用户和对应的ip是', QQ_IP)


            #                 else:
            #                    break
            #             else:
            #                 print('没有找到')
            #                 break
            #         else:
            #             print('没有找到这个登录的QQ号码')
            #     else:
            #         msg = 'fail'
            #         conn.send(msg.encode('utf-8'))
            #         print('没有取到数据')
            except Exception as e:
                print(e)

    if __name__ == '__main__':
        FTPconnect()
normal_user_auth()

##############################################################################################################################################
    # import socket
    # import selectors
    # import time
    # import json
    # import socket
    #
    # import  os,sys
    # PATH=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # # PATH= os.path.abspath(os.path.dirname(__file__))
    # sys.path.append(PATH)
    #
    # from  wechat_server_manage import *
    # class normal_user_auth:
    #     print('进入普通用户验证环节')
    #
    #
    #
    #     # 一直监听有没有客户进来
    #     class FTPconnect():
    #         def __init__(self):
    #             self.dic = []
    #             ###############################这个字典把全部的都放在里面了，可以后面调用使用#########################
    #             self.rel = selectors.DefaultSelector()
    #             self.create_socket()
    #             self.handler()
    #
    #         def create_socket(self):
    #             self.sock = socket.socket()
    #             self.sock.bind(('127.1.1.3', 8080))
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
    #
    #         def read(self, conn):
    #             try:
    #                 data = conn.recv(1024)
    #                 print(data)
    #                 if data:
    #                     print('接收到的验证信息的数据是:',data.decode('utf-8'))
    #                     data=data.decode('utf-8')
    #                     import demjson
    #                     # data=demjson.encode(data)
    #                     # print(data)
    #                     import json
    #                     ###############做出连接这个server的选择来
    #                     f = open('exist_users_QQ.txt', 'r')
    #                     data1 = f.read()
    #                     f.close()
    #                     # print(data.encode('utf-8'))
    #                     # data2 = data1.encode('utf-8')
    #                     # print(type(data))
    #
    #
    #                     # print(type(data))
    #
    #                     Dicyionary = demjson.decode(data1)
    #                     print(Dicyionary)
    #
    #                     print('用户%s连接进来了' % self.dic.index(conn))
    #                     #################################验证环节########################################################
    #
    #
    #                     print('已经接收到%s的数据%s' %((self.dic.index(conn)),data))
    #                     i=0
    #
    #                     print('data是,',data)
    #                     for i in range(0,len(Dicyionary)):
    #                         if data==str(Dicyionary[i]):
    #                             print('QQ身份验证通过')
    #                             ##################################发送QQ_ID对应的ip地址#####################
    #                             IP=open('QQ_ID_IP_save.txt','r')
    #                             QQ_IP=IP.read()
    #                             IP.close()
    #                             print(QQ_IP)
    #                             QQ_IP=demjson.decode(QQ_IP)
    #                             print('转换后的QQ_IP类型是:',type(QQ_IP))
    #                             j=0
    #                             # d = {'name': 'haohao'}
    #                             ####################这个是取QQ的id,在传送过来的数据里面取
    #                             # (QQ_ID_key, value), = data.items()
    #                             # print(QQ_ID_key)
    #                             #####################这个是取QQ_IP字典里面对应的ip你的QQ_ID
    #                             print('接收过来的data类型是:',type(data))
    #                             data2 = demjson.decode(data)
    #                             print(type(data2))
    #                             (QQ_ID_key, QQ_ID_VALUE), = data2.items()
    #                             print(QQ_ID_key)
    #                             print(data2)
    #
    # ######################################对QQ_IP进行类型转化############################################################
    #
    #
    #
    #                             ######################在QQ_IP这里面拿到所有的已经注册号的QQ_ID,在QQ_ID.txt也有所有已经注册的QQ号码
    #                             all_QQ_ID = []
    #                             for j in range(0, len(QQ_IP)):
    #                                 (QQ_ID, value), = QQ_IP[j].items()
    #                                 all_QQ_ID.append(QQ_ID)
    #                                 # print(key)
    #                                 # print(d)
    #
    #                             print(all_QQ_ID)
    #                             print('这个所有的QQ_IP的QQ_ID类型是：',type(all_QQ_ID))
    #
    # ######################################进行验证环节########################################################################################################
    #                             print('这个QQ_ID_KEY是:',type(str(QQ_ID_key)))
    #                             print('这个QQ_IP【1】的数据类型是:',type(QQ_IP[1]))
    #
    #                             #########################这步是进行密码验证环节#########################
    #                             for z in range(0, len(Dicyionary)):
    #                                 print('进行查找这个用户....')
    #                                 # if str(QQ_ID_key) == str(QQ_IP[z]):
    #                                 print('这个数据库用户与密码是:',Dicyionary[z])
    #                                 #######################在这里去相对应的数据库里面的QQ用户的密码
    #                                 (DATA_QQ_ID, QQ_ID_PWD), = Dicyionary[z].items()
    #                                 print(type(QQ_ID_VALUE))
    #                                 print(type(QQ_ID_PWD))
    #                                 if str(QQ_ID_VALUE)==str(QQ_ID_PWD):
    #                                     print('用户传送过来的密码是', QQ_ID_VALUE)
    #                                     print('这个数据库的密码是:', QQ_ID_PWD)
    #                                     print('验证通过')
    #                                     print('QQ用户号码是:',QQ_ID_key)
    #                                     print('这个QQ密码是:',Dicyionary[z][QQ_ID_key])
    #                                 else:
    #                                     continue
    #                             else:
    #                                 continue
    #                                 print('没有找到')
    #                         else:
    #                             continue
    #                             print('没有找到这个登录的QQ号码')
    #
    #                     else:
    #                         msg = 'fail'
    #                         conn.send(msg.encode('utf-8'))
    #                         print('没有取到数据')
    #             except Exception as e:
    #                 print(e)
    #
    #     if __name__ == '__main__':
    #         FTPconnect()


    #############################################################重写########################################
















    #     for i in range(0, len(QQ_IP)):
                                #         print('QQ用户{}匹配ip地址中.................................'.format(QQ_ID_key))
                                #         print('在注册的数据库里面已经找到你登录的QQ号码')
                                #         (key, value), = QQ_IP[i].items()
                                #         ##################拿到这个QQ_ID
                                #         if QQ_ID == key:
                                #             print(QQ_ID)
                                #             print('已经找到这个QQ用户。。。。。。。。。。。。。。。。。。。。。。。。。', key)
                                #             print('这个对应的ip地址是:', value)
                                #             msg=value
                                #             ####################这个取出来了ip地址，某个QQ号码对应的ip地址
                                #             conn.send(str(msg).encode('utf-8'))
                                #         else:
                                #             # print('没有找到。。。。。。。。。。。。。。。。。。。。。。。。。。')
                                #            continue
                                #     else:
                                #         print('没有找这个用户...................................')
                                #
                                #
                                # else:
                                #     # print('fail')
                                #     continue










#########################################################################################################################################################

                                    # if QQ_ID_key in all_QQ_ID:
                                    #     print('QQ用户{}匹配ip地址中.................................'.format(QQ_ID_key))
                                    #     print('在注册的数据库里面已经找到你登录的QQ号码')
                                    #     # print(Dicyionary[QQ_ID_key])
                                    #     print(QQ_IP[QQ_ID_key])
                                    #     print('这个QQ_IP是',QQ_IP)
                                    #     # msg = 'success'
                                    #     msg=QQ_IP[QQ_ID_key]
                                    #     ####################这个取出来了ip地址，某个QQ号码对应的ip地址
                                    #     conn.send(str(msg).encode('utf-8'))
                                    #     #
                                    #     # from  wechat_server_manage import server
                                    #     # server.all_server()
                                    # else:
                                    #     print('没有找到这个登录的QQ号码')








###############################在这里拿整个ip地址###############################



# import  os,sys
# PATH=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# PATH= os.path.abspath(os.path.dirname(__file__))
#########################这个是当前的绝对路径
# sys.path.append(PATH)
# import json
# import random
# import  demjson
# import time
# time.sleep(3)
# print('#'*100)
# print('欢迎来到server端。。。。。。。。。。。。。。。。。。')
#################################拿到登录注册环节传过来的QQ用户##############################################
# from  wechat_server_manage import normal_user_authenticate_manage
# QQ_ID=normal_user_authenticate_manage.normal_user_auth.FTPconnect()
#
#
# QQ_ID=normal_user_auth.FTPconnect()
# print('传进来的QQ_ID是：',QQ_ID)
#
#
#
#
#








        #################生成ip


    # def has_QQ_ID(self):
        # print('运行生成ip的函数...........................................................')
        # has_QQ = self.QQ_ID_IP_create()
        # print(has_QQ)
        # if has_QQ:
        #     print('此用户没有分配ip地址')
        #     ########################################只生成一个ip地址就好了#########################
        #     QQ_new_IP = self.create_ip()
        #     print('生成的ip地址是:', QQ_new_IP)
        #     if QQ_new_IP == None:
        #         print('没有生成ip直接返回')
        #     else:
        #         print('已经执行creat_ip的函数了')
        #         QQ_dic = {}
        #         QQ_dic[QQ_ID] = QQ_new_IP
        #         print(QQ_dic)
        #
        #         QQ_ID_IP_read.append(QQ_dic)
        #         ###############################################保存这个用户和对应的ip到数据库里面
        #         QQ_ID_IP_save = open('QQ_ID_IP_save.txt', 'w')
        #
        #         QQ_ID_IP_save.write(str(QQ_ID_IP_read))
        #         QQ_ID_IP_save.close()
        #         print('保存成功')
        # else:
        #     print('不执行此步骤')
        #












                        # ##############拿到用户和ip地址,每一个用户都分配一个ip地址
    # QQ_ID_IP_read=demjson.decode(QQ_ID_IP_read)
    #####################################demjson会转化为就可以导入这个字典里面对象，
    # QQ_ID_IP_read.append(QQ_dic)








# else:
        #     print('错误')

        # return  QQ_ID_key
        ####################返回QQ用户给server端，分配ip地址#####################################################


    # return  QQ_ID_key





# all_server()

