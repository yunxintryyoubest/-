#########################启动聊天室low版见谅############################################################
import  sys
import  os
import  time


################################注意，这个是引入绝对路径，从这个文件夹里面开始执行
PATH=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# PATH= os.path.abspath(os.path.dirname(__file__))
##########################这个是当前的绝对路径
sys.path.append(PATH)


# os.path.basename(r'')##访问当前路径的文件名，path最后的文件名
# os.path.dirname(path)##访问文件名的路径，path的目录
#
# os.path.join()#路径拼接
from  core import  main_menus


def  before_start():
    start_menus = input("请输入run启动聊天室:")
    if start_menus=='run':
        set_up()
    else:
        print ('输入有误')

class set_up:
    # print('执行set_up部分')
    def __init__(self):
        print( '执行init这块')
        print('已经启动后台服务端环节.........................')
        # from  wechat_server_manage import  normal_user_register_manage
        # normal_user_register_manage.normal_register_manage.FTPconnect()
        # self.menus=menus
        self.start()
    def start(self):
        print('进入聊天室...............')
        # time.sleep(3)
        menus=({1,'admin(超级用户)'},{2,'普通用户'},{3,'退出聊天室'})
        print(menus)
        from  core import main_menus
        print('success')
        main_menus.main_choice()
before_start()





#
# import  threading
# import  time
# def server():
#     print('已经启动后台服务端环节.........................')
#     from  wechat_server_manage import normal_user_register_manage
#     normal_user_register_manage.normal_register_manage.FTPconnect()
#
# def hi():
#     print('进入聊天室...............')
#     # time.sleep(3)
#     menus = ({1, 'admin(超级用户)'}, {2, '普通用户'}, {3, '退出聊天室'})
#     print(menus)
#     from  core import main_menus
#     print('success')
#     main_menus.main_choice()
#
# thread=[]
#
# t1=threading.Thread(target=server)
#
# t2=threading.Thread(target=hi)
#
#
# thread.append(t1)
# thread.append(t2)#把t1，t2放进列表thread里面
# # t1.setDaemon(t1)
# t1.setDaemon(True)#当t1结束时，主线程也结束了，t2是守护主线程的，当主线程结束时，t2也跟着结束
# # print('t2进程是否结束',t2.isAlive())
# for t in thread:
#     t.start()#所有线程都开启了
#     # print(t.setName('Thread-1'))
#
#
# print('all over')
# print(t2.isAlive())#判断t2线程是否活动




import  time,os
from multiprocessing import  Process,Pool

#
# #子进程的
# def foo():
#     print('已经启动后台服务端环节.........................')
#     from  wechat_server_manage import normal_user_register_manage
#     normal_user_register_manage.normal_register_manage.FTPconnect()
# def set_up():
#     print('进入聊天室...............')
#     # time.sleep(3)
#     menus = ({1, 'admin(超级用户)'}, {2, '普通用户'}, {3, '退出聊天室'})
#     print(menus)
#     from  core import main_menus
#     print('success')
#     main_menus.main_choice()


#
#主进程的
# def Bar(num):


#
# if __name__ == '__main__':
#     pool=Pool(2)
    # for i in range(2):
        # pool.apply(func=foo,args=(i,))#同步，一个进程一个进程的走
     #某个动作后某个函数执行成功后，在执行的函数
        # pool.apply_async(func=foo,args=(i,),callback=Bar)#异步,几个进程进程的走

    # pool.apply_async(func=foo)
    # pool.apply_async(func=set_up())
    # pool.close()
    # pool.join()
    # print('endding')