##########进入普通用户验证环节,登录环节#############################################################################
import  threading
import time
import  os,sys
PATH=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(PATH)
class user_authenticate:
    print('auth开始')
    print('进入普通用户验证环节...........................')
    import socket
    sk=socket.socket()
    sk.connect(('127.0.0.2',8080))
    while True:
        try:
            # QQ_number = int(input('请输入QQ号码:'))
            QQ_number = input('请输入QQ号码:')
            # while True:
            #     if type(QQ_number) == str:
            #         print('输入格式错误,重新输入')
            #         QQ_number = input('请输入QQ号码:')
            #     else:
            #         print('格式正确')
            #         break
            QQ_password = str(input('请输入QQ密码：'))
            print(QQ_password)
            print(QQ_number)
            # print(type(QQ_number))
            # print(type(QQ_password))
            normal_user_dict = {}
            # normal_user_dict = {QQ_number:QQ_password}
            normal_user_dict[QQ_number] = QQ_password

            # normal_user_dict.replace("'","")
            print(normal_user_dict)
            # sk.send(str(normal_user_dict))

            sk.send(str(normal_user_dict).encode('utf-8'))
            # sk.send(normal_user_dict)
            print('已经发送')
            data = sk.recv(1024)
            print('服务端发回消息.................................................................')
            #####################################################################拿到对应的ip地址中
            print('接收到服务端的数据是:', data.decode('utf-8'))
            data = data.decode('utf-8')

            if data == 'auth fail,please input again':
                print('验证失败.................')
                import  time
                time.sleep(3)
                print(' ' * 10 + '#' * 2 + ' ' * 8 + '#' * 5 + ' ' * 9 + '#' * 2)
                print(' ' * 11 + '#' * 2 + ' ' * 5 + '#' * 2 + ' ' * 5 + '#' * 2 + ' ' * 5 + '#' * 2)
                print(' ' * 12 + '#' * 2 + ' ' * 3 + '#' * 2 + ' ' * 7 + '#' * 2 + ' ' * 3 + '#' * 2)
                print(' ' * 14 + '#' * 2 + ' ' * 12 + '#' * 2)
                print('#' * 200)
            else:
                print(len(data))
                print('authenticate  success')
                print('欢迎QQ用户【{}】登录聊天室........'.format(QQ_number))
                ###########创建文件夹
                import os
                # os.mkdir('C:/Users/Public/Documents/{}.txt'.format(QQ_personal_data))
                QQ_docu = open('C:/Users/Public/Documents/' + '{}'.format(QQ_number) + ".txt", 'w')
                QQ_docu = open('{}'.format(QQ_number) + ".txt", 'w')
                QQ_docu.write(str(QQ_number))
                print('写入文件')
                QQ_docu.close()
                #############################在main首页取这个登录的QQ号码###########################################################
                docu = open('QQ_ID_docu' + '.txt', 'w')
                docu.write(str(QQ_number))
                docu.close()
                print('拿到的这个ip地址是:', data)
                #################################把ip地址写入文件里面
                ip_save = open('ip_save' + '.txt', 'w')
                ip_save.write(data)
                ip_save.close()
                print('已经生成ip地址文件..................................................')
                from  nomal_user import nomal_user_main
                nomal_user_main.normal_user_main()
        except Exception as e:
            print(e)





            # import socket
    # sk = socket.socket()
    # ip_addr_user=input('请输入想添加的好友QQ号码:')
    # sk.connect(('127.1.1.2', 8080))
    # while True:
    #     try:
    #         msg = input('输入：')
    #         sk.send(msg.encode('utf-8'))
    #         print('已经发送')
    #         data = sk.recv(1024)
    #         print('接收到服务端的数据是:', data.decode('utf-8'))
    #     except Exception as e:
    #         print(e)









