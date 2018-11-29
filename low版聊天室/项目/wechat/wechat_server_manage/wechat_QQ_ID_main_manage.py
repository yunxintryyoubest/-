#########################################这里是处理这个聊天的主界面的####################################################################



import  os,sys
PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(PATH)



print('进入到聊天主界面的管理系统................................................................................')
import  threading
import  time
import  socket
import selectors
import  time
import demjson
#一直监听有没有客户进来
class chat_main_manage:
    def __init__(self,QQ_ID,QQ_IP):
        self.QQ_ID=QQ_ID
        self.QQ_IP=QQ_IP
        print('开始时间是%s' % time.ctime())
        print('hello %s'%self.QQ_ID)
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
            import demjson
            # data = conn.recv(1024)
            # data=data.decode('utf-8')
            friend_choice = conn.recv(1024).decode('utf-8')
            print(friend_choice)
            print('已经接收到这个发送过来的好友QQ:', friend_choice)
            if friend_choice:
                print('接收到')

                with open('login_QQ_ID.txt', 'r')as fr:
                    reve_chat_QQ_id = fr.read()
                    fr.close()
                print(reve_chat_QQ_id)
            #     ###################################如果要请求连接的QQ号码是离线的话，就保存到数据库里面
                print(type(reve_chat_QQ_id))
                reve_chat_QQ_id = demjson.decode(reve_chat_QQ_id)
                all_login_QQ = []
                #################################################找出已经在线的好友##############################################
                for i in range(0, len(reve_chat_QQ_id)):
                    (recv_id, recv_ip), = reve_chat_QQ_id[i].items()
                    all_login_QQ.append(recv_id)
                    if str(friend_choice) == str(recv_id):
                        print('已经找到')
                        print('当前路径是:', PATH)
                        if not os.path.exists('{}/wechat_recode/{} '.format(PATH, self.QQ_ID)):
                            print('不存在这个路径，要新建这个用户的数据库')
                            os.mkdir('{}/wechat_recode/{}'.format(PATH, self.QQ_ID))
                            # break
                        print('执行文件这步')
                        chat_recode = '{}'.format(recv_id) + ' chat_recode'
                        print(chat_recode)
                        f = open('{}/wechat_recode/{}/{}  wechat_recode.txt'.format(PATH, self.QQ_ID, friend_choice),
                                 'w')
                        #####################################创建完成
                        recode = '{}  and {}wechat recode list:'.format(self.QQ_ID, friend_choice)
                        f.write(str(recode))
                        f.close()
                        print('success')

                        from wechat_server_manage import  create_main_chat_ip
                        friend_ip=create_main_chat_ip.has_ip()

                        conn.send(friend_ip.encode('utf-8'))
                        print('已经发送成功这个好友ip')

                        friend_data={}

                        friend_data[friend_choice]=friend_ip
                        print('friedn_data是,',friend_data)


                        open('self_chat_other_manage.txt','w')
                        f=open('self_chat_other_manage.txt','r')
                        before_friend_data1=f.read()
                        f.close()
                        print(len(before_friend_data1))
                        if len(before_friend_data1):
                            print('  有数据')
                            befor_friend_data = demjson.decode(before_data)
                            befor_friend_data.append(friend_data)
                        else:
                            print('没有数据')
                            dic=[]
                            start=friend_data
                            print(start)
                            dic.append(start)
                            print(dic)
                            f1 = open('self_chat_other_manage.txt', 'w')
                            f1.write(str(dic))
                            f1.close()
                        print('写入这个friend_data成功')
                        from   wechat_server_manage import self_chat_others
                        self_chat_others.multi_thread()
                    else:
                        continue
                else:
                    #######################不在线的情况
                    msg="can't send message ,{}  not online  ".format(friend_choice)
                    print('不在线')
                    conn.send(msg.encode('utf-8'))




                        ##########################################不做好友移除处理###############################################
            #             remove_friend_QQ_login = {}
            #             remove_friend_QQ_login[friend_choice] = recv_ip
            #             import os
            #             print('当前路径是:', PATH)
            #             if not os.path.exists('{}/wechat_recode/{} '.format(PATH, self.QQ_ID)):
            #                 print('不存在这个路径，要新建这个用户的数据库')
            #                 os.mkdir('{}/wechat_recode/{}'.format(PATH, self.QQ_ID))
            #                 # break
            #             print('执行文件这步')
            #             chat_recode = '{}'.format(recv_id) + ' chat_recode'
            #             print(chat_recode)
            #             f = open('{}/wechat_recode/{}/{}  wechat_recode.txt'.format(PATH, self.QQ_ID, friend_choice),  'w')
            #             #####################################创建完成
            #             recode = '{}  and {}wechat recode list:'.format(self.QQ_ID, friend_choice)
            #             f.write(str(recode))
            #             f.close()
            #             print('success')
            #             # open('QQ_IP_CHAT.txt', 'w')
            #             with  open('QQ_IP_CHAT.txt','r')as f:
            #                 remove_QQ_Friend=f.read()
            #                 f.close()
            #
            #             if len(remove_QQ_Friend):
            #                 remove_QQ_Friend=demjson.decode(remove_QQ_Friend)
            #             else:
            #                 dic=[]
            #                 with open('QQ_IP_CHAT.txt','w')as f:
            #                     f.write(str(dic))
            #                     f.close()
            #             with open('QQ_IP_CHAT.txt', 'r')as f:
            #                 before_data=f.read()
            #                 f.close()
            #             before_data=demjson.decode(before_data)
            #
            #             before_data.append(remove_friend_QQ_login)
            #             print('全部移除的好友是:',before_data)
            #
            #             with open("QQ_IP_CHAT.txt",'w')as f:
            #                 f.write(str(before_data))
            #                 f.close()
            #             # QQ_IP_chat.write(str(remove_friend_QQ_login))
            #             print('保存对应的聊天记录成功...........................................')
            #             ##########################################发送好友ip地址
            #             from  wechat_server_manage import create_main_chat_ip
            #             others_ip = create_main_chat_ip.has_ip()
            #
            #             conn.send(others_ip.encode('utf-8'))
            #             print('已经发送成功')
            #             from   wechat_server_manage  import self_chat_others
            #             self_chat_others.multi_user()
            #             break
            #             ################当选择某个好友聊天的时候，就切换到了一个页面
            #         else:
            #             continue
            #     else:
            #         #######################不在线的情况
            #         msg="can't send message ,{}  not online  ".format(friend_choice)
            #         print('不在线')
            #         conn.send(msg.encode('utf-8'))
            # else:
            #     print('没有收到消息')
        except Exception as e:
            print(e)
            print('异常')


#########################################多线程处理############################################

#############################当最外面的下线之后，就清除这个上线记录,拿到之前存在的上线记录

        #############################################################移除上线的好友



                        # with open('login_QQ_ID.txt', 'r')as f:
                        #     exist_data = f.read()
                        #     f.close()
                        # import demjson
                        # remove_data = demjson.decode(exist_data)
                        # print('要移除的好友QQ用户:', remove_friend_QQ_login)
                        # print('已经存在的全部的好友:', remove_data)
                        # for i in range(0, len(remove_data)):
                        #     (key, value), = remove_data[i].items()
                        #     if str(key) == str(friend_choice):
                        #         print('已经找到')
                        #         remove_data.remove(remove_data[i])
                        #         fr = open('login_QQ_ID.txt', 'w')
                        #         fr.write(str(remove_data))
                        #         fr.close()
                        #         print('移除成功，这个选择要聊天的好友')








with open('self_QQ_main_chat.txt','r')as f:
    all_QQ_main=f.read()
    f.close()
all_QQ_id_ip_main=demjson.decode(all_QQ_main)
print(type(all_QQ_id_ip_main))


###############################################把自己移除后要加进这个登录记录数据库里面才能显示在线

# with open('login_QQ_ID.txt','r')as f:
#     login_QQ_data=f.read()
#     f.close()
#
# login_QQ_data=demjson.decode(login_QQ_data)
# add_login_QQ_data=login_QQ_data.append(all_QQ_id_ip_main)
# print('已经添加成功')


thread=[]
t=[]
for i in range(0,len(all_QQ_id_ip_main)):
    # (key,value),=all_QQ.items()
    (key,value),=all_QQ_id_ip_main[i].items()
    print('这个在main界面聊天用户ip是:',value)
    print('这个在main主界面的QQ用户是:',key)
    i = threading.Thread(target=chat_main_manage, args=(key, value,))
    thread.append(i)
for j in thread:
    j.start()
print('ending................。。。。')

