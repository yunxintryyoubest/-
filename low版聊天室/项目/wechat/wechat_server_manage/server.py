# # ################################这里可以配置全部的ip地址##############################################################################
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
#
#
#
# all_server()

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
# ##############################注意：这里会传入一个QQ用户，返回一个ip地址给该用户#################################################################################
#
# ################################这里可以配置全部的ip地址##############################################################################
import  os,sys
PATH=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# PATH= os.path.abspath(os.path.dirname(__file__))
##########################这个是当前的绝对路径
sys.path.append(PATH)
import json
import random
import  demjson
import time
# time.sleep(3)
print('#'*100)
print('欢迎来到server端。。。。。。。。。。。。。。。。。。')
##################################拿到登录注册环节传过来的QQ用户##############################################
# from  wechat_server_manage import normal_user_authenticate_manage
# QQ_ID=normal_user_authenticate_manage.normal_user_auth.FTPconnect()
# print('传进来的QQ_ID是：',QQ_ID)

#

QQ_ID_IP_read = open('QQ_ID_IP_save.txt' , 'r')
QQ_ID_IP_read=QQ_ID_IP_read.read()
print('这个字典的全部ip是',QQ_ID_IP_read)
print(type(QQ_ID_IP_read))
#########################转换类型
import demjson

QQ_ID_IP_read=demjson.decode(QQ_ID_IP_read)
print(type(QQ_ID_IP_read))
#########################已经转换成功list类型
#
#



ip_open = open('QQ_ID_IP_save.txt', 'r')
QQ_IP = ip_open.read()
ip_open.close()
print('全部的用户和对应的ip是', QQ_IP)


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
            last_ip = int(random.randrange(100))
            print(last_ip)
            seconde_last_ip = int(random.randrange(100))
            print(seconde_last_ip)
            ip_addr = '192.168.{}.{}'.format(seconde_last_ip, last_ip)
            print('这个生成的ip地址是：', ip_addr)
            ##################执行此步骤，看看这个ip地址是否重复#########################################
            return  ip_addr
            ########################这个可以返回到init函数里面，这个retrun ip_addr，默认是返回到init函数里面####################


        ########################拿到已经存在的ip地址，去重
            #####################拿到已经存在的ip地址
    def has_ip(self):
        ip_addr=self.create_ip()
        exist_ip = open('QQ_ID_IP_save.txt', 'r')
        existed_ip = exist_ip.read()
        exist_ip.close()
        existed_ip = demjson.decode(existed_ip)
        print('全部的ip地址是：',existed_ip)
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
#     ####################################这里判断这个数据库里面有没有这个QQ用户
#
    def QQ_ID_IP_create(self):
        print('每一个用户分配一个ip')
        print('执行这个QQ用户对应的某个ip')

        PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        sys.path.append(PATH)
        from  wechat_server_manage import test
        QQ_ID= test.create_id.create()

        # QQ_ID = input('请输入QQ_ID:')
        # print('QQ_ID是', QQ_ID)
        # print(Dicyionary.last(cd))
        #
        # print('这个输入的QQ用户是：', QQ_ID)
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
                    # if QQ_ID ==key:
                    #     print('已经存在此用户，不需要再生成ip地址..........................')
                    #     print(value)

                ################做判断
                print(exist_QQ_ID)
                print('正在遍历查询有没有这个QQ用户')
                QQ_ID = int(QQ_ID)
                if QQ_ID in exist_QQ_ID:
                    print('已经存在此用户，不需要再生成ip地址..........................')
                    # print(value)
                    for i in range(0,len(QQ_ID_IP_read)):
                        (key, value), = QQ_ID_IP_read[i].items()
                        if key==QQ_ID:
                            print(QQ_ID_IP_read[i][key])
                            print('这个就是已经存在的ip')




                        # if str(key) == str(QQ_ID):
                    # return  value
                else:
                    print('运行生成ip的函数...........................................................')
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
                        ip_addr=QQ_dic[QQ_ID]
                        print(ip_addr)
                        # return QQ_dic[QQ_ID]
                    return

            else:
                print('没有QQ_ID传过来...........................................................')
        except Exception as e:
            print(e)

all_server()



# all_server()
# from  wechat_server_manage import test
# ID=test.create_id.create()
# print(ID)
# QQ_ID = test.create_id()
        #################生成ip

#
#     def has_QQ_ID(self):
#         print('运行生成ip的函数...........................................................')
#         has_QQ = self.QQ_ID_IP_create()
#         print(has_QQ)
#         if has_QQ:
#             print('此用户没有分配ip地址')
#             ########################################只生成一个ip地址就好了#########################
#             QQ_new_IP = self.create_ip()
#             print('生成的ip地址是:', QQ_new_IP)
#             if QQ_new_IP == None:
#                 print('没有生成ip直接返回')
#             else:
#                 print('已经执行creat_ip的函数了')
#                 QQ_dic = {}
#                 QQ_dic[QQ_ID] = QQ_new_IP
#                 print(QQ_dic)
#
#                 QQ_ID_IP_read.append(QQ_dic)
#                 ###############################################保存这个用户和对应的ip到数据库里面
#                 QQ_ID_IP_save = open('QQ_ID_IP_save.txt', 'w')
#
#                 QQ_ID_IP_save.write(str(QQ_ID_IP_read))
#                 QQ_ID_IP_save.close()
#                 print('保存成功')
#         else:
#             print('不执行此步骤')
#
#
# #
# #
# #
# #
# #
# #
#
#
#
#
#
#                         # ##############拿到用户和ip地址,每一个用户都分配一个ip地址
#     # QQ_ID_IP_read=demjson.decode(QQ_ID_IP_read)
#     #####################################demjson会转化为就可以导入这个字典里面对象，
#     # QQ_ID_IP_read.append(QQ_dic)
#
#
#
#
#
#
#
#
# # ip_addr=all_server()
# # print('*'*100)
# # print(ip_addr)
#
#
#
#

#
#
#
# #
# QQ_ID_key=[{10:'192.168.5.5'}]
# f = open('login_QQ_ID' + '.txt', 'w')
# f.write(str(QQ_ID_key))
# f.close()
#
# fh=open('login_QQ_ID.txt','r')
# data=fh.read()
# fh.close()
# import demjson
# data=demjson.decode(data)
# print(type(data))
#
#
#
# for i in range(0,len(data)):
#     (key,value),=data[i].items()
#     print(value)
#     print(key)
# print(value)



# a={1:23}
#
# data.append(a)
# print(data)


#
# f = open('login_QQ_ID.txt', 'r')
# ID = f.read()
# f.close()
# print(ID)
# import demjson
# ID=demjson.decode(ID)
# print(type(ID))
# # (key,value),=ID.items()
# (key,value),=ID.items()
# (key, value), =ID.items()
# print('这个ip地址是:')
#
# print(ID[1])
# print(value)



