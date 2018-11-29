#############################后台验证，服务这端进行验证######################################################################



import  os,sys
import  time,os
from multiprocessing import  Process,Pool
PATH=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(PATH)
print('开启服务这端，进行后台验证环节.....................................')
import threading
# class server_set_up:
import json
# # open('all_set_up_reques')
# with open('all_set_up_request'+'.txt','r')as f:
#     all_id=f.read()
#     f.close()
# print(all_id)
# import demjson
# all_id=demjson.decode(all_id)
# print(type(all_id))
# print(len(all_id))
#
# if all_id:
#     print('有数据')
#     f_open_id=open('all_set_up_request.txt','r')
#     all_request=json.loads(f_open_id.read())
#     f_open_id.close()
#     print(type(all_request))
#
# else:
#     all_request=[1,2]
#     with open('all_set_up_request.txt', 'w')as f:
#         f.write(str(all_request))
#         f.close()
#         print('执行')
#
# print(len(all_request))
# ################################################开启多线程通信#####################################
# ############进行监听#############################################################################################
#
# print('进入到多用户高并发环节......................................................')
# import os,sys
#
# PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# # PATH= os.path.abspath(os.path.dirname(__file__))
# ##########################这个是当前的绝对路径
# sys.path.append(PATH)
# import json
# print(PATH)
#
# f = open('login_QQ_ID.txt', 'r')
# data = f.read()
# f.close()
# import demjson
#
# # print(all_QQ)
# print('全部的用户ip已经上线的QQ用户')
#
#
#
#
# import  threading
# import  time
# import  socket
# import selectors
# #一直监听有没有客户进来
#
#
# import selectors
# import socket
# sk=socket.socket()
# sk.bind(('127.1.1.0',8080))
# sk.listen(100)
# sel=selectors.DefaultSelector()#有对象才能监听注册
# sk.setblocking(False)
# def accept(sk):
#     try:
#     # print('开始建立链接了')
#         conn,addr=sk.accept()
#         print('开始建立链接了',conn)
#         conn.setblocking(False)
#     except Exception as e:
#         print(e)
#     sel.register(conn,selectors.EVENT_READ,read)
# def read(conn):
#     try:
#         print('开始建立通信循环了')
#         data=conn.recv(1024)
#         print ('接受到的数据是:',data.decode('utf-8'))
#         data=data.decode('utf-8')
#         def request_handler(conn):
#             if data_thread == 'login_request':
#                 print('建立登录请求端口')
#                 all_request.append(data)
#                 # send_data=input('请输入你发送的数据:').encode('utf-8')
#                 # send_data = ' 服务端响应： success'
#                 # conn.send(send_data.encode('utf-8'))
#                 # print('已经发送数据')
#                 print('启动后台登录验证环节')
#                 from wechat_server_manage import normal_user_authenticate_manage
#                 normal_user_authenticate_manage.normal_user_auth.FTPconnect()
#             elif data_thread == 'register_request':
#                 print('建立注册请求的端口')
#                 # send_data = ' 服务端响应： success'
#                 # conn.send(send_data.encode('utf-8'))
#                 print('启动后台注册环节')
#                 from wechat_server_manage import normal_user_register_manage
#                 normal_user_register_manage.normal_register_manage.FTPconnect()
#         # request_handler()
#         ########################################################################
#             # return  data
#         # def create_request_thread():
#         #     request=data
#         #     all_request.append(request)
#         #     for i in range(0,len(all_request)):
#         #         all_request[i] = threading.Thread(target=request_handler, args=(request,))
#         #         all_request[i].start()
#         #         print('启动线程number%s'%all_request[i])
#         # create_request_thread()
#
#
#         # return  data
#         # else:
#         #     print('fail')
#     except Exception as e:
#         print(e)
# sel.register(sk,selectors.EVENT_READ,accept)
# while True:
#     print('开始一直监听.........')
#     events=sel.select()#如果监听到的话，就是sk变成活动的socket对象时，accept绑定sk,[sk,accept,accept,]
#     # print('events是',events
#     for key,mask in events:
#         callback=key.data#这个是绑定的accept函数
#         # print(key.data,key.fileobj)
#         callback(key.fileobj)
# def create_thread():
#     request=read()
#     print(request)
#     print('suce')
    ######################################################################################################################################################



# create_thread()



# FTPconnect()
    # def create_thread(self):
    #     print('来一个用户请求就创建一个线程，分配相应的任务')
    #     request=self.read()

# thread=[]
# t=[]
# for i in range(0,len(all_request)):
    # (key,value),=all_QQ.items()
    # (key,value),=all_QQ[i].items()
    # print('这个当前用户ip是:',value)
    # print('这个当前用户是:',key)
    # current_QQ_IP=
    # print(current_QQ_ID)
    # t1=threading.Thread(target=hi,args=(3,))
    # request=all_request[-1]
#     i=threading.Thread(target=FTPconnect,args=(request,))
#     thread.append(i)
# for j in thread:
#     j.start()
# print('ending................。。。。')



# server_register()
# server_authenticate()
#
def server_register():
    print('启动后台注册环节')
    from wechat_server_manage import normal_user_register_manage
    normal_user_register_manage.normal_register_manage.FTPconnect()
    # normal_user_register_manage.normal_register_manage()

def server_authenticate():
    print('启动后台登录验证环节')
    from wechat_server_manage import normal_user_authenticate_manage
    normal_user_authenticate_manage.normal_user_auth.FTPconnect()


if __name__ == '__main__':
    pool = Pool(4)
    # 某个动作后某个函数执行成功后，在执行的函数
    #    pool.apply_async(func=server_authenticate)#异步,几个进程进程的走
    pool.apply_async(func=server_authenticate())
    pool.apply_async(func=server_register())
    pool.close()
    pool.join()
    print('endding.........................................')


# thread=[]
# t=[]
# for i in range(0,len(all_QQ)):
#     (key,value),=all_QQ[i].items()
#     print('这个当前用户ip是:',value)
#     print('这个当前用户是:',key)
#     # current_QQ_IP=
#     # print(current_QQ_ID)
#     # t1=threading.Thread(target=hi,args=(3,))
#     i=threading.Thread(target=multi_user,args=(key,value,))
#     thread.append(i)
# for j in thread:
#     j.start()
# print('ending................。。。。')
#
#
#
# t1=threading.Thread(target=server_register())
# t2=threading.Thread(target=server_authenticate())
# t1.start()
# t2.start()



