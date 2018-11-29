# ###################################################注册和登录成功的页面#####################################
# #####################取ip地址中
#
#
# #####################################################注册功能和登录成功的页面，已经拿到这个ip地址######################################################
# import  socket
# import selectors
# import  threading
# import time
# import  os,sys
# PATH=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.append(PATH)
# import json
# f_open = open('QQ_ID_docu.txt', 'r')
# all_dic_data = json.loads(f_open.read())
# QQ_ID = all_dic_data
# # print(QQ_ID)
#
#
# QQ_IP=open('ip_save.txt','r')
# QQ_IP=QQ_IP.read()
# print('已经取到这个ip地址：',QQ_IP)
#
#
#
#
# class normal_user_main:
#     print('开始运行这个客户端了')
#     # def __init__(self):
#     print('欢迎登录成功')
#     print('QQ用户【{}】已经上线..................................'.format(QQ_ID))
#     print('打开普通用户服务端.......................................')
#         # self.start()
#         # self.message_thread()
#     def start():
#         try:
#             client_main_menus = '''
#                        0:查看消息
#                        1,查看你的好友（在线，离线）
#                        2,个人账户信息
#                        3,搜索（个人，群，公众号等anything）
#                        4,退出此账号
#                        5,注销
#                         '''
#             # msg = input('输入：')
#             print(client_main_menus)
#             client_main_choice = input('请输入你的选择（1-5）:').strip()
#             import socket
#             sk = socket.socket()
#             # self.sk = sk
#             sk.connect((QQ_IP, 8080))
#
#             print('开始运行客户端了')
#             msg = input('输入:').strip()
#             # tcp_client.sendto(client_main_choice.encode('utf-8'), ip_port)
#             print('已经发送消息给服务端了')
#             sk.send(client_main_choice.encode('utf-8'))
#             print('已经发送')
#             data = sk.recv(1024)
#             print(data.decode('utf-8'))
#             if client_main_choice==str(0):
#                 sk.send(str(0).encode('utf-8'))
#                 message_thread()
#             elif client_main_choice == str(1):
#                 sk.send(str(1).encode('utf-8'))
#                 look_friend()
#             elif client_main_choice == str(2):
#                 personal_information()
#             elif client_main_choice == str(3):
#                 sk.send(str(3).encode('utf-8'))
#                 user_search()
#             elif client_main_choice == str(4):
#                 print('退出普通用户登录端..........')
#                 exit()
#             elif client_main_choice == str(5):
#                 sk.send(str(5).encode('utf-8'))
#                 data = sk.recv(1024)
#             elif client_main_choice == '':
#                 print('没有输入')
#             else:
#                 print('输入有误')
#         except Exception as e:
#             print(e)
#
#
#
#
# ####################################################菜单选项###############################################################################
#     def message_thread():
#         print('开启message线程页面.......................................................')
#         from  nomal_user import  self_user_main_wechat
#         self_user_main_wechat.normal_user_message()
#
#     def look_friend(self):
#         from  nomal_user import existed_friend
#         existed_friend.look_existed_friend()
#
#         # print('进入查看你的好友界面')
#
#     def personal_information(self):
#         from  nomal_user import personal_information
#         # print('进入个人账户信息页面')
#         personal_information.personal_information()
#
#     def user_search(self):
#         from  nomal_user import user_search
#         user_search.search()
#
#
#
# # normal_user_main()
# #######################开了多个线程,实现并发操作#########################################
#
#
# other_thread=threading.Thread(target=normal_user_main.start,)
# # look_friend_thread=threading.Thread(target=normal_user_main.look_friend,)
# # user_search_thread=threading.Thread(target=normal_user_main.user_search,)
# # personal_information_thread=threading.Thread(target=normal_user_main.personal_information,)
# message_thread=threading.Thread(target=normal_user_main.message_thread,)
#     # i=threading.Thread(target=FTPconnect,args=(key,value,))
# message_thread.setDaemon(True)
# # look_friend_thread.setDaemon(True)
# # user_search_thread.setDaemon(True)
# # personal_information_thread.setDaemon(True)
#
#
#
#
# ###########守护主线程###################################################
#
# message_thread.start()
# other_thread.start()
#
# print('ending................。。。。')
#
#
#
#
#
#
#
#

###############################################################################################

###################################################注册和登录成功的页面#####################################
#####################取ip地址中


#####################################################注册功能和登录成功的页面，已经拿到这个ip地址######################################################
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

print(PATH)

QQ_IP=open('ip_save.txt','r')
QQ_IP=QQ_IP.read()
print('已经取到这个ip地址：',QQ_IP)
print('#'*200)
for i in range(0,6):
    print(' ' * 10 + '#' * 2 + ' ' * 8 + '#' * 5 + ' ' * 9 + '#' * 2)
    print(' ' * 11 + '#' * 2 + ' ' * 5 + '#' * 2 + ' ' * 5 + '#' * 2 + ' ' * 5 + '#' * 2)
    print(' ' * 12 + '#' * 2 + ' ' * 3 + '#' * 2 + ' ' * 7 + '#' * 2 + ' ' * 3 + '#' * 2)
    print(' ' * 14 + '#' * 2 + ' ' * 12 + '#' * 2)
class normal_user_main:
    def __init__(self):
        import socket
        sk = socket.socket()
        # self.sk = sk
        sk.connect((QQ_IP, 8080))
        self.sk=sk
        print('开始运行这个客户端了')
        # def __init__(self):
        print('欢迎登录成功')
        print('QQ用户【{}】已经上线..................................'.format(QQ_ID))
        print('打开普通用户服务端.......................................')
        self.start()
    def start(self):
        try:
            client_main_menus = '''
                       0:查看消息
                       1,查看你的好友（在线，离线）
                       2,个人账户信息
                       3,搜索（个人，群，公众号等anything）
                       4,加好友
                       5,退出此账号
                       6,注销
                        '''
            # msg = input('输入：')
            print(client_main_menus)
            ########################做判断，是否有消息发送过来#################################
            # existed_message=sk.recv(1024)
            # if existed_message:
            #     print('存在消息，是否查看...............?????')
            print('开始运行客户端了')
            while True:
                client_main_choice = input('请输入你的选择（1-5）:').strip()
                # msg = input('输入:').strip()
                # tcp_client.sendto(client_main_choice.encode('utf-8'), ip_port)
                # print('已经发送消息给服务端了')
                # sk.send(client_main_choice.encode('utf-8'))
                # print('已经发送')
                # data = sk.recv(1024)
                # print(data.decode('utf-8'))
                if client_main_choice == str(0):
                    self.sk.send(str(0).encode('utf-8'))
                    self.message_thread()
                elif client_main_choice == str(1):
                    if not os.path.exists('add_friends/{}_friends.txt'.format(QQ_ID)):
                        print('没有好友')
                        print('请进入添加好友界面..........................................................')
                        time.sleep(3)
                        break
                    else:
                        self.sk.send(str(1).encode('utf-8'))
                        self.look_friend()
                elif client_main_choice == str(2):
                    self.personal_information()
                elif client_main_choice == str(3):
                    self.sk.send(str(3).encode('utf-8'))
                    self.user_search()
                elif client_main_choice == str(4):
                    self.sk.send(str(4).encode('utf-8'))
                    self.add_friend()
                elif client_main_choice == str(5):
                    print('退出普通用户登录端..........')
                    exit()
                elif client_main_choice == str(6):
                    self.sk.send(str(5).encode('utf-8'))
                    data = self.sk.recv(1024)
                elif client_main_choice == '':
                    print('没有输入，请重新输入，OK？')

                else:
                    print('输入有误')
        except Exception as e:
            print(e)




####################################################菜单选项###############################################################################
    def message_thread(self):
        print('开启message线程页面.......................................................')
        from  nomal_user import  self_user_main_wechat
        self_user_main_wechat.normal_user_message()

    def look_friend(self):
        print('进入查看你的好友界面')

        # open('add_friends/{}_friends.txt','w')
        with open('add_friends/{}_friends.txt'.format(QQ_ID), 'r')as fr:
            exist_friends=fr.read()
            fr.close()
        print('已经存在的好友是:',exist_friends)
        import demjson
        exist_friend=demjson.decode(exist_friends)
        self.sk.send(str(exist_friend).encode('utf-8'))
        print('已经发送全部的好友过去了')
        print('exist_frinend的类型是:',type(exist_friend))
        ###############################################后续优化#########################################
        login_friends=self.sk.recv(10240).decode('utf-8')
        print('上线的好友是:',login_friends)
        print('*'*100)
        print(login_friends)
        login_friend=demjson.decode((login_friends))
        # print(type(login_friend))
        # print(login_friend[0])
        ######################拿没有上线的好友出来
        print(len(login_friend))

        for i in range(0,len(exist_friend)):
            exist_friend[i]=demjson.decode(exist_friend[i])
            # print('类型是:',type(exist_friend[i]))
        for i in range(0,len(login_friend)):
            print(login_friend[i][0])
            login_friend[i][0]=demjson.decode(login_friend[i][0])
            print(type(login_friend[i][0]))
            # if login_friend[i][0] in exist_friend:

            exist_friend.remove(login_friend[i][0])


        print('没有上线的好友:',exist_friend)
######################################################################################
        print('>>'*1000)
        print('全部QQ好友如下：')
        for i in range(0,len(login_friend)):
            # login_friend[i][0]=demjson.decode(login_friend[i][0])
            (login_key,login_value),=login_friend[i][0].items()
            print('QQ好友{}'.format(i+1))
            print('{}【上线】'.format(login_key))
        for i in range(0,len(exist_friend)):
            print('QQ好友{}'.format(1+i+len(login_friend)))
            exist_friend[i]=demjson.decode(exist_friend[i])
            (not_login_key,not_login_value),=exist_friend[i].items()
            print('{}【离线】'.format(not_login_key))
        while True:
            friend_menus = '''
                   1,选择好友（聊天）
                   2,删除好友
                   3,管理好友
                   '''
            print(friend_menus)
            friend_menus_choice = input('请输入你的选择：')
            if friend_menus_choice == str(1):
                print('您选择了好友聊天')
                main_ip = self.sk.recv(1024).decode('utf-8')
                print('接受到这个ip地址是:')
                print(main_ip)
                ###########################拿到聊天主界面的ip的ip地址:
                if not os.path.exists('{}/nomal_user/nomal_all_ip_data'.format(PATH)):
                    os.mkdir('{}/nomal_user/nomal_all_ip_data'.format(PATH))
                    ##########################保存这个聊天界面的ip地址#################################################################################
                open('{}/nomal_user/nomal_all_ip_data/chat_main_ip/{}_main.txt'.format(PATH, QQ_ID), 'w')
                with open(('{}/nomal_user/nomal_all_ip_data/chat_main_ip/{}_main.txt'.format(PATH, QQ_ID)), 'w')as f:
                    f.write(main_ip)
                    f.close()
                from  nomal_user import nomal_user_chat_main_page
                nomal_user_chat_main_page.main_chat_nomal_user()
            elif friend_menus_choice == str(2):
                print('您选择了删除好友的功能')
            elif friend_menus_choice == str(3):
                print('您选择了管理好友的功能')
            else:
                print('输入非法')
                print('请重新输入》》》》》》》》》》》》》》》》')






            # number=input('请输入好友QQ号码：')
            # self.sk.send(str(number).encode('utf-8'))
            # print('已经发送出去')
            # number_response = self.sk.recv(1024).decode('utf-8')
            # print('接收到消息:',number_response)








        # elif friend_menus_choice==str(2):
        #     print('您选择了删除好友')
        # elif friend_menus_choice==str(3):
        #     print('您选择了管理某个好友')
        # else:
        #     print('输入不当，没有这个操作')

    def personal_information(self):

        from  nomal_user import personal_information
        print('进入个人账户信息页面')
        personal_information.personal_information()

    def user_search(self):
        from  nomal_user import user_search
        user_search.search()

    def add_friend(self):
        QQ_IP = open('ip_save.txt', 'r')
        QQ_IP = QQ_IP.read()
        print('已经取到这个ip地址：', QQ_IP)
        import json
        f_open = open('QQ_ID_docu.txt', 'r')
        all_dic_data = json.loads(f_open.read())
        QQ_ID = all_dic_data
        print('欢迎QQ用户[{}]进入加好友页面......................................................'.format(QQ_ID))
        print('进来...............................')
        add_number = input('请输入你要加的好友QQ：')
        if str(add_number)==str(QQ_ID):
            print('就是本人，别逗了，咋添加????????')
            time.sleep(3)
        else:
            self.sk.send(str(add_number).encode('utf-8'))
            print('已经发送请求给服务端>>>>>>>>>>>>>>>>>>>>>>>>>>>')
            data = self.sk.recv(1024).decode('utf-8')
            print('返回的结果:', data)
            if data == '不存在':
                pass
            else:
                choice = input('y/n:')
                if choice == 'y':
                    print('确定')
                    self.sk.send(choice.encode('utf-8'))
                    print('已经发送')
                    response = self.sk.recv(1024).decode('utf-8')
                    print('response是', response)
                    # res=self.sk.recv(1024).decode('utf-8')
                    # print(res)
                    # open('add_friends' + '.txt', 'w')
                    open('add_friends/{}_friends.txt'.format(QQ_ID), 'w')
                    with open('add_friends/{}_friends.txt'.format(QQ_ID), 'r')as fo:
                        before_data = fo.read()
                        fo.close()
                    import demjson
                    if len(before_data):
                        print('有数据')
                        before_data=demjson.decode('utf-8')
                    else:
                        dic=[]
                        with open('add_friends/{}_friends.txt'.format(QQ_ID), 'w')as fo:
                            friend_data = fo.write(str(dic))
                            fo.close()
                    with open('add_friends/{}_friends.txt'.format(QQ_ID), 'r')as fo:
                        friend_data = fo.read()
                        fo.close()
                    import demjson
                    friend_data = demjson.decode(friend_data)
                    print(len(friend_data))
                    if len(friend_data):
                        print('有数据')
                    else:
                        dic = []
                        print('没有数据')
                        with open('add_friends' + '.txt', 'w')as f:
                            f.write(str(dic))
                            f.close()
                    with open('add_friends.txt', 'r')as f:
                        add_friend_data = f.read()
                        print('已经存在的数据是:', add_friend_data)
                        f.close()
                    print(type(add_friend_data))
                    add_friend_data = demjson.decode(add_friend_data)
                    # response=demjson.decode(response)
                    print(type(response))
                    # add_friend_data.append(response)
                    # print(type(add_friend_data))
                    for i in range(0, len(add_friend_data)):
                        if str(response) == str(add_friend_data[i]):
                            print('已经存在,不必添加')
                            break
                    else:
                        add_friend_data.append(response)
                        print(add_friend_data)
                        with open('add_friends/{}_friends.txt'.format(QQ_ID), 'w')as fw:
                            fw.write(str(add_friend_data))
                            fw.close()
                        print('添加好友成功')
                else:
                    print('取消添加此好友')


normal_user_main()
#######################开了多个线程,实现并发操作#########################################


# other_thread=threading.Thread(target=normal_user_main.start,)
# look_friend_thread=threading.Thread(target=normal_user_main.look_friend,)
# user_search_thread=threading.Thread(target=normal_user_main.user_search,)
# personal_information_thread=threading.Thread(target=normal_user_main.personal_information,)
# message_thread=threading.Thread(target=normal_user_main.message_thread,)
    # i=threading.Thread(target=FTPconnect,args=(key,value,))
# message_thread.setDaemon(True)
# look_friend_thread.setDaemon(True)
# user_search_thread.setDaemon(True)
# personal_information_thread.setDaemon(True)




###########守护主线程###################################################

# message_thread.start()
# other_thread.start()

# print('ending................。。。。')


#######################################################################欢迎进入加好友的页面
# import  socket
# import selectors
# import  threading
# import time
# import  os,sys
# PATH=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.append(PATH)


#
# class add_friend:
#     QQ_IP = open('ip_save.txt', 'r')
#     QQ_IP = QQ_IP.read()
#     print('已经取到这个ip地址：', QQ_IP)
#
#     import json
#     f_open = open('QQ_ID_docu.txt', 'r')
#     all_dic_data = json.loads(f_open.read())
#     QQ_ID = all_dic_data
#     print('欢迎QQ用户[{}]进入加好友页面......................................................'.format(QQ_ID))
#     def __init__(self):
#         self.add_start()
#     def add_start(self):
#         while True:
#             print('进来...............................')
#
#             add_number = input('请输入你要加的好友QQ：')
#             self.sk.send(str(add_number).encode('utf-8'))
#             print('已经发送请求给服务端>>>>>>>>>>>>>>>>>>>>>>>>>>>')
#             data = self.sk.recv(1024)
#             print('接收到数据:', data)

# add_friend()





