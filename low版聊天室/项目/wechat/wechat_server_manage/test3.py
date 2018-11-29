
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
        while True:
            try:
                data = conn.recv(1024)
                data = data.decode('UTF-8')
                print(data)
                print('已经接收到')
                msg = input('输入：')
                conn.send(msg.encode('utf-8'))
                print('已经发')
            except Exception as e:
                print(e)











print('执行下面的多线程')


with open('login_QQ_ID.txt','r')as f:
    all_login_ID=f.read()
    f.close()


import demjson
all_QQ=demjson.decode(all_login_ID)






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
