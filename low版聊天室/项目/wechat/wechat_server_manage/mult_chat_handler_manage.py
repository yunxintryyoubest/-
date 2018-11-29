##############################################多用户聊天管理#################################################################


import  threading
import  time
import  socket
import selectors
import  time
#一直监听有没有客户进来
class multi_user_chat():
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
            print(data.decode('utf-8'))
            if data:
                # while True:
                print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>注明一下，这个是已经进来的用户..........................')
                #######################################################判断这个接收到的数据##################################################################
                data = data.decode('UTF-8')
                conn.send(str(send_login_QQ_ID).encode('utf-8'))
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
thread=[]
t=[]
for i in range(0,len(all_QQ)):
    # (key,value),=all_QQ.items()
    (key,value),=all_QQ[i].items()
    print('这个当前用户ip是:',value)
    print('这个当前用户是:',key)
    i=threading.Thread(target=multi_user,args=(key,value,))
    thread.append(i)
for j in thread:
    j.start()
print('ending................。。。。')