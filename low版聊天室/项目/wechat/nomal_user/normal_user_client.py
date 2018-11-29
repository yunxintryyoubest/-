#######################欢迎进入进入普通用户client端############################################################################


class normal_client:
    print('欢迎进入普通用户client界面')



    import socket
    sk = socket.socket()
    msg='上线'
    sk.connect(('127.1.1.2', 8080))
    while True:
        try:
            # msg = input('输入：')
            sk.send(msg.encode('utf-8'))
            print('已经发送')
            data = sk.recv(1024)
            print('接收到服务端的数据是:', data.decode('utf-8'))
        except Exception as e:
            print(e)